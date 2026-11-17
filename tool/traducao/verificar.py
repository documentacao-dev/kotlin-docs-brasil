#!/usr/bin/env python3
"""Confere as páginas traduzidas da documentação do Kotlin (Writerside) contra o inglês.

Para cada docs/topics/**/*.md cuja ÚLTIMA linha é `<!-- ia-translate: true -->`,
compara com o inglês do commit em tool/traducao/ultimo-sync-upstream.txt (`git show`):

- linha `[//]: # (title: ...)` presente nos dois (o texto pode ser traduzido);
- blocos de código (``` e ~~~ e <code-block>) idênticos e na mesma ordem;
- tags XML/Writerside (<tabs>, <tab title>, <note>, <deflist>, <def title>,
  <procedure>, <step>, <include from>, <a href>, <img>...) com o mesmo nome, na
  mesma ordem e com os mesmos atributos; só o texto de atributos visíveis
  (title, collapsed-title, alt, caption, summary, label) pode mudar.
  Tags de formatação inline (b, strong, em, i, br, code, emphasis, control,
  path, ui-path) só geram AVISO;
- blocos de atributos `{...}` (`{style="note"}`, `{kotlin-runnable="true"}`,
  `{width="700"}`...) idênticos, exceto o texto de collapsed-title/title;
- URLs de links Markdown e definições `[ref]: url` idênticas;
- comentários HTML <!-- --> idênticos (exceto o marcador);
- variáveis %nome% iguais;
- mesmo número e nível de títulos #, mesmo número de itens de lista;
- título com texto traduzido leva o id do inglês: `## Título {id="slug-em-inglês"}`
  (ancorar_titulos.py grava); id explícito do inglês fica idêntico;
- código inline que não existe no inglês vira AVISO.

Uso: python3 tool/traducao/verificar.py [caminhos .md...]
Saída: `ERRO arquivo: ...` e `N arquivo(s) traduzido(s), M erro(s)`; exit 1 se houver erro.
"""
import re
import sys
from collections import Counter
from pathlib import Path

from comum import (MARCADOR, ROOT, commit_upstream, id_explicito, ids_do_ingles, ingles,
                   mascarar_codigo, paginas, sem_id, titulos, traduzido)

ATTR_TRADUZIVEIS = ('title', 'collapsed-title', 'alt', 'caption', 'summary', 'label')
INLINE = {'b', 'strong', 'em', 'i', 'u', 's', 'br', 'code', 'emphasis', 'control', 'path',
          'ui-path', 'sup', 'sub', 'shortcut', 'format', 'p'}
TITULO_PAGINA = re.compile(r'^\[//\]: # \(title: (.*)\)\s*$', re.M)
COMENTARIO = re.compile(r'<!--.*?-->', re.S)
TAG = re.compile(r'</?([a-zA-Z][\w-]*)\b((?:[^>"\']|"[^"]*"|\'[^\']*\')*)/?>')
CHAVES = re.compile(r'\{\s*[\w-]+\s*=\s*"[^"]*"(?:\s+[\w-]+\s*=\s*"[^"]*")*\s*\}')
NOMES = '|'.join(re.escape(a) for a in ATTR_TRADUZIVEIS)


def neutralizar(s):
    """Esvazia o texto dos atributos visíveis e normaliza espaços."""
    s = re.sub(rf'(?<![\w-])({NOMES})\s*=\s*"[^"]*"', r'\1=""', s)
    s = re.sub(rf"(?<![\w-])({NOMES})\s*=\s*'[^']*'", r"\1=''", s)
    return re.sub(r'\s+', ' ', s)


def sem_inline_code(t):
    return re.sub(r'(`+)(.+?)\1', '', t)


def corpo(t):
    """Texto sem código, linha a linha (mesmos índices)."""
    blocos, linhas = mascarar_codigo(t)
    return blocos, '\n'.join(linhas)


