# CLAUDE.md

Tradução PT-BR da documentação do **Kotlin**, fork de `JetBrains/kotlin-web-site` (branch `master`), parte da org [`documentacao-dev`](https://github.com/documentacao-dev). Original: https://kotlinlang.org/docs. Publicado em https://kotlin.documentacao.dev (site Firebase `kotlin-documentacao`, projeto `transliteradu`). Licença: Apache 2.0, com atribuição à JetBrains no rodapé de cada página.

- Conteúdo traduzível: `docs/topics/**/*.md` (Markdown do Writerside), traduzido no lugar. Fora disso fica em inglês: `docs/topics/*.topic`, `docs/snippets/`, `docs/v.list` e o site Next.js do kotlinlang.org (raiz do repositório, não usamos).
- O clone usa sparse checkout (`docs` e `.github`). Arquivos fora disso (`tool/`, `.claude/`, `CLAUDE.md`, `firebase.json`) entram com `git add --sparse`.
- Comandos `gh` sempre com `-R documentacao-dev/kotlin-docs-brasil`. Nunca abra PR no upstream.
- Sync: merge de `upstream/master`, retradução só do que mudou, atualização de `tool/traducao/ultimo-sync-upstream.txt` com o sha do upstream.

## Modelo da tradução: sempre Haiku

Toda tradução e retradução de página roda no **Haiku** (`model: haiku`), local ou na nuvem. O agente `.claude/agents/traduzir-pt-br.md` já declara isso; não troque. Orquestrador que dispara subagentes passa `model: "haiku"`. O modelo principal só orquestra (merge, scripts, commits). Revisão de tradução: subagente de contexto limpo que lê 100% lado a lado e declara `COBERTURA`.

## Build

`tool/site/build.sh` gera o site estático em `site/` (gitignored):

1. copia `docs/` para uma pasta temporária e aplica lá a tradução dos `toc-title` do `kr.tree` a partir de `tool/site/toc-pt-BR.json` (o `kr.tree` do repositório fica igual ao upstream, sem conflito no sync);
2. roda o builder oficial em Docker (`jetbrains/writerside-builder`, versão em `WRS_VERSAO` no script; a 2025.07.8502 do `writerside.cfg` não existe no Docker Hub) para a instância `kotlin-reference/kr`; o builder gera um zip, que é extraído em `site/`;
3. `tool/site/pos_build.py site` faz o pós-processamento: `lang="pt-BR"` (o `app.js` do Writerside já tem a interface em pt-BR e escolhe o idioma por esse atributo: "Nesta página", busca, "Editar página", "Última modificação"), data em português, remoção de analytics/rastreamento e do formulário de feedback, faixa "página ainda em inglês" nas páginas sem marcador e rodapé com a atribuição e link para a página equivalente em kotlinlang.org/docs.

O builder sai com código != 0 por causa da inspeção (imagens `_dark` faltando no upstream), mas gera o site; o script decide pelo zip. Em Mac arm64 a imagem roda emulada (amd64), ~4 min. `WRS_PULAR=1 tool/site/build.sh` refaz só o pós-processamento a partir de `.wrs-build/`. Servir local: `python3 -m http.server -d site 8000`.

Deploy: `.github/workflows/deploy-firebase.yml` roda `verificar.py`, o mesmo `build.sh` e publica no push para `master`.

## Convenções das páginas

- **Marcador de página traduzida:** a **última linha** do .md é `<!-- ia-translate: true -->`. O Writerside não renderiza comentários HTML. Sem marcador, a página recebe a faixa "ainda em inglês".
- `[//]: # (title: ...)`: traduza o texto do título; o formato da linha fica.
- Blocos de código, `<code-block>`, blocos de atributos `{...}`, tags XML do Writerside e seus atributos, URLs, variáveis `%nome%`, comentários HTML e código inline ficam idênticos. Atributos de texto visível (`title`, `collapsed-title`, `alt`, `caption`, `summary`, `label`) podem ser traduzidos.
- **Âncoras:** depois de traduzir, rode `python3 tool/traducao/ancorar_titulos.py <arquivos>`. Ele grava em cada título traduzido `{id="..."}` com o id que o Writerside geraria do título em inglês (regra em `tool/traducao/comum.py:slug`), ou repete o `{id}` explícito do original. Assim `pagina.html#ancora` não muda. Títulos que já têm `{...}` com outros atributos recebem o id no mesmo bloco.
- `python3 tool/traducao/verificar.py [arquivos]` confere cada página com marcador contra o inglês do commit em `ultimo-sync-upstream.txt` (via `git show`) e falha o deploy se houver ERRO. AVISO não bloqueia.

## Política de termos

Ficam em inglês: class, data class, object, companion object, extension function, lambda, coroutine, null safety, smart cast, sealed class, enum class, inline, receiver, scope function, Gradle, build (masculino), IDE, IntelliJ IDEA, Kotlin Multiplatform. "interface" e "app" ficam iguais. Evite "certifique-se", "você pode querer", "devolver" (return = retornar) e "suportar" (support). Títulos em sentence case.

## Sem rastreamento

O site traduzido não manda dados para a JetBrains: o pós-build remove o Google Tag Manager, o `analytics.js` da JetBrains, o widget "Was this page helpful?" (desligado também no `config.json`) e o Disqus, e falha se sobrar algum. Não reintroduza. Pendente: a busca usa o Algolia da JetBrains (índice em inglês do kotlinlang.org); o `app.js` e o CSS vêm do CDN `resources.jetbrains.com`.
