[//]: # (title: Tipos básicos)

<no-index/>


Toda variável e estrutura de dados em Kotlin tem um tipo. Os tipos são importantes porque dizem ao compilador o que você pode fazer com essa variável ou estrutura de dados. Em outras palavras, quais funções e propriedades ela tem.

No capítulo anterior, o Kotlin conseguiu identificar, no exemplo anterior, que `customers` tem o tipo [`Int`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/).
A capacidade do Kotlin de **inferir** o tipo chama-se **inferência de tipos**. `customers` recebe um valor inteiro. A partir disso, o Kotlin infere que `customers` tem o tipo numérico `Int`. Como resultado, o compilador sabe que você pode realizar operações aritméticas com `customers`:

```kotlin
fun main() {
//sampleStart
    var customers = 10

    // Some customers leave the queue
    customers = 8

    customers = customers + 3 // Example of addition: 11
    customers += 7            // Example of addition: 18
    customers -= 3            // Example of subtraction: 15
    customers *= 2            // Example of multiplication: 30
    customers /= 3            // Example of division: 10

    println(customers) // 10
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-basic-types-arithmetic"}

> `+=`, `-=`, `*=`, `/=` e `%=` são operadores de atribuição compostos. Para mais informações, consulte [Atribuições compostas](operator-overloading.md#augmented-assignments).
> 
{style="tip"}

No total, o Kotlin tem os seguintes tipos básicos:

| **Categoria**                                             | **Tipos básicos**                  | **Exemplo de código**                                             |
|-----------------------------------------------------------|------------------------------------|-------------------------------------------------------------------|
| [Inteiros](numbers.md#integer-types)                      | `Byte`, `Short`, `Int`, `Long`     | `val year: Int = 2020`<br/> `val amount: Long = 350_000_000`      |
| [Inteiros sem sinal](unsigned-integer-types.md)           | `UByte`, `UShort`, `UInt`, `ULong` | `val score: UInt = 100u`                                          |
| [Números de ponto flutuante](numbers.md#floating-point-types) | `Float`, `Double`               | `val currentTemp: Float = 24.5f`<br/> `val price: Double = 19.99` |
| [Booleanos](booleans.md)                                  | `Boolean`                          | `val isEnabled: Boolean = true`                                   |
| [Caracteres](characters.md)                               | `Char`                             | `val separator: Char = ','`                                       |
| [Strings](strings.md)                                     | `String`                           | `val message: String = "Hello, world!"`                           |

Para mais informações sobre os tipos básicos e suas propriedades, consulte [Visão geral dos tipos](types-overview.md).

Com esse conhecimento, você pode declarar variáveis e inicializá-las depois. O Kotlin consegue lidar com isso desde que as variáveis sejam inicializadas antes da primeira leitura.

Para declarar uma variável sem inicializá-la, especifique o tipo dela com `:`. Por exemplo:

```kotlin
fun main() {
//sampleStart
    // Variable declared without initialization
    val d: Int
    // Variable initialized
    d = 3

    // Variable explicitly typed and initialized
    val e: String = "hello"

    // Variables can be read because they have been initialized
    println(d) // 3
    println(e) // hello
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-basic-types-initialization"}

Se você não inicializar uma variável antes de lê-la, verá um erro:

```kotlin
fun main() {
//sampleStart
    // Variable declared without initialization
    val d: Int
    
    // Triggers an error
    println(d)
    // Variable 'd' must be initialized
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-basic-types-no-initialization" validate="false"}

Agora que você sabe declarar tipos básicos, é hora de conhecer as [coleções](kotlin-tour-collections.md).

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true">
<def title="Declare tipos explícitos para variáveis" id="basic-types-exercise-1">

Declare explicitamente o tipo correto para cada variável:

```kotlin
fun main() {
    val a: Int = 1000 
    val b = "log message"
    val c = 3.14
    val d = 100_000_000_000_000
    val e = false
    val f = '\n'
}
```
{validate="false" kotlin-runnable="true" id="kotlin-tour-basic-types-exercise"}

```kotlin
fun main() {
    val a: Int = 1000
    val b: String = "log message"
    val c: Double = 3.14
    val d: Long = 100_000_000_000_000
    val e: Boolean = false
    val f: Char = '\n'
}
```
{initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-basic-types-solution"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-hello-world.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-collections.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->
