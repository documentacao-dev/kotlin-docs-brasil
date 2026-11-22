[//]: # (title: Visão geral dos tipos)

No Kotlin, tudo é um objeto no sentido de que você pode chamar funções e propriedades de membro em qualquer variável.
Alguns tipos, como números, caracteres e booleanos, têm uma representação interna otimizada como valores primitivos em
tempo de execução, mas se comportam e aparecem como classes comuns no código Kotlin.

## Tipos básicos {id="basic-types"}

Esta seção descreve os tipos básicos usados no Kotlin:

| **Categoria**                                             | **Tipos básicos**                  | **Definição**                      |
|-----------------------------------------------------------|------------------------------------|------------------------------------|
| [Inteiros](numbers.md#integer-types)                      | `Byte`, `Short`, `Int`, `Long`     | Números inteiros                   |
| [Inteiros sem sinal](unsigned-integer-types.md)           | `UByte`, `UShort`, `UInt`, `ULong` | Números inteiros não negativos     |
| [Números de ponto flutuante](numbers.md#floating-point-types) | `Float`, `Double`                  | Números com parte fracionária      |
| [Booleanos](booleans.md)                                  | `Boolean`                          | Valores lógicos: `true` e `false`  |
| [Caracteres](characters.md)                               | `Char`                             | Um único caractere                 |
| [Strings](strings.md)                                     | `String`                           | Uma sequência de caracteres        |
| [Arrays](arrays.md)                                       | `Array<T>`, arrays de tipos primitivos | Uma sequência de valores de tamanho fixo |


> Por padrão, todo tipo é não nulável. Para permitir valores `null`, declare uma variável com o sinal `?` logo após o tipo
> da variável. Por exemplo, `String?`. Saiba mais em [Null safety](null-safety.md#nullable-types-and-non-nullable-types).
> 
{style="note"}

Para conhecer outros tipos do Kotlin, como `Nothing`, `Any` e `Unit`, consulte a referência da API do Kotlin:

* [`Any`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/) – A raiz da hierarquia de classes do Kotlin.
* [`Nothing`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-nothing.html) – Um tipo que não tem valores.
* [`Unit`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/) – Um tipo com apenas um valor (`Unit`). O compilador o infere como o tipo de retorno de funções com corpo em bloco
  e sem tipo de retorno explícito. Veja [Funções que retornam Unit](functions.md#unit-returning-functions).

## Tipos não denotáveis {id="non-denotable-types"}

O Kotlin também tem tipos não denotáveis. São tipos que você não consegue escrever diretamente no código Kotlin. Em vez disso, o
compilador os usa internamente, por exemplo, para interoperabilidade com outras linguagens. O Kotlin cria tipos não denotáveis
para representar informações de tipo mais precisas do que a sintaxe de código-fonte do Kotlin permite.

Mesmo que você não consiga declarar tipos não denotáveis, pode encontrá-los em diagnósticos do compilador, em
dicas de ferramentas da IDE ou nas exibições de tipos inferidos. Saiba mais sobre tipos não denotáveis em:

* [Tipos de plataforma](java-interop.md#null-safety-and-platform-types)
* [](typecasts.md#intersection-types)
* [](numbers.md#integer-literal-types)
* [](generics.md#captured-types)
* [Especificação da linguagem Kotlin: sistema de tipos](https://kotlinlang.org/spec/type-system.html)

> [Saiba como fazer verificações e conversões de tipo no Kotlin](typecasts.md).
>
{style="tip"}

<!-- ia-translate: true -->
