#!/usr/bin/env python3
"""Fixa nos títulos traduzidos o id que o Writerside geraria do título em inglês.

Para cada .md com o marcador `<!-- ia-translate: true -->` na última linha, lê o
inglês do commit em ultimo-sync-upstream.txt e, título a título (na mesma ordem):

- título do inglês com {id="..."}: o traduzido fica com o mesmo id;
- sem id: grava `{id="<slug do título em inglês>"}` (regra do Writerside em
  comum.slug, com -1, -2 para repetidos). Se o título já tem `{...}` com outros
  atributos (collapsible, initial-collapse-state...), o id entra no mesmo bloco;
- título idêntico ao inglês e sem id no original: não mexe (o id gerado é o mesmo);
- atributos numa linha `{id="..."}` logo abaixo do título: não mexe (a linha fica
  idêntica ao inglês e o verificar.py confere).

Assim os links `pagina.md#ancora` e kotlinlang.org/docs/...#ancora continuam
valendo na tradução.

Uso: python3 tool/traducao/ancorar_titulos.py [caminhos .md...]
"""
import sys
from pathlib import Path

from comum import (commit_upstream, id_explicito, ids_do_ingles, ingles, paginas, sem_id,
                   titulos, traduzido)


def ancorar(p, commit):
    en = ingles(p, commit)
    if en is None:
        print(f'ERRO {p}: não existe no upstream')
        return False
    pt = p.read_text()
    te, tp = titulos(en), titulos(pt)
    if len(te) != len(tp):
        print(f'ERRO {p}: {len(te)} títulos no inglês, {len(tp)} na tradução')
        return False
    linhas = pt.split('\n')
    for (nivel, _, txe, ae, se), (_, i, txp, ap, sp), id_en in zip(te, tp, ids_do_ingles(en)):
        if se or sp:
            continue  # atributos numa linha `{...}` abaixo do título: ficam como no inglês
        if txe.strip() == txp.strip() and not id_explicito(ae) and not id_explicito(ap):
            continue
        outros = sem_id(ap) or sem_id(ae)
        attrs = f'id="{id_en}"' + (f' {outros}' if outros else '')
        linhas[i] = f'{"#" * nivel} {txp.strip()} {{{attrs}}}'
    novo = '\n'.join(linhas)
    if novo != pt:
        p.write_text(novo)
        print(f'ancorado {p}')
    return True


def main():
    commit = commit_upstream()
    args = sys.argv[1:]
    arquivos = [Path(a).resolve() for a in args] if args else [p for p in paginas() if traduzido(p.read_text())]
    ok = all([ancorar(p, commit) for p in arquivos])
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