def conferir(p, commit):
    rel = p.resolve().relative_to(ROOT).as_posix()
    en = ingles(p, commit)
    if en is None:
        return [f'{rel}: não existe no upstream ({commit[:9]})'], []
    pt = p.read_text()
    erros, avisos = [], []
    if not traduzido(pt):
        erros.append(f'falta o marcador `{MARCADOR}` na última linha')

    # título da página
    if len(TITULO_PAGINA.findall(en)) != len(TITULO_PAGINA.findall(pt)):
        erros.append('linha `[//]: # (title: ...)` diferente do inglês (deve existir e ficar nesse formato)')

    # código
    be, ce = corpo(en)
    bp, cp = corpo(pt)
    if be != bp:
        msg = f'blocos de código: {len(be)} no inglês, {len(bp)} na tradução'
        if len(be) == len(bp):
            i = next(i for i, (a, b) in enumerate(zip(be, bp)) if a != b)
            msg += f' (o {i + 1}º é diferente: `{be[i].splitlines()[0][:60]}`)'
        erros.append(msg)

    # comentários HTML
    come = COMENTARIO.findall(ce)
    comp = [c for c in COMENTARIO.findall(cp) if c.strip() != MARCADOR]
    if come != comp:
        erros.append(f'comentários <!-- --> diferentes do inglês ({len(come)} no inglês, {len(comp)} na tradução)')
    ce, cp = COMENTARIO.sub('', ce), COMENTARIO.sub('', cp)
    ce_s, cp_s = sem_inline_code(ce), sem_inline_code(cp)

    # tags
    def tags(t):
        estrut, inline = [], []
        for m in TAG.finditer(t):
            (inline if m.group(1).lower() in INLINE else estrut).append(neutralizar(m.group(0)))
        return estrut, inline
    te, ie = tags(ce_s)
    tp, ip = tags(cp_s)
    if te != tp:
        if len(te) != len(tp):
            erros.append(f'tags XML: {len(te)} no inglês, {len(tp)} na tradução'
                         f' ({_primeira_diferenca(te, tp)})')
        else:
            a, b = next((a, b) for a, b in zip(te, tp) if a != b)
            erros.append(f'tag diferente do inglês: `{a[:90]}` -> `{b[:90]}`')
    if Counter(re.sub(r'\s.*', '', x) for x in ie) != Counter(re.sub(r'\s.*', '', x) for x in ip):
        avisos.append(f'{rel}: tags de formatação inline (<b>, <code>, <br>...) diferentes do inglês')

    # blocos {atributos}, fora os {id} dos títulos (conferidos abaixo)
    def chaves(t):
        out = []
        for linha in t.split('\n'):
            if re.match(r'^#{1,6}\s', linha):
                continue
            out += [neutralizar(c) for c in CHAVES.findall(linha)]
        return out
    ke, kp = chaves(ce_s), chaves(cp_s)
    if ke != kp:
        erros.append(f'blocos de atributos {{...}}: {len(ke)} no inglês, {len(kp)} na tradução'
                     f' ({_primeira_diferenca(ke, kp)})')

    # links
    url = lambda t: re.findall(r'\]\(([^)\s]*)', t) + re.findall(r'^\s*\[[^\]]+\]:\s*(\S+)', t, re.M)
    ue, up = url(ce_s), url(cp_s)
    if ue != up:
        erros.append(f'URLs de links diferentes do inglês ({_primeira_diferenca(ue, up)})')

    # variáveis
    var = lambda t: Counter(re.findall(r'%[A-Za-z][\w-]*%', t))
    if var(ce) != var(cp):
        erros.append('variáveis %nome% diferentes do inglês')

    # títulos e listas
    tit_e, tit_p = titulos(en), titulos(pt)
    if [n for n, *_ in tit_e] != [n for n, *_ in tit_p]:
        erros.append(f'títulos #: {len(tit_e)} no inglês, {len(tit_p)} na tradução (ou níveis diferentes)')
    else:
        for (_, _, txe, ae, _), (_, _, txp, ap, _), id_en in zip(tit_e, tit_p, ids_do_ingles(en)):
            idp = id_explicito(ap)
            if sem_id(ae) != sem_id(ap):
                erros.append(f'título "{txp[:50]}": atributos `{{{ap or ""}}}` diferentes do inglês `{{{ae or ""}}}`')
            elif idp and idp != id_en:
                erros.append(f'título "{txp[:50]}": id `{idp}`, deveria ser `{id_en}` (rode ancorar_titulos.py)')
            elif not idp and (txe.strip() != txp.strip() or id_explicito(ae)):
                erros.append(f'título "{txp[:50]}": falta `{{id="{id_en}"}}` (rode ancorar_titulos.py)')
    item = lambda t: len(re.findall(r'^\s*(?:[-*+]|\d+\.)\s+\S', t, re.M))
    if item(ce) != item(cp):
        erros.append(f'itens de lista: {item(ce)} no inglês, {item(cp)} na tradução')

    # código inline novo
    inl = lambda t: {m.group(2).strip() for m in re.finditer(r'(`+)(.+?)\1', t)}
    for c in sorted(inl(cp) - inl(ce))[:5]:
        avisos.append(f'{rel}: código inline que não existe no inglês (traduzido?): `{c}`')

    return [f'{rel}: {e}' for e in erros], avisos


def _primeira_diferenca(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return f'1ª diferença: `{x[:70]}` -> `{y[:70]}`'
    if len(a) > len(b):
        return f'falta `{a[len(b)][:70]}`'
    if len(b) > len(a):
        return f'sobra `{b[len(a)][:70]}`'
    return ''


def main():
    args = sys.argv[1:]
    commit = commit_upstream()
    arquivos = [Path(a).resolve() for a in args] if args else [p for p in paginas() if traduzido(p.read_text())]
    todos = []
    for p in arquivos:
        erros, avisos = conferir(p, commit)
        todos += erros
        for a in avisos:
            print(f'AVISO {a}')
    for e in todos:
        print(f'ERRO {e}')
    print(f'{len(arquivos)} arquivo(s) traduzido(s), {len(todos)} erro(s)')
    sys.exit(1 if todos else 0)


if __name__ == '__main__':
    main()
