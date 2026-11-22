[//]: # (title: Booleanos)
<web-summary>Saiba como usar valores booleanos no Kotlin, incluindo declaração, operadores lógicos e condições.</web-summary>

<show-structure depth="1"/>

O tipo [`Boolean`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) representa
valores lógicos: `true` e `false`.

Use valores `Boolean` em funções que respondem perguntas de sim ou não, e nas
condições de `while`, `if` e `when`.


## Declare uma variável `Boolean` {id="declare-a-boolean-variable"}

Para declarar uma variável `Boolean`, atribua a ela `true` ou `false`.

Você pode especificar o tipo `Boolean` explicitamente ou deixar que o Kotlin o infira a partir do valor:

```kotlin
val isTrue: Boolean = true
val isFalse = false // Kotlin infers Boolean
```

Se um valor puder ser `null`, use `Boolean?`:

```kotlin
val isEnabled: Boolean? = null
```

> Você não pode atribuir um valor inteiro a uma variável `Boolean`.
> No Kotlin, `0` e `1` não são valores `Boolean`.
>
{style="note"}

## Produza valores `Boolean` {id="produce-boolean-values"}

Você pode usar expressões de comparação e funções para produzir valores `Boolean`:

```kotlin
fun main() {
//sampleStart
    val number = 10
    val isPositive = number > 0 
    println(isPositive) // true

    val language = "Kotlin"
    val isEmpty = language.isEmpty() 
    println(isEmpty) // false
//sampleEnd
}
```
{kotlin-runnable="true"}

Você também pode usar os resultados em condições e em outras expressões:

```kotlin
fun main() {
//sampleStart
    val number = 10
    val isPositive = number > 0 // true

    if (isPositive) {
        println("The number is positive.")
    }
//sampleEnd    
}
```
{kotlin-runnable="true"}

## Operações com `Boolean` {id="boolean-operations"}

O Kotlin oferece operadores e funções infixas para trabalhar com valores `Boolean`.
Você pode usá-los para inverter um valor `Boolean` ou combinar vários valores `Boolean` em um único resultado.

### Negação (NOT) {id="negation-not"}

O operador NOT inverte um valor `Boolean`.

Para usar NOT, coloque o operador `!` antes de um valor `Boolean`:


```kotlin
val isOn = true
val isOff = !isOn // isOff is false
```

### AND lógico {id="logical-and"}

O operador AND retorna `true` somente se os dois operandos forem `true`.

Para usar AND lógico, coloque o operador `&&` entre os operandos:

```kotlin
val a = false && false // false
val b = false && true // false
val c = true && false // false
val d = true && true  // true
```

> Se o primeiro operando for `false`, o operador `&&` ignora o segundo operando.
> Para avaliar os dois operandos, use, em vez disso, a [função infixa](functions.md#infix-notation) `and`.
>
{style="note"}

### OR lógico {id="logical-or"}

O operador OR retorna `true` se pelo menos um dos operandos for `true`.

Para usar OR lógico, coloque o operador `||` entre os operandos:

```kotlin
val a = false || false // false
val b = false || true  // true
val c = true || false  // true
val d = true || true   // true
```

> Se o primeiro operando for `true`, o operador `||` ignora o segundo operando.
> Para avaliar os dois operandos, use, em vez disso, a [função infixa](functions.md#infix-notation) `or`.
>
{style="note"}

### OR exclusivo (XOR) {id="exclusive-or-xor"}

A operação OR exclusivo (XOR) retorna `true` se os operandos tiverem valores diferentes.

Para usar XOR, escreva `xor` entre os operandos:

```kotlin
val a = false xor false // false
val b = false xor true  // true
val c = true xor false  // true
val d = true xor true   // false
```

> `xor` é uma [função infixa](functions.md#infix-notation), não um operador.
>
> Saiba mais sobre funções de `Boolean` na [Referência da API](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/).
>
{style="note"}

## Precedência de operadores {id="operator-precedence"}

Se uma expressão contiver várias operações lógicas e não tiver parênteses para especificar a ordem de avaliação,
o Kotlin aplica as regras de precedência. Operações com precedência maior são avaliadas antes de
operações com precedência menor.

Para as operações `Boolean` descritas nesta seção, a ordem de precedência é a seguinte:

1. `!`
2. `xor` (e outras funções infixas)
3. `&&`
4. `||`

No exemplo a seguir, o compilador avalia `&&` antes de `||`:

```kotlin
fun main() {
//sampleStart
    val result = true || false && false
    println(result) // true
//sampleEnd    
}
```
{kotlin-runnable="true" validate="false"}

Para deixar a ordem de avaliação explícita, use parênteses:

```kotlin
fun main() {
//sampleStart
    val result = (true || false) && false
    println(result) // false
//sampleEnd    
}
```
{kotlin-runnable="true" validate="false"}


## `Boolean` em condições {id="boolean-in-conditions"}

[`if`](control-flow.md#if-expression), [`when`](control-flow.md#when-expressions-and-statements)
e [`while`](control-flow.md#while-loops) avaliam expressões `Boolean` para direcionar o fluxo do programa.

### Expressões `if` {id="if-expressions"}

```kotlin
fun main() {
//sampleStart
    val number = 4
    val isEven = number % 2 == 0

    // Condition already has the `Boolean` type
    // You do not need to compare it to `true` or `false`
    if (isEven) { 
        println("The number is even.")
    } else {
        println("The number is odd.")
    }
//sampleEnd    
}
```
{kotlin-runnable="true"}


### Expressões `when` {id="when-expressions"}

```kotlin
fun main() {
//sampleStart
    val number = 3

    when {
        number > 0 -> println("The number is positive.")
        number < 0 -> println("The number is negative.")
        else -> println("The number is zero.")
    }
//sampleEnd    
}
```
{kotlin-runnable="true"}

### Laços `while` {id="while-loops"}

```kotlin
fun main() {
//sampleStart
    var isCalculating = true
    
    while (isCalculating) {
        println("Calculating...")
        isCalculating = false
    }
//sampleEnd    
}
```
{kotlin-runnable="true"}

<!-- ia-translate: true -->
