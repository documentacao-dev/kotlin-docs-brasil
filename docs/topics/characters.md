[//]: # (title: Caracteres)
<web-summary>Saiba como usar o tipo Char no Kotlin, incluindo sintaxe, suporte a Unicode, sequências de escape e operações comuns com caracteres.</web-summary>

O tipo [`Char`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char/) representa um único caractere como uma unidade de código UTF-16.

Use `Char` para valores de caractere individuais, como letras, dígitos,
sinais de pontuação ou espaços em branco. Para sequências de caracteres, use [`String`](strings.md).

> `Char` não é um tipo numérico, mas cada caractere tem um valor numérico Unicode que você pode acessar. 
> Veja [](#character-conversion).
> 
{style="tip"}

## Sintaxe {id="syntax"}

Para declarar um caractere, coloque o valor entre aspas simples (`' '`). Você pode especificar o tipo `Char` explicitamente ou
deixar que o Kotlin o infira a partir do valor:

```kotlin
val letter: Char = 'a'

// Kotlin infers Char because the values are written in single quotes
val digit = '1'
val symbol = '!'
val space = ' '
val separator = ':'
```

Um literal de caractere deve conter exatamente um caractere. Caso contrário, o compilador do Kotlin emite um erro:

```kotlin
val invalid = 'AB' // Error
val invalidEmpty = '' // Error
```
{validate="false"}

### Valores anuláveis {id="nullable-values"}

Para armazenar um valor anulável, use `Char?`:

```kotlin
val maybeAbsent: Char? = null
```

> No JVM, valores `Char` anuláveis passam por boxing quando necessário. O mesmo vale para
> [tipos numéricos](numbers.md#boxing-and-caching-numbers-on-the-jvm).
>
{style="note"}


## Suporte a Unicode {id="unicode-support"}

O Kotlin representa valores `Char` como unidades de código UTF-16. Isso significa que um único `Char` armazena uma unidade de código UTF-16,
e não necessariamente um caractere Unicode completo.

### Plano multilíngue básico {id="basic-multilingual-plane"}

Um único `Char` pode armazenar valores no intervalo de `\u0000` a `\uFFFF`.
Esse intervalo cobre o Plano Multilíngue Básico (BMP), que inclui caracteres de quase todas as línguas modernas e um grande número de símbolos.

Para especificar um caractere pelo valor Unicode, use
`\u` seguido de um valor hexadecimal de quatro dígitos da [tabela Unicode](https://www.unicode.org/charts/):

```kotlin
val unicodeNumber = '\u0031' // Equals '1'
```

### Caracteres suplementares {id="supplementary-characters"}

Caracteres Unicode fora do BMP, como emojis e alguns sistemas de escrita históricos,
não podem ser representados por um único `Char`. Em UTF-16, eles são codificados como um _par substituto_ (surrogate pair),
em que dois valores `Char` juntos representam um caractere Unicode em uma `String`:

```kotlin
fun main() {
//sampleStart
    val emoji = "🥦"
    
    println(emoji.length) // 2
    println(emoji[0])     // First surrogate
    println(emoji[1])     // Second surrogate
//sampleEnd
}
```

> Para tratar símbolos de 32 bits individualmente, use pontos de código Unicode armazenados como valores `Int`.
>
{style="tip"}


## Sequências de escape {id="escape-sequences"}

Use sequências de escape para caracteres especiais que são difíceis de escrever diretamente no código-fonte ou que têm um
significado especial.

Toda sequência de escape começa com uma barra invertida (`\`).

| **Sequência aceita**   | **Descrição**         | 
|------------------------|-----------------------|
| `\t`                   | Tabulação             | 
| `\b`                   | Backspace             | 
| `\n`                   | Nova linha (LF)       | 
| `\r`                   | Retorno de carro (CR) | 
| `\'`                   | Aspas simples         | 
| `\"`                   | Aspas duplas          |
| `\\`                   | Barra invertida       | 
| `\$`                   | Cifrão                | 


Por exemplo:

```kotlin
val newLine = '\n'
val dollar = '\$'
val backslash = '\\'
```

## Operações {id="operations"}

`Char` oferece comparação, inspeção, conversão de maiúsculas e minúsculas e conversão numérica explícita.

### Comparação de caracteres {id="character-comparison"}

Para comparar valores `Char`, use os [operadores de comparação](keyword-reference.md#operators-and-special-symbols) padrão,
como `==`, `!=`, `<`, `>`, `<=` e `>=`.

O Kotlin compara valores `Char` por seus valores numéricos Unicode e retorna
um valor `Boolean`:

```kotlin
val before = 'a' < 'b' // true
val after = 'c' > 'd' // false
val different = 'A' == 'a' // false 
val equal = 'A' == 'A' // true
```

### Processamento de caracteres {id="character-processing"}

O Kotlin oferece funções para inspeção e conversão de maiúsculas e minúsculas de valores de caractere.
Por exemplo:

```kotlin
fun main() {
//sampleStart
    val myChar = 'A'
    // Checks if the character represents a digit
    println(myChar.isDigit()) // false
    // Checks if the character represents an uppercase letter
    println(myChar.isUpperCase()) // true
    // Returns a lowercase version
    println(myChar.lowercaseChar()) // 'a'
//sampleEnd
}
```
{kotlin-runnable="true"}

> Saiba mais sobre as funções disponíveis na
> [Referência da API](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char/).
>
{style="note"}


### Aritmética de caracteres {id="character-arithmetic"}

Você pode criar outro valor de caractere somando ou subtraindo um inteiro:

```kotlin
fun main() {
//sampleStart
    val a = 'a'

    println(a + 1)  // b
    println(a + 2)  // c
    println(a - 32) // A
//sampleEnd
}
```
{kotlin-runnable="true"}

> Essas operações seguem os valores Unicode, e não as regras de alfabeto específicas de cada idioma.
>
{style="note"}

Você também pode usar os operadores de incremento (`++`) e decremento (`--`) nas formas prefixa e pós-fixa
com variáveis mutáveis:

```kotlin
fun main() {
//sampleStart
    var a = 'A'
    
    a += 10
    println(a)   // 'K'
    
    println(++a) // 'L'  prefix increment
    println(a++) // 'L'  postfix increment
    println(a)   // 'M'
    
    println(--a) // 'L'  prefix decrement
    println(a--) // 'L'  postfix decrement
    println(a)   // 'K'
//sampleEnd
}
```
{kotlin-runnable="true"}

### Conversão de caracteres {id="character-conversion"}

Para converter `Char` para um tipo numérico, use conversão explícita:

* Use `.code` para obter o valor numérico Unicode de um caractere:

  ```kotlin
  fun main() { 
  //sampleStart
      val letter = 'A'
      println(letter.code) // 65
  //sampleEnd
  }
  ```
  {kotlin-runnable="true"}

* Se um caractere representar um dígito decimal, use `digitToInt()`:
  ```kotlin
  fun main() { 
  //sampleStart
      val digit = '7'
      println(digit.digitToInt()) // 7
  //sampleEnd
  }
  ```
  {kotlin-runnable="true"}

  > Se o caractere puder não ser um dígito válido, use `digitToIntOrNull()`.
  >
  {style="tip"}

<!-- ia-translate: true -->
