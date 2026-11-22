[//]: # (title: Visão geral da sintaxe básica)

Esta é uma coleção de elementos básicos da sintaxe, com exemplos. No fim de cada seção, você encontra um link para
uma descrição detalhada do tópico relacionado.

Você também pode aprender todos os fundamentos do Kotlin com a gratuita [trilha Kotlin Core](https://hyperskill.org/tracks?category=4&utm_source=jbkotlin_hs&utm_medium=referral&utm_campaign=kotlinlang-docs&utm_content=button_1&utm_term=22.03.23)
da JetBrains Academy.

## Definição de pacote e imports {id="package-definition-and-imports"}

A especificação do pacote deve ficar no topo do arquivo de código-fonte:

```kotlin
package my.demo

import kotlin.text.*

// ...
```

Não é obrigatório que diretórios e pacotes correspondam: os arquivos de código-fonte podem ficar em qualquer lugar do sistema de arquivos.

Veja [Pacotes](packages.md).

## Ponto de entrada do programa {id="program-entry-point"}

O ponto de entrada de uma aplicação Kotlin é a função `main`:

```kotlin
fun main() {
    println("Hello world!")
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-hello-world"}

Outra forma de `main` aceita um número variável de argumentos `String`: 

```kotlin
fun main(args: Array<String>) {
    println(args.contentToString())
}
```
{kotlin-runnable="true"}

## Imprimir na saída padrão {id="print-to-the-standard-output"}

`print` imprime o argumento na saída padrão:

```kotlin
fun main() {
//sampleStart
    print("Hello ")
    print("world!")
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-print"}

`println` imprime os argumentos e adiciona uma quebra de linha, para que o próximo conteúdo impresso apareça na linha seguinte:

```kotlin
fun main() {
//sampleStart
    println("Hello world!")
    println(42)
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-println"}

## Ler da entrada padrão {id="read-from-the-standard-input"}

A função `readln()` lê da entrada padrão. Ela lê a linha inteira que o usuário digita, como uma string.

Você pode usar as funções `println()`, `readln()` e `print()` juntas para exibir mensagens que solicitam 
e mostrar a entrada do usuário:

```kotlin
// Prints a message to request input
println("Enter any word: ")

// Reads and stores the user input. For example: Happiness
val yourWord = readln()

// Prints a message with the input
print("You entered the word: ")
print(yourWord)
// You entered the word: Happiness
```

Para mais informações, veja [Ler a entrada padrão](read-standard-input.md).

## Funções {id="functions"}

Uma função com dois parâmetros `Int` e tipo de retorno `Int`:

```kotlin
//sampleStart
fun sum(a: Int, b: Int): Int {
    return a + b
}
//sampleEnd

fun main() {
    print("sum of 3 and 5 is ")
    println(sum(3, 5))
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-return-int"}

O corpo de uma função pode ser uma expressão. O tipo de retorno é inferido:

```kotlin
//sampleStart
fun sum(a: Int, b: Int) = a + b
//sampleEnd

fun main() {
    println("sum of 19 and 23 is ${sum(19, 23)}")
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-function-expression"}

Uma função que não retorna um valor significativo:

```kotlin
//sampleStart
fun printSum(a: Int, b: Int): Unit {
    println("sum of $a and $b is ${a + b}")
}
//sampleEnd

fun main() {
    printSum(-1, 8)
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-return-unit"}

O tipo de retorno `Unit` pode ser omitido:

```kotlin
//sampleStart
fun printSum(a: Int, b: Int) {
    println("sum of $a and $b is ${a + b}")
}
//sampleEnd

fun main() {
    printSum(-1, 8)
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-function-omit-unit"}

Veja [Funções](functions.md).

## Variáveis {id="variables"}

No Kotlin, você declara uma variável começando com uma palavra-chave, `val` ou `var`, seguida do nome da variável.

Use a palavra-chave `val` para declarar variáveis que recebem um valor apenas uma vez. São variáveis locais imutáveis, somente leitura, que não podem receber outro valor
depois da inicialização: 

```kotlin
fun main() {
//sampleStart
    // Declares the variable x and initializes it with the value of 5
    val x: Int = 5
    // 5
//sampleEnd
    println(x)
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-val"}

Use a palavra-chave `var` para declarar variáveis que podem ser reatribuídas. São variáveis mutáveis, e você pode alterar seus valores depois da inicialização:

```kotlin
fun main() {
//sampleStart
    // Declares the variable x and initializes it with the value of 5
    var x: Int = 5
    // Reassigns a new value of 6 to the variable x
    x += 1
    // 6
//sampleEnd
    println(x)
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-var"}

O Kotlin oferece inferência de tipos e identifica automaticamente o tipo de dado de uma variável declarada. Ao declarar uma variável, você pode omitir o tipo depois do nome dela:

```kotlin
fun main() {
//sampleStart
    // Declares the variable x with the value of 5;`Int` type is inferred
    val x = 5
    // 5
//sampleEnd
    println(x)
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-inference"}

Você só pode usar variáveis depois de inicializá-las. Você pode inicializar uma variável no momento da declaração ou declará-la primeiro e inicializá-la depois. 
No segundo caso, você deve especificar o tipo de dado:

```kotlin
fun main() {
//sampleStart
    // Initializes the variable x at the moment of declaration; type is not required
    val x = 5
    // Declares the variable c without initialization; type is required
    val c: Int
    // Initializes the variable c after declaration 
    c = 3
    // 5 
    // 3
//sampleEnd
    println(x)
    println(c)
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-initialize"}

Você pode declarar variáveis no nível superior:

```kotlin
//sampleStart
val PI = 3.14
var x = 0

fun incrementX() {
    x += 1
}
// x = 0; PI = 3.14
// incrementX()
// x = 1; PI = 3.14
//sampleEnd

fun main() {
    println("x = $x; PI = $PI")
    incrementX()
    println("incrementX()")
    println("x = $x; PI = $PI")
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-variable-top-level"}

Para informações sobre como declarar propriedades, veja [Propriedades](properties.md).

## Criando classes e instâncias {id="creating-classes-and-instances"}

Para definir uma classe, use a palavra-chave `class`:
```kotlin
class Shape
```

As propriedades de uma classe podem ser listadas na declaração ou no corpo: 

```kotlin
class Rectangle(val height: Double, val length: Double) {
    val perimeter = (height + length) * 2 
}
```

O construtor padrão, com os parâmetros listados na declaração da classe, fica disponível automaticamente:

```kotlin
class Rectangle(val height: Double, val length: Double) {
    val perimeter = (height + length) * 2 
}
fun main() {
    val rectangle = Rectangle(5.0, 2.0)
    println("The perimeter is ${rectangle.perimeter}")
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-class-constructor"}

A herança entre classes é declarada com dois-pontos (`:`). As classes são `final` por padrão; para tornar uma classe herdável,
marque-a como `open`:

```kotlin
open class Shape

class Rectangle(val height: Double, val length: Double): Shape() {
    val perimeter = (height + length) * 2 
}
```

Para mais informações sobre construtores e herança, veja [Classes](classes.md) e [Objetos e instâncias](object-declarations.md).

## Comentários {id="comments"}

Como a maioria das linguagens modernas, o Kotlin oferece comentários de linha única (ou _fim de linha_) e de várias linhas (_bloco_):

```kotlin
// This is an end-of-line comment

/* This is a block comment
   on multiple lines. */
```

Comentários de bloco no Kotlin podem ser aninhados:

```kotlin
/* The comment starts here
/* contains a nested comment *​/  
and ends here. */
```

Veja [Documentando código Kotlin](kotlin-doc.md) para informações sobre a sintaxe dos comentários de documentação.

## Templates de string {id="string-templates"}

```kotlin
fun main() {
//sampleStart
    var a = 1
    // simple name in template:
    val s1 = "a is $a" 
    
    a = 2
    // arbitrary expression in template:
    val s2 = "${s1.replace("is", "was")}, but now is $a"
//sampleEnd
    println(s2)
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-string-templates"}

Veja [Templates de string](strings.md#string-templates) para mais detalhes.

## Expressões condicionais {id="conditional-expressions"}

```kotlin
//sampleStart
fun maxOf(a: Int, b: Int): Int {
    if (a > b) {
        return a
    } else {
        return b
    }
}
//sampleEnd

fun main() {
    println("max of 0 and 42 is ${maxOf(0, 42)}")
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-conditional-expressions"}

No Kotlin, `if` também pode ser usado como expressão:

```kotlin
//sampleStart
fun maxOf(a: Int, b: Int) = if (a > b) a else b
//sampleEnd

fun main() {
    println("max of 0 and 42 is ${maxOf(0, 42)}")
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-if-expression"}

Veja [Expressões `if`](control-flow.md#if-expression).

## Laço for {id="for-loop"}

```kotlin
fun main() {
//sampleStart
    val items = listOf("apple", "banana", "kiwifruit")
    for (item in items) {
        println(item)
    }
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-for-loop"}

ou:

```kotlin
fun main() {
//sampleStart
    val items = listOf("apple", "banana", "kiwifruit")
    for (index in items.indices) {
        println("item at $index is ${items[index]}")
    }
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-for-loop-indices"}

Veja [Laço for](control-flow.md#for-loops).

## Laço while {id="while-loop"}

```kotlin
fun main() {
//sampleStart
    val items = listOf("apple", "banana", "kiwifruit")
    var index = 0
    while (index < items.size) {
        println("item at $index is ${items[index]}")
        index++
    }
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-while-loop"}

Veja [Laço while](control-flow.md#while-loops).

## Expressão when {id="when-expression"}

```kotlin
//sampleStart
fun describe(obj: Any): String =
    when (obj) {
        1          -> "One"
        "Hello"    -> "Greeting"
        is Long    -> "Long"
        !is String -> "Not a string"
        else       -> "Unknown"
    }
//sampleEnd

fun main() {
    println(describe(1))
    println(describe("Hello"))
    println(describe(1000L))
    println(describe(2))
    println(describe("other"))
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-when-expression"}

Veja [Expressões e instruções when](control-flow.md#when-expressions-and-statements).

## Intervalos {id="ranges"}

Verifique se um número está dentro de um intervalo usando o operador `in`:

```kotlin
fun main() {
//sampleStart
    val x = 10
    val y = 9
    if (x in 1..y+1) {
        println("fits in range")
    }
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-range-in"}

Verifique se um número está fora do intervalo:

```kotlin
fun main() {
//sampleStart
    val list = listOf("a", "b", "c")
    
    if (-1 !in 0..list.lastIndex) {
        println("-1 is out of range")
    }
    if (list.size !in list.indices) {
        println("list size is out of valid list indices range, too")
    }
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-out-of-range"}

Itere sobre um intervalo:

```kotlin
fun main() {
//sampleStart
    for (x in 1..5) {
        print(x)
    }
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-iterate-range"}

Ou sobre uma progressão:

```kotlin
fun main() {
//sampleStart
    for (x in 1..10 step 2) {
        print(x)
    }
    println()
    for (x in 9 downTo 0 step 3) {
        print(x)
    }
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-iterate-progression"}

Veja [Intervalos e progressões](ranges.md).

## Coleções {id="collections"}

Itere sobre uma coleção:

```kotlin
fun main() {
    val items = listOf("apple", "banana", "kiwifruit")
//sampleStart
    for (item in items) {
        println(item)
    }
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-iterate-collection"}

Verifique se uma coleção contém um objeto usando o operador `in`:

```kotlin
fun main() {
    val items = setOf("apple", "banana", "kiwifruit")
//sampleStart
    when {
        "orange" in items -> println("juicy")
        "apple" in items -> println("apple is fine too")
    }
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-collection-in"}

Use [expressões lambda](lambdas.md) para filtrar e mapear coleções:

```kotlin
fun main() {
//sampleStart
    val fruits = listOf("banana", "avocado", "apple", "kiwifruit")
    fruits
      .filter { it.startsWith("a") }
      .sortedBy { it }
      .map { it.uppercase() }
      .forEach { println(it) }
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-collection-filter-map"}

Veja [Visão geral das coleções](collections-overview.md).

## Valores nuláveis e verificações de null {id="nullable-values-and-null-checks"}

Uma referência deve ser marcada explicitamente como nulável quando um valor `null` for possível. Nomes de tipos nuláveis terminam com `?`.
Por exemplo, `Int?`.

Retorne `null` se `str` não contiver um inteiro:

```kotlin
fun parseInt(str: String): Int? {
    return str.toIntOrNull()
}
```

Use uma função que retorna um valor nulável:

```kotlin
fun parseInt(str: String): Int? {
    return str.toIntOrNull()
}

//sampleStart
fun printProduct(arg1: String, arg2: String) {
    val x = parseInt(arg1)
    val y = parseInt(arg2)

    // Using `x * y` yields error because they may hold nulls.
    if (x != null && y != null) {
        // x and y are automatically cast to non-nullable after null check
        println(x * y)
    }
    else {
        println("'$arg1' or '$arg2' is not a number")
    }    
}
//sampleEnd

fun main() {
    printProduct("6", "7")
    printProduct("a", "7")
    printProduct("a", "b")
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-function-nullable-value"}

ou:

```kotlin
fun parseInt(str: String): Int? {
    return str.toIntOrNull()
}

fun printProduct(arg1: String, arg2: String) {
    val x = parseInt(arg1)
    val y = parseInt(arg2)
    
//sampleStart
    // ...
    if (x == null) {
        println("Wrong number format in arg1: '$arg1'")
        return
    }
    if (y == null) {
        println("Wrong number format in arg2: '$arg2'")
        return
    }

    // x and y are automatically cast to non-nullable after null check
    println(x * y)
//sampleEnd
}

fun main() {
    printProduct("6", "7")
    printProduct("a", "7")
    printProduct("99", "b")
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-function-null-check"}

Veja [Null safety](null-safety.md).

## Verificações de tipo e conversões automáticas {id="type-checks-and-automatic-casts"}

O operador `is` verifica se uma expressão é uma instância de um tipo.
Se uma variável local imutável ou uma propriedade for verificada quanto a um tipo específico, não é preciso fazer uma conversão explícita:

```kotlin
//sampleStart
fun getStringLength(obj: Any): Int? {
    if (obj is String) {
        // `obj` is automatically cast to `String` in this branch
        return obj.length
    }

    // `obj` is still of type `Any` outside of the type-checked branch
    return null
}
//sampleEnd

fun main() {
    fun printLength(obj: Any) {
        println("Getting the length of '$obj'. Result: ${getStringLength(obj) ?: "Error: The object is not a string"} ")
    }
    printLength("Incomprehensibilities")
    printLength(1000)
    printLength(listOf(Any()))
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-is-operator"}

ou:

```kotlin
//sampleStart
fun getStringLength(obj: Any): Int? {
    if (obj !is String) return null

    // `obj` is automatically cast to `String` in this branch
    return obj.length
}
//sampleEnd

fun main() {
    fun printLength(obj: Any) {
        println("Getting the length of '$obj'. Result: ${getStringLength(obj) ?: "Error: The object is not a string"} ")
    }
    printLength("Incomprehensibilities")
    printLength(1000)
    printLength(listOf(Any()))
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-is-operator-expression"}

ou até:

```kotlin
//sampleStart
fun getStringLength(obj: Any): Int? {
    // `obj` is automatically cast to `String` on the right-hand side of `&&`
    if (obj is String && obj.length >= 0) {
        return obj.length
    }

    return null
}
//sampleEnd

fun main() {
    fun printLength(obj: Any) {
        println("Getting the length of '$obj'. Result: ${getStringLength(obj) ?: "Error: The object is not a string"} ")
    }
    printLength("Incomprehensibilities")
    printLength("")
    printLength(1000)
}
```
{kotlin-runnable="true" id="kotlin-basic-syntax-is-operator-logic"}

Veja [Classes](classes.md) e [Conversões de tipo](typecasts.md).

<!-- ia-translate: true -->
