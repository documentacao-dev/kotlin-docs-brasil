#!/usr/bin/env bash
# Build do site kotlin.documentacao.dev com o Writerside, saída em site/.
#
# - copia docs/ para uma pasta temporária e traduz lá os toc-title do kr.tree a
#   partir de tool/site/toc-pt-BR.json (o kr.tree do repositório fica igual ao
#   upstream, sem conflito no sync);
# - roda o builder oficial (Docker jetbrains/writerside-builder) para a instância
#   kotlin-reference/kr e extrai o HTML e as imagens em site/;
# - pós-processa o HTML (tool/site/pos_build.py): lang="pt-BR", interface em
#   português, sem analytics/feedback, aviso de página em inglês e rodapé com
#   atribuição.
#
# Uso: tool/site/build.sh
# Variáveis: WRS_VERSAO (tag da imagem), WRS_PULAR=1 reaproveita o zip do último
# build em .wrs-build/ e só refaz o pós-processamento.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

# 2025.07.8502 (a do writerside.cfg) não existe no Docker Hub; esta é a mais próxima.
WRS_VERSAO=${WRS_VERSAO:-2025.11.8530}
TRAB="$PWD/.wrs-build"

if [ "${WRS_PULAR:-0}" != 1 ]; then
    rm -rf "$TRAB"
    mkdir -p "$TRAB/src" "$TRAB/out"
    # cópia sem .git: o builder roda `git log` no repositório e trava em clone parcial
    cp -R docs "$TRAB/src/docs"
    python3 tool/site/traduzir_toc.py "$TRAB/src/docs/kr.tree" tool/site/toc-pt-BR.json

    plataforma=()
    [ "$(uname -m)" = arm64 ] || [ "$(uname -m)" = aarch64 ] && plataforma=(--platform linux/amd64)
    # o builder sai com código != 0 quando a inspeção acha problema (ex.: imagem
    # faltando na test-page.md do upstream), mas gera o site; quem decide é o zip.
    docker run --rm "${plataforma[@]}" \
        -e SOURCE_DIR=/opt/sources -e MODULE_INSTANCE=kotlin-reference/kr \
        -e OUTPUT_DIR=/opt/out/site -e RUNNER=other \
        -v "$TRAB/src:/opt/sources" -v "$TRAB/out:/opt/out" \
        "jetbrains/writerside-builder:$WRS_VERSAO" > "$TRAB/builder.log" 2>&1 || true
    grep -E '^Inspection failed|^Help for|^Building' "$TRAB/builder.log" || true
fi

zip="$TRAB/out/site/webHelpKR2.zip"
if [ ! -f "$zip" ]; then
    echo "ERRO: o builder não gerou $zip (log em $TRAB/builder.log)" >&2
    tail -40 "$TRAB/builder.log" >&2
    exit 1
fi

rm -rf site
mkdir site
unzip -q "$zip" -d site
unzip -q -o "$TRAB/out/site/webHelpImages.zip" -d site/images
python3 tool/site/pos_build.py site
echo "site/ pronto ($(find site -type f | wc -l | tr -d ' ') arquivos)"
