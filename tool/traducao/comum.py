"""Funções comuns às ferramentas de tradução da documentação do Kotlin (Writerside)."""
import html
import os
import re
import subprocess
import unicodedata
from pathlib import Path

GIT_ROOT = Path(__file__).resolve().parents[2]
ROOT = Path(os.environ.get('VERIFICAR_RAIZ') or GIT_ROOT)
TOPICS = ROOT / 'docs' / 'topics'
MARCADOR = '<!-- ia-translate: true -->'


def paginas():
    """Páginas traduzíveis: docs/topics/**/*.md."""
    return sorted(TOPICS.rglob('*.md'))


def traduzido(texto):
    linhas = [l for l in texto.splitlines() if l.strip()]
    return bool(linhas) and linhas[-1].strip() == MARCADOR


def commit_upstream():
    return (Path(__file__).parent / 'ultimo-sync-upstream.txt').read_text().strip()


def ingles(p, commit):
    """Texto do arquivo no commit do upstream (None se não existir)."""
    rel = Path(p).resolve().relative_to(ROOT).as_posix()
    r = subprocess.run(['git', '-C', str(GIT_ROOT), 'show', f'{commit}:{rel}'],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


CERCA = re.compile(r'^\s*(`{3,}|~{3,})')


def mascarar_codigo(t):
    """Devolve (blocos, linhas) com os blocos de código (cercados e <code-block>)
    trocados por linhas vazias, para que o resto da análise não os veja.
    `linhas` tem o mesmo número de linhas de `t`."""
    blocos, linhas, dentro, cerca, tipo = [], [], None, None, None
    for linha in t.split('\n'):
        if dentro is None:
            m = CERCA.match(linha)
            if m:
                cerca, dentro, tipo = m.group(1), [linha], 'cerca'
                linhas.append('')
                continue
            if re.match(r'^\s*<code-block\b', linha):
                dentro, tipo = [linha], 'tag'
                linhas.append('')
                if re.search(r'</code-block>|/>\s*$', linha):
                    blocos.append(linha)
                    dentro = None
                continue
            linhas.append(linha)
        else:
            dentro.append(linha)
            linhas.append('')
            if tipo == 'cerca':
                m = CERCA.match(linha)
                fecha = m and m.group(1)[0] == cerca[0] and len(m.group(1)) >= len(cerca) and linha.strip() == m.group(1)
            else:
                fecha = '</code-block>' in linha
            if fecha:
                blocos.append('\n'.join(dentro))
                dentro = None
    if dentro is not None:
        blocos.append('\n'.join(dentro))
    return blocos, linhas


TITULO = re.compile(r'^(#{1,6})\s+(.*?)\s*$')
ATRIBUTOS_TITULO = re.compile(r'\s*\{([^{}]*)\}\s*$')
ID_ATTR = re.compile(r'(?<![\w-])id\s*=\s*(?:"([^"]*)"|([\w.-]+))')
LINHA_ATRIBUTOS = re.compile(r'^\s*\{([^{}]*=[^{}]*)\}\s*$')


def titulos(t):
    """[(nível, índice da linha, texto, atributos, linha_seguinte)] dos títulos # fora de código.
    `atributos` é o conteúdo do `{...}` no fim do título ou, se não houver, o de uma
    linha `{...}` logo abaixo do título (então `linha_seguinte` é True)."""
    _, linhas = mascarar_codigo(t)
    out = []
    for i, linha in enumerate(linhas):
        m = TITULO.match(linha)
        if not m:
            continue
        texto, attrs, seguinte = m.group(2), None, False
        a = ATRIBUTOS_TITULO.search(texto)
        if a and '=' in a.group(1):
            texto, attrs = texto[:a.start()], a.group(1).strip()
        elif i + 1 < len(linhas) and LINHA_ATRIBUTOS.match(linhas[i + 1]):
            attrs, seguinte = LINHA_ATRIBUTOS.match(linhas[i + 1]).group(1).strip(), True
        out.append((len(m.group(1)), i, texto, attrs, seguinte))
    return out


def id_explicito(attrs):
    m = ID_ATTR.search(attrs or '')
    return (m.group(1) if m.group(1) is not None else m.group(2)) if m else None


def sem_id(attrs):
    return re.sub(r'\s+', ' ', ID_ATTR.sub('', attrs or '')).strip()


def slug(titulo):
    """Id que o Writerside gera para um título sem {id}.

    Regra observada no HTML gerado (builder 2025.11): texto puro do título
    (links viram o texto; entidades &lt; &gt; viram < >; o conteúdo do código
    inline conta, inclusive `<T>`), em minúsculas; letras acentuadas perdem o
    acento; tudo o que não é letra/dígito ASCII vira separador; separadores
    seguidos viram um só hífen; hífens nas pontas saem. Títulos repetidos na
    página ganham -1, -2... (ids_do_ingles)."""
    t = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', titulo)   # links e imagens: fica o texto
    t = html.unescape(t).replace('`', '')
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = t.lower()
    t = re.sub(r'[^a-z0-9]+', '-', t)
    return t.strip('-')


def ids_do_ingles(en):
    """Id final de cada título do inglês: o {id} explícito ou o slug (repetidos ganham sufixo)."""
    vistos, out = {}, []
    for _, _, texto, attrs, _ in titulos(en):
        explicito = id_explicito(attrs)
        if explicito:
            out.append(explicito)
            continue
        base = slug(texto)
        n = vistos.get(base, 0)
        vistos[base] = n + 1
        out.append(base if n == 0 else f'{base}-{n}')
    return out
