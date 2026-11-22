[//]: # (title: Tipos inteiros sem sinal)

Além dos [tipos inteiros](numbers.md#integer-types), o Kotlin fornece os seguintes tipos para números inteiros sem sinal:

| Tipo     | Tamanho (bits) | Valor mínimo | Valor máximo                                    |
|----------|----------------|--------------|-------------------------------------------------|
| `UByte`  | 8              | 0            | 255                                             |
| `UShort` | 16             | 0            | 65.535                                          |
| `UInt`   | 32             | 0            | 4.294.967.295 (2<sup>32</sup> - 1)              |
| `ULong`  | 64             | 0            | 18.446.744.073.709.551.615 (2<sup>64</sup> - 1) |


Os tipos sem sinal oferecem suporte à maior parte das operações dos seus equivalentes com sinal.

> Números sem sinal são implementados como [inline classes](inline-classes.md) com uma única propriedade de armazenamento que contém o tipo com sinal correspondente de mesma largura. Se você quiser converter entre tipos inteiros com e sem sinal,
> garanta que seu código seja atualizado para que chamadas de função e operações aceitem o novo tipo.
>
{style="note"}

## Arrays e intervalos sem sinal {id="unsigned-arrays-and-ranges"}

> Arrays sem sinal e as operações sobre eles estão em [Beta](components-stability.md). Eles podem mudar de forma incompatível a qualquer momento.
> É necessário fazer opt-in (veja os detalhes abaixo).
>
{style="warning"}

Assim como acontece com os primitivos, cada tipo sem sinal tem um tipo correspondente que representa arrays desse tipo:

* `UByteArray`: um array de bytes sem sinal.
* `UShortArray`: um array de shorts sem sinal.
* `UIntArray`: um array de ints sem sinal.
* `ULongArray`: um array de longs sem sinal.

Assim como nos arrays de inteiros com sinal, eles oferecem uma API semelhante à classe `Array`, sem o overhead de boxing.

Ao usar arrays sem sinal, você recebe um aviso indicando que este recurso ainda não é estável.
Para remover o aviso, faça opt-in com a anotação `@ExperimentalUnsignedTypes`.
Cabe a você decidir se os clientes precisam fazer opt-in explicitamente para usar a API, mas tenha em mente que
arrays sem sinal não são um recurso estável, então uma API que os utiliza pode quebrar com mudanças na linguagem.
[Saiba mais sobre os requisitos de opt-in](opt-in-requirements.md).

[Intervalos e progressões](ranges.md) estão disponíveis para `UInt` e `ULong` por meio das classes `UIntRange`, `UIntProgression`,
`ULongRange` e `ULongProgression`. Junto com os tipos inteiros sem sinal, essas classes são estáveis.

## Literais de inteiros sem sinal {id="unsigned-integers-literals"}

Para facilitar o uso de inteiros sem sinal, você pode acrescentar um sufixo a um literal inteiro
indicando um tipo sem sinal específico (de forma semelhante ao `F` para `Float` ou ao `L` para `Long`):

* As letras `u` e `U` indicam literais sem sinal sem especificar o tipo exato.
    Se nenhum tipo esperado for fornecido, o compilador usa `UInt` ou `ULong`, dependendo do tamanho do literal:

    ```kotlin
    val b: UByte = 1u  // UByte, expected type provided
    val s: UShort = 1u // UShort, expected type provided
    val l: ULong = 1u  // ULong, expected type provided
  
    val a1 = 42u // UInt: no expected type provided, constant fits in UInt
    val a2 = 0xFFFF_FFFF_FFFFu // ULong: no expected type provided, constant doesn't fit in UInt
    ```

* `uL` e `UL` especificam explicitamente que o literal deve ser um `ULong`:

    ```kotlin
    val a = 1UL // ULong, even though no expected type provided and the constant fits into UInt
    ```

## Casos de uso {id="use-cases"}

O principal caso de uso dos números sem sinal é aproveitar toda a faixa de bits de um inteiro para representar valores positivos.
Por exemplo, para representar constantes hexadecimais que não cabem em tipos com sinal, como uma cor no formato `AARRGGBB` de 32 bits:

```kotlin
data class Color(val representation: UInt)

val yellow = Color(0xFFCC00CCu)
```

Você pode usar números sem sinal para inicializar arrays de bytes sem precisar de casts explícitos com `toByte()` nos literais:

```kotlin
val byteOrderMarkUtf8 = ubyteArrayOf(0xEFu, 0xBBu, 0xBFu)
```

Outro caso de uso é a interoperabilidade com APIs nativas. O Kotlin permite representar declarações nativas que contêm
tipos sem sinal na assinatura. O mapeamento não substitui inteiros sem sinal por inteiros com sinal, preservando a semântica original.

### Não objetivos {id="non-goals"}

Embora inteiros sem sinal só possam representar números positivos e zero, não é objetivo usá-los onde o domínio da aplicação
exige inteiros não negativos. Por exemplo, como tipo de tamanho de coleção ou de valor de índice de coleção.

Há alguns motivos para isso:

* Usar inteiros com sinal ajuda a detectar estouros acidentais e a sinalizar condições de erro, como o [`List.lastIndex`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/last-index.html) valer -1 para uma lista vazia.
* Inteiros sem sinal não podem ser tratados como uma versão com faixa limitada dos inteiros com sinal, porque a faixa de valores deles não é um
  subconjunto da faixa dos inteiros com sinal. Nem inteiros com sinal nem sem sinal são subtipos um do outro.

<!-- ia-translate: true -->
