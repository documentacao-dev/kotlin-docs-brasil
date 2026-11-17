#!/usr/bin/env python3
"""Pós-processa o HTML gerado pelo Writerside para kotlin.documentacao.dev.

- `lang="pt-BR"`: o app.js do Writerside já traz a interface em pt-BR (i18next)
  e escolhe o idioma pelo atributo lang do <html>; "On this page", busca,
  "Last modified", "Was this page helpful?", anterior/próxima etc. saem em português;
- títulos, cabeçalho, og:locale, canonical e og:url do nosso domínio, data da
  última modificação em português, "Editar página" aponta para o fork;
- remove rastreamento: Google Tag Manager, analytics.js da JetBrains, widget de
  feedback (posta em forms-service.jetbrains.com) e Disqus; no config.json
  desliga o feedbackWidget;
- página sem o marcador `<!-- ia-translate: true -->` ganha a faixa "esta página
  ainda está em inglês"; todas ganham o rodapé com atribuição e link para o
  original em kotlinlang.org/docs.

Uso: python3 tool/site/pos_build.py site
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / 'tool' / 'traducao'))
from comum import traduzido  # noqa: E402

DOMINIO = 'https://kotlin.documentacao.dev'
ORIGINAL = 'https://kotlinlang.org/docs'
FORK = 'https://github.com/documentacao-dev/kotlin-docs-brasil'
MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto',
         'setembro', 'outubro', 'novembro', 'dezembro']
MESES_EN = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
            'September', 'October', 'November', 'December']

ESTILO = '''<style id="documentacao-dev">
.ddev-aviso{margin:0 0 24px;padding:12px 16px;border-radius:8px;border:1px solid rgba(48,127,255,.35);background:rgba(48,127,255,.08);font-size:15px;line-height:1.5}
.ddev-rodape{margin:40px 0 0;padding:20px 0 8px;border-top:1px solid rgba(128,128,128,.25);font-size:13px;line-height:1.6;opacity:.8}
.ddev-rodape p{margin:0 0 6px}
</style>'''


def paginas_traduzidas():
    """{nome do html: traduzido?} a partir de docs/topics."""
    out = {}
    for p in (RAIZ / 'docs' / 'topics').rglob('*'):
        if p.suffix in ('.md', '.topic'):
            out[p.stem + '.html'] = p.suffix == '.md' and traduzido(p.read_text())
    return out


def data_pt(m):
    d, mes, a = m.group(1), m.group(2), m.group(3)
    if mes not in MESES_EN:
        return m.group(0)
    return f'<div class="last-modified">{int(d)} de {MESES[MESES_EN.index(mes)]} de {a}</div>'


def processar(arq, ok_traducao):
    t = arq.read_text()
    nome = arq.name
    t = t.replace('<html lang="en-US"', '<html lang="pt-BR"', 1)
    # rastreamento
    t = re.sub(r'<script>\s*\(function \(w, d, s, l, i\).*?googletagmanager.*?</script>', '', t, flags=re.S)
    t = re.sub(r'<script src="https://resources\.jetbrains\.com/storage/help-app/v\d+/analytics\.js"></script>', '', t)
    t = re.sub(r'<noscript><iframe[^>]*googletagmanager.*?</noscript>', '', t, flags=re.S)
    t = t.replace('<div data-feedback-placeholder="true"></div>', '')
    t = t.replace('<div id="disqus_thread"></div>', '')
    # metadados
    t = t.replace(f'href="{ORIGINAL}/{nome}"', f'href="{DOMINIO}/{nome}"')
    t = t.replace(f'content="{ORIGINAL}/{nome}"', f'content="{DOMINIO}/{nome}"')
    t = t.replace('content="en_US"', 'content="pt_BR"').replace('"inLanguage":"en-US"', '"inLanguage":"pt-BR"')
    t = t.replace(' | Kotlin Documentation</title>', ' | Documentação do Kotlin</title>')
    t = t.replace('<h3>Kotlin  Help</h3>', '<h3>Documentação do Kotlin</h3>')
    t = t.replace('content="Kotlin Help"', 'content="Documentação do Kotlin"')
    t = t.replace('https://github.com/JetBrains/kotlin-web-site/edit/master/', f'{FORK}/edit/master/')
    t = re.sub(r'<div class="last-modified">(\d{1,2}) (\w+) (\d{4})</div>', data_pt, t)
    # aviso e rodapé
    original = f'{ORIGINAL}/{nome}'
    if '<article class="article"' in t:
        t = t.replace('</head>', ESTILO + '</head>', 1)
        if not ok_traducao:
            aviso = ('<div class="ddev-aviso" role="note">Esta página ainda não foi traduzida e está em inglês. '
                     f'<a href="{FORK}">Ajude a traduzir</a> ou leia o <a href="{original}">original em kotlinlang.org</a>.</div>')
            t = re.sub(r'(<article class="article"[^>]*>(?:<h1\b.*?</h1>)?)', lambda m: m.group(1) + aviso, t, count=1, flags=re.S)
        rodape = ('<footer class="ddev-rodape">'
                  '<p>Tradução comunitária da documentação oficial do Kotlin (JetBrains, Apache 2.0). '
                  f'Original em <a href="{original}">kotlinlang.org/docs</a>.</p>'
                  f'<p>Parte do <a href="https://documentacao.dev">documentacao.dev</a>. '
                  f'<a href="{FORK}">Código no GitHub</a>. Kotlin é marca registrada da JetBrains; '
                  'este site não é afiliado à JetBrains nem à Kotlin Foundation.</p></footer>')
        t = t.replace('</article>', rodape + '</article>', 1)
    arq.write_text(t)


def main(site):
    site = Path(site)
    status = paginas_traduzidas()
    htmls = sorted(site.glob('*.html'))
    for arq in htmls:
        processar(arq, status.get(arq.name, False))
    cfg = site / 'config.json'
    if cfg.exists():
        c = json.loads(cfg.read_text())
        c['feedbackWidget'] = False
        for k in ('feedbackUrl', 'feedbackSupport', 'webmaster'):
            c.pop(k, None)
        c['productName'] = 'Kotlin'
        cfg.write_text(json.dumps(c, ensure_ascii=False))
    restantes = [a.name for a in htmls if re.search(r'googletagmanager|analytics\.js|disqus_thread', a.read_text())]
    if restantes:
        print(f'ERRO: rastreamento ainda presente em {restantes[:5]}', file=sys.stderr)
        sys.exit(1)
    n = sum(1 for a in htmls if status.get(a.name))
    print(f'pós-build: {len(htmls)} páginas, {n} traduzida(s)')


if __name__ == '__main__':
    main(sys.argv[1])
