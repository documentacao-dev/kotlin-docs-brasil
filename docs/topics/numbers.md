[//]: # (title: Números)
<web-summary>Saiba como usar números no Kotlin, incluindo tipos numéricos, literais, conversões, operações aritméticas, estouro (overflow) e comportamento específico da JVM.</web-summary>

Os tipos numéricos do Kotlin representam:
* Valores inteiros ([Byte](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte/),
  [Short](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/),
  [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/),
  e [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/))
* Valores de ponto flutuante ([Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/)
  e [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/))

Use tipos numéricos para armazenar e processar dados numéricos, por exemplo, em aritmética, contadores, medições e outros cálculos.

## Escolha um tipo numérico {id="choose-a-number-type"}

Na maioria dos casos, você pode seguir as regras abaixo para determinar o tipo numérico correto para a tarefa:

* Use `Int` para números inteiros.
* Use `Long` para números inteiros fora do intervalo de `Int`.
* Use `Double` para números decimais.
* Use `Float` quando uma precisão menor for aceitável ou exigida.
* Use `Byte` e `Short` quando uma API ou um formato de dados exigir.

> O Kotlin também oferece [](unsigned-integer-types.md) como um recurso Beta. 
>
{style="tip"}

## Tipos inteiros {id="integer-types"}

O Kotlin oferece quatro tipos inteiros com tamanhos e intervalos de valores diferentes:

| Tipo     | Tamanho (bits) | Valor mínimo                                 | Valor máximo                                   |
|----------|----------------|----------------------------------------------|------------------------------------------------|
| `Byte`   | 8              | -128                                         | 127                                            |
| `Short`  | 16             | -32768                                       | 32767                                          |
| `Int`    | 32             | -2,147,483,648 (-2<sup>31</sup>)             | 2,147,483,647 (2<sup>31</sup> - 1)             |
| `Long`   | 64             | -9,223,372,036,854,775,808 (-2<sup>63</sup>) | 9,223,372,036,854,775,807 (2<sup>63</sup> - 1) |


### Declare valores inteiros {id="declare-integer-values"}

O Kotlin aceita as seguintes formas de literais para valores inteiros:

* Decimais: `123`
* Hexadecimais: `0x0F`
* Binários: `0b00001011`

> O Kotlin não aceita literais octais.
>
{style="note"}

Para declarar um valor numérico, especifique o tipo explicitamente: 

```kotlin
val one: Int = 1

// Use underscores to improve readability
val oneBillion: Long = 1_000_000_000
val hexBytes: Int = 0x7F_EC_DE_5E
val bytes: Int = 0b01010010_01101001_10010100_10010010

val oneByte: Byte = 1
val oneShort: Short = 1
```

Você também pode adicionar o sufixo `L` para declarar um valor `Long`:

```kotlin
val oneLong = 1L
```

Quando você declara um tipo numérico explicitamente, o compilador verifica se o valor cabe no intervalo desse tipo:

```kotlin
// Value fits in Byte
val oneByte: Byte = 1

// Error: the value does not fit in Byte
val tooBig: Byte = 128
```

Quando você não especifica um tipo numérico, o Kotlin infere `Int` se o valor couber no intervalo de `Int`. Caso contrário, o Kotlin infere `Long`:

```kotlin
val million = 1_000_000 // Int
val threeBillion = 3_000_000_000 // Long
```

Se um valor puder estar ausente, use tipos anuláveis:

```kotlin
val maybeAbsent: Int? = null
```

## Tipos de ponto flutuante {id="floating-point-types"}

Para números com parte fracionária, o Kotlin oferece `Float` e `Double`.

Os tipos de ponto flutuante seguem o [padrão IEEE 754](https://en.wikipedia.org/wiki/IEEE_754).
`Float` representa a _precisão simples_. `Double` representa a _precisão dupla_.

Os tipos de ponto flutuante diferem em tamanho e precisão:

| Tipo     | Tamanho (bits) | Bits significativos | Bits do expoente | Dígitos decimais |
|----------|----------------|---------------------|------------------|------------------|
| `Float`  | 32             | 24                  | 8                | 6-7              |
| `Double` | 64             | 53                  | 11               | 15-16            |    


### Declare valores de ponto flutuante {id="declare-floating-point-values"}

Para declarar um literal de ponto flutuante, inclua um ponto decimal (`.`) ou use notação exponencial:

```kotlin
val pi = 3.14
val avogadro = 6.02214076e23
```

Por padrão, o Kotlin infere literais de ponto flutuante como `Double`. 
Para declarar um `Float`, adicione o sufixo `f` ou `F`:

```kotlin
val pi = 3.14 // Double
val eFloat = 2.7182817f // Float
```

> O Kotlin arredonda um literal `Float` que contém mais precisão do que `Float` consegue armazenar.
>
{style="note"}

Se um valor puder estar ausente, use tipos anuláveis:

```kotlin
val maybeAbsent: Double? = null
```

## Operações aritméticas {id="arithmetic-operations"}

O Kotlin oferece as operações aritméticas padrão sobre números: `+`, `-`, `*`, `/` e `%`.

Use esses operadores para fazer cálculos comuns:

```kotlin
fun main() {
//sampleStart
    println(1 + 2) // 3
    println(2_500_000_000L - 1L) // 2499999999
    println(3.14 * 2.71) // 8.5094
    println(10.0 / 3) // 3.3333333333333335
//sampleEnd
}
```
{kotlin-runnable="true"}

O tipo do resultado depende dos tipos dos operandos. Saiba mais em [](#mixed-numeric-expressions).

> Você pode sobrescrever esses operadores em classes numéricas personalizadas.
> Para mais informações, consulte [Sobrecarga de operadores](operator-overloading.md).
>
{style="tip"}

### Divisão inteira {id="integer-division"}

A divisão entre valores inteiros sempre retorna um resultado inteiro. O compilador descarta a parte fracionária:

```kotlin
fun main() {
//sampleStart
    val intValue = 5 / 2
    println(intValue) // 2
    
    val longValue = 5L / 2
    println(longValue) // 2
//sampleEnd
}
```
{kotlin-runnable="true"}

Para retornar um resultado de ponto flutuante, faça pelo menos um dos operandos ser `Float` ou `Double`:

```kotlin
fun main() {
//sampleStart
    val a = 5 / 2.0
    println(a) // 2.5
    
    val b = 5 / 2.toDouble()
    println(b) // 2.5
//sampleEnd
}
```
{kotlin-runnable="true"}

## Conversão de tipos {id="type-conversion"}

Tipos numéricos não são subtipos uns dos outros. O Kotlin exige conversões explícitas para evitar perda silenciosa de dados e comportamentos inesperados.

Por exemplo, uma função que espera `Double` não aceita um valor `Int` ou `Float` sem conversão:

```kotlin
fun main() {
//sampleStart
    fun printDouble(x: Double) { 
        print(x) 
    }

    val x = 1.0
    val xInt = 1
    val xFloat = 1.0f
    val one: Double = 1 // Error: initializer type mismatch

    printDouble(x) // OK
    printDouble(xInt) // Error: argument type mismatch
    printDouble(xFloat) // Error: argument type mismatch
//sampleEnd
}
```
{kotlin-runnable="true" validate="false"}

Todos os tipos numéricos aceitam conversões para outros tipos numéricos.
Para converter um número para outro tipo, use uma função de conversão explícita:

* `toByte()`
* `toShort()`
* `toInt()`
* `toLong()`
* `toFloat()`
* `toDouble()`

Por exemplo, o código a seguir converte um valor `Int` para `Double`:

```kotlin
fun main() {
//sampleStart
    val intValue: Int = 1
    val doubleValue = intValue.toDouble()
    
    println(doubleValue) // 1.0
//sampleEnd
}
```
{kotlin-runnable="true"}

Quando você converte um valor de ponto flutuante para um tipo inteiro, o compilador descarta a parte fracionária:

```kotlin
fun main() {
//sampleStart
    val d: Double = 1.5
    val l: Long = d.toLong()
    
    println(l) // 1
//sampleEnd    
}
```
{kotlin-runnable="true"}

### Expressões numéricas mistas {id="mixed-numeric-expressions"}

O Kotlin não aceita conversão implícita em atribuições ou em argumentos de função. 
No entanto, você pode combinar tipos numéricos diferentes em expressões aritméticas. Nesses casos, 
o Kotlin determina o tipo do resultado com base nos tipos dos operandos, 
e os operadores aritméticos fazem a conversão automaticamente:

```kotlin
val intNumber: Int = 1
val longNumber: Long = 1000
val result = intNumber + longNumber // 1001, Long
```

Se você tentar atribuir o resultado a um tipo menor, o compilador reporta um erro:

```kotlin
val intNumber: Int = 1
val longNumber: Long = 1000
val result: Int = intNumber + longNumber 
// Error: Initializer type mismatch
```

### Tipos literais inteiros {id="integer-literal-types"}

Durante a inferência de tipos, o Kotlin trata literais inteiros sem sufixo como um tipo especial [Integer Literal Type (ILT)](https://kotlinlang.org/spec/type-system.html#integer-literal-types)
até que o contexto ao redor determine um tipo específico:

```kotlin
//sampleStart
fun List<Any>.log() {
    println(joinToString(" | ") { it::class.simpleName ?: "Unknown" })
}

fun main() {
    listOf(1, 2).log()
    // Int | Int
    
    listOf(1L, 2L).log()
    // Long | Long
    
    // Compiler interprets 1 as an ILT and resolves it to Long
    listOf(1, 2L).log()
    // Long | Long
    
    // .toInt() converts the literal to Int
    listOf(1.toInt(), 2L).log()
    // Int | Long
}
//sampleEnd
```
{kotlin-runnable="true"}

É especialmente fácil não notar essa diferença com valores `Int` e `Long`, porque eles têm a mesma representação em texto em tempo de execução. Para evitar isso, especifique o tipo esperado ou converta os valores explicitamente:

```kotlin
//sampleStart
fun List<Any>.log() {
    println(joinToString(" | ") { it::class.simpleName ?: "Unknown" })
}

fun main() {
    val longValues: List<Long> = listOf(1, 2L)
    longValues.log()
    // Long | Long

    val numberValues: List<Number> = listOf(1.toInt(), 2L)
    numberValues.log()
    // Int | Long
}
//sampleEnd
```
{kotlin-runnable="true"}

Você também pode usar um tipo explícito para detectar inferências de tipo não intencionais:

```kotlin
fun main() {
//sampleStart
    val intValues: List<Int> = listOf(1, 2L)
    // Error: initializer type mismatch
//sampleEnd
}
```
{kotlin-runnable="true" validate="false"}

> Saiba mais sobre [Tipos literais inteiros](https://kotlinlang.org/spec/type-system.html#integer-literal-types).
> 
{style="tip"}

## Estouro de dados {id="data-overflow"}

Tipos numéricos só conseguem representar valores dentro dos intervalos definidos.

Se o resultado de uma operação ficar fora desse intervalo, ocorre um estouro (overflow). Se você converter um valor para um tipo numérico menor, o valor convertido pode não preservar 
o valor numérico original.

Esse comportamento pode afetar o resultado do código mesmo quando o compilador o aceita.

### Estouro em operações {id="overflow-in-operations"}

Cada tipo inteiro só consegue armazenar valores dentro do seu intervalo definido. Quando o resultado de uma operação aritmética ultrapassa esse intervalo, ocorre _estouro de dados_:

```kotlin
fun main(){
//sampleStart
    val intNumber: Int = 2147483647
    // Max Int value is 2147483647
    println(intNumber + 1) // -2147483648
//sampleEnd    
}
```
{kotlin-runnable="true"}

Aqui, o resultado volta ao início do intervalo, porque o valor não cabe mais em `Int`.

> O compilador não gera erro automaticamente quando ocorre estouro de inteiros.
>
{style="note"}

### Estouro na negação {id="overflow-in-negation"}

O estouro também pode ocorrer na negação. 
Por exemplo, você não consegue representar o equivalente positivo de `Int.MIN_VALUE` como `Int`.

```kotlin
fun main(){
//sampleStart
    val min = Int.MIN_VALUE
    println(-min) // -2147483648
//sampleEnd    
}
```
{kotlin-runnable="true"}

### Conversões para tipos menores {id="narrowing-conversions"}

Quando você converte um valor para um tipo inteiro menor, 
o resultado pode não preservar o valor numérico original:

```kotlin
fun main() {
//sampleStart
    val large: Int = 130
    val narrowed: Byte = large.toByte()

    println(narrowed) // -126
//sampleEnd
}
```
{kotlin-runnable="true"}

No entanto, como os tipos de ponto flutuante seguem o
[padrão IEEE 754](https://en.wikipedia.org/wiki/IEEE_754), resultados muito grandes podem se tornar `Infinity`:

```kotlin
fun main() {
//sampleStart
    println(Double.MAX_VALUE * 2) // Infinity
//sampleEnd    
}
```
{kotlin-runnable="true"}

## Operações bit a bit {id="bitwise-operations"}

O Kotlin oferece _operações bit a bit_ para `Int` e `Long`. Essas operações são representadas por um conjunto de [funções infixas](functions.md#infix-notation) e por `inv()`.

```kotlin
fun main() {
//sampleStart
    val x = 1
    
    println(x shl 2) // 4
    println(x and 0x000FF000) // 0
//sampleEnd
}
```
{kotlin-runnable="true"}

As operações bit a bit incluem:

* `shl()` – deslocamento à esquerda com sinal
* `shr()` – deslocamento à direita com sinal
* `ushr()` – deslocamento à direita sem sinal
* `and()` – AND bit a bit
* `or()` – OR bit a bit
* `xor()` – XOR bit a bit
* `inv()` – inversão bit a bit

## Comparação de números de ponto flutuante {id="floating-point-number-comparison"}

No Kotlin, a comparação de ponto flutuante depende do tipo estático dos operandos.

Quando os operandos são conhecidos estaticamente como `Float` ou `Double`,
as operações sobre os números e o intervalo que eles formam seguem o [padrão IEEE 754 para aritmética de ponto flutuante](https://en.wikipedia.org/wiki/IEEE_754).

No entanto, em casos de uso genéricos (como `Any`, `Comparable<...>` ou `Collection<T>`), o comportamento muda para operandos que não são tipados estaticamente como números de ponto flutuante. Nesses casos, o Kotlin
usa as implementações de `equals()` e `compareTo()` de `Float` e `Double`. 

Como resultado:

* `NaN` é considerado igual a si mesmo
* `NaN` é considerado maior que qualquer outro elemento, incluindo `POSITIVE_INFINITY`
* `-0.0` é considerado menor que `0.0`

O exemplo a seguir mostra a diferença entre operandos tipados estaticamente como números de ponto flutuante e operandos usados por meio de tipos genéricos:

```kotlin
//sampleStart  
fun generalizedEquals(a: Any, b: Any): Boolean {
    return a == b
}

fun main() {
    // Operands statically typed as floating-point numbers
    println(Double.NaN == Double.NaN) // false
    println(0.0 == -0.0) // true

    // Operands used through a non-floating-point static type
    println(generalizedEquals(Double.NaN, Double.NaN)) // true
    println(generalizedEquals(0.0, -0.0)) // false
}
//sampleEnd  
```
{kotlin-runnable="true" id="kotlin-numbers-floating-comp"}

## Boxing e cache de números na JVM {id="boxing-and-caching-numbers-on-the-jvm"}

Na JVM, valores numéricos não anuláveis normalmente são armazenados com tipos primitivos, como `int`, `long` ou `double`.
No entanto, quando você usa [tipos genéricos](generics.md) ou tipos numéricos anuláveis como `Int?`, o valor passa por boxing e é representado como um objeto.

A JVM aplica uma [técnica de otimização de memória](https://docs.oracle.com/javase/specs/jls/se22/html/jls-5.html#jls-5.1.7)
para números pequenos, armazenando em cache as representações boxed. Como resultado,
números boxed com o mesmo valor podem ser [referencialmente iguais](equality.md#referential-equality).

Por exemplo, a JVM armazena em cache valores `Integer` boxed no intervalo de `-128` a `127`. Por isso, o código a seguir retorna `true`:

```kotlin
fun main() {
//sampleStart
    val score: Int = 100
    val savedScore: Int? = score
    val displayedScore: Int? = score
    
    println(savedScore === displayedScore) // true
//sampleEnd
}
```
{kotlin-runnable="true" validate="false"}

Para valores fora do intervalo em cache, os valores boxed são objetos separados. Nesse caso,
eles não são referencialmente iguais, mesmo que os valores sejam [estruturalmente iguais](equality.md#structural-equality).
Por esse motivo, use `==` para comparar valores numéricos:

```kotlin
fun main() {
//sampleStart
    val score: Int = 10000
    val savedScore: Int? = score
    val displayedScore: Int? = score

    println(savedScore === displayedScore) // false
    println(savedScore == displayedScore) // true
//sampleEnd
}
```
{kotlin-runnable="true" validate="false"}

<!-- ia-translate: true -->
