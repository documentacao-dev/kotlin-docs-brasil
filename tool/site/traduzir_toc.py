#!/usr/bin/env python3
"""Traduz os toc-title de um kr.tree (cópia do build) com o dicionário JSON.

Uso: python3 tool/site/traduzir_toc.py <kr.tree> <toc-pt-BR.json>
Título sem tradução no JSON fica em inglês. Os toc-element sem toc-title usam o
título da própria página, que vem traduzido quando a página é traduzida.
"""
import html
import json
import re
import sys
from pathlib import Path


def main(tree, dicionario):
    pt = json.loads(Path(dicionario).read_text())
    t = Path(tree).read_text()
    trocas = 0

    def trocar(m):
        nonlocal trocas
        en = html.unescape(m.group(1))
        if en in pt:
            trocas += 1
            return f'toc-title="{html.escape(pt[en], quote=True)}"'
        return m.group(0)

    t = re.sub(r'toc-title="([^"]*)"', trocar, t)
    Path(tree).write_text(t)
    print(f'toc: {trocas} títulos traduzidos')


if __name__ == '__main__':
    main(*sys.argv[1:])
