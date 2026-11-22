[//]: # (title: Idiomas)

Uma coleção de idiomas aleatórios e muito usados em Kotlin. Se você tem um idioma favorito, contribua enviando um pull request.

## Criar DTOs (POJOs/POCOs) {id="create-dtos-pojos-pocos"}

```kotlin
data class Customer(val name: String, val email: String)
```

fornece uma classe `Customer` com a seguinte funcionalidade:

* getters (e setters, no caso de `var`s) para todas as propriedades
* `equals()`
* `hashCode()`
* `toString()`
* `copy()`
* `component1()`, `component2()`, ..., para todas as propriedades (veja [Data classes](data-classes.md))

## Valores padrão para parâmetros de função {id="default-values-for-function-parameters"}

```kotlin
fun foo(a: Int = 0, b: String = "") { ... }
```

## Filtrar uma lista {id="filter-a-list"}

```kotlin
val positives = list.filter { x -> x > 0 }
```

Ou, alternativamente, uma forma ainda mais curta:

```kotlin
val positives = list.filter { it > 0 }
```

Saiba a diferença entre [filtragem em Java e em Kotlin](java-to-kotlin-collections-guide.md#filter-elements).

## Verificar a presença de um elemento em uma coleção {id="check-the-presence-of-an-element-in-a-collection"}

```kotlin
if ("john@example.com" in emailsList) { ... }

if ("jane@example.com" !in emailsList) { ... }
```

## Interpolação de strings {id="string-interpolation"}

```kotlin
println("Name $name")
```

Saiba a diferença entre [concatenação de strings em Java e em Kotlin](java-to-kotlin-idioms-strings.md#concatenate-strings).

## Ler a entrada padrão de forma segura {id="read-standard-input-safely"}

```kotlin
// Reads a string and returns null if the input can't be converted into an integer. For example: Hi there!
val wrongInt = readln().toIntOrNull()
println(wrongInt)
// null

// Reads a string that can be converted into an integer and returns an integer. For example: 13
val correctInt = readln().toIntOrNull()
println(correctInt)
// 13
```

Para mais informações, veja [Ler a entrada padrão.](read-standard-input.md)

## Verificações de instância {id="instance-checks"}

```kotlin
when (x) {
    is Foo -> ...
    is Bar -> ...
    else   -> ...
}
```

## Lista somente leitura {id="read-only-list"}

```kotlin
val list = listOf("a", "b", "c")
```
## Map somente leitura {id="read-only-map"}

```kotlin
val map = mapOf("a" to 1, "b" to 2, "c" to 3)
```

## Acessar uma entrada de map {id="access-a-map-entry"}

```kotlin
println(map["key"])
map["key"] = value
```

## Percorrer um map ou uma lista de pares {id="traverse-a-map-or-a-list-of-pairs"}

```kotlin
for ((k, v) in map) {
    println("$k -> $v")
}
```

`k` e `v` podem ser quaisquer nomes convenientes, como `name` e `age`.

## Iterar sobre um intervalo {id="iterate-over-a-range"}

```kotlin
for (i in 1..100) { ... }  // includes 100
for (i in 1..<100) { ... } // excludes 100
for (x in 2..10 step 2) { ... }
for (x in 10 downTo 1) { ... }
(1..10).forEach { ... }
```

## Propriedade lazy {id="lazy-property"}

```kotlin
val p: String by lazy { // the value is computed only on first access
    // compute the string
}
```

## Funções de extensão {id="extension-functions"}

```kotlin
fun String.spaceToCamelCase() { ... }

"Convert this to camelcase".spaceToCamelCase()
```

## Criar um singleton {id="create-a-singleton"}

```kotlin
object Resource {
    val name = "Name"
}
```

## Usar inline value classes para valores com segurança de tipo {id="use-inline-value-classes-for-type-safe-values"}

```kotlin
@JvmInline
value class EmployeeId(private val id: String)

@JvmInline
value class CustomerId(private val id: String)
```

Se você misturar `EmployeeId` e `CustomerId` por acidente, um erro de compilação será gerado.

> A anotação `@JvmInline` só é necessária para os backends da JVM.
>
{style="note"}

## Instanciar uma classe abstrata {id="instantiate-an-abstract-class"}

```kotlin
abstract class MyAbstractClass {
    abstract fun doSomething()
    abstract fun sleep()
}

fun main() {
    val myObject = object : MyAbstractClass() {
        override fun doSomething() {
            // ...
        }

        override fun sleep() { // ...
        }
    }
    myObject.doSomething()
}
```

## Atalho para if-not-null {id="if-not-null-shorthand"}

```kotlin
val files = File("Test").listFiles()

println(files?.size) // size is printed if files is not null
```

## Atalho para if-not-null-else {id="if-not-null-else-shorthand"}

```kotlin
val files = File("Test").listFiles()

// For simple fallback values:
println(files?.size ?: "empty") // if files is null, this prints "empty"

// To calculate a more complicated fallback value in a code block, use `run`
val filesSize = files?.size ?: run { 
    val someSize = getSomeSize()
    someSize * 2
}
println(filesSize)
```

## Executar uma expressão se for null {id="execute-an-expression-if-null"}

```kotlin
val values = ...
val email = values["email"] ?: throw IllegalStateException("Email is missing!")
```

## Obter o primeiro item de uma coleção que pode estar vazia {id="get-first-item-of-a-possibly-empty-collection"}

```kotlin
val emails = ... // might be empty
val mainEmail = emails.firstOrNull() ?: ""
```

Saiba a diferença entre [obter o primeiro item em Java e em Kotlin](java-to-kotlin-collections-guide.md#get-the-first-and-the-last-items-of-a-possibly-empty-collection).

## Executar se não for null {id="execute-if-not-null"}

```kotlin
val value = ...

value?.let {
    ... // execute this block if not null
}
```

## Mapear um valor nullable se não for null {id="map-nullable-value-if-not-null"}

```kotlin
val value = ...

val mapped = value?.let { transformValue(it) } ?: defaultValue 
// defaultValue is returned if the value or the transform result is null.
```

## Retornar a partir de uma instrução when {id="return-on-when-statement"}

```kotlin
fun transform(color: String): Int {
    return when (color) {
        "Red" -> 0
        "Green" -> 1
        "Blue" -> 2
        else -> throw IllegalArgumentException("Invalid color param value")
    }
}
```

## Expressão try-catch {id="try-catch-expression"}

```kotlin
fun test() {
    val result = try {
        count()
    } catch (e: ArithmeticException) {
        throw IllegalStateException(e)
    }

    // Working with result
}
```

## Expressão if {id="if-expression"}

```kotlin
val y = if (x == 1) {
    "one"
} else if (x == 2) {
    "two"
} else {
    "other"
}
```

## Uso no estilo builder de métodos que retornam Unit {id="builder-style-usage-of-methods-that-return-unit"}

```kotlin
fun arrayOfMinusOnes(size: Int): IntArray {
    return IntArray(size).apply { fill(-1) }
}
```

## Funções de expressão única {id="single-expression-functions"}

```kotlin
fun theAnswer() = 42
```

Isso é equivalente a

```kotlin
fun theAnswer(): Int {
    return 42
}
```

Isso pode ser combinado de forma eficaz com outros idiomas, resultando em código mais curto. Por exemplo, com a expressão `when`:

```kotlin
fun transform(color: String): Int = when (color) {
    "Red" -> 0
    "Green" -> 1
    "Blue" -> 2
    else -> throw IllegalArgumentException("Invalid color param value")
}
```

## Chamar vários métodos em uma instância de objeto (with) {id="call-multiple-methods-on-an-object-instance-with"}

```kotlin
class Turtle {
    fun penDown()
    fun penUp()
    fun turn(degrees: Double)
    fun forward(pixels: Double)
}

val myTurtle = Turtle()
with(myTurtle) { //draw a 100 pix square
    penDown()
    for (i in 1..4) {
        forward(100.0)
        turn(90.0)
    }
    penUp()
}
```

## Configurar propriedades de um objeto (apply) {id="configure-properties-of-an-object-apply"}

```kotlin
val myRectangle = Rectangle().apply {
    length = 4
    breadth = 5
    color = 0xFAFAFA
}
```

Isso é útil para configurar propriedades que não estão presentes no construtor do objeto.

## try-with-resources do Java 7 {id="java-7-s-try-with-resources"}

```kotlin
val stream = Files.newInputStream(Paths.get("/some/file.txt"))
stream.buffered().reader().use { reader ->
    println(reader.readText())
}
```

## Função genérica que precisa da informação de tipo genérico {id="generic-function-that-requires-the-generic-type-information"}

```kotlin
//  public final class Gson {
//     ...
//     public <T> T fromJson(JsonElement json, Class<T> classOfT) throws JsonSyntaxException {
//     ...

inline fun <reified T: Any> Gson.fromJson(json: JsonElement): T = this.fromJson(json, T::class.java)
```

## Trocar o valor de duas variáveis {id="swap-two-variables"}

```kotlin
var a = 1
var b = 2
a = b.also { b = a }
```

## Marcar código como incompleto (TODO) {id="mark-code-as-incomplete-todo"}

A biblioteca padrão do Kotlin tem uma função `TODO()` que sempre lança um `NotImplementedError`.
Seu tipo de retorno é `Nothing`, então ela pode ser usada independentemente do tipo esperado.
Também existe uma sobrecarga que aceita um parâmetro com o motivo:

```kotlin
fun calcTaxes(): BigDecimal = TODO("Waiting for feedback from accounting")
```

O plugin de Kotlin do IntelliJ IDEA entende a semântica de `TODO()` e adiciona automaticamente um marcador de código na janela de ferramentas TODO.

## Próximos passos {id="what-s-next"}

* Resolva [os desafios do Advent of Code](advent-of-code.md) usando o estilo idiomático do Kotlin.
* Saiba como realizar [tarefas típicas com strings em Java e Kotlin](java-to-kotlin-idioms-strings.md).
* Saiba como realizar [tarefas típicas com coleções em Java e Kotlin](java-to-kotlin-collections-guide.md).
* Saiba como [lidar com nullability em Java e Kotlin](java-to-kotlin-nullability-guide.md).

<!-- ia-translate: true -->
