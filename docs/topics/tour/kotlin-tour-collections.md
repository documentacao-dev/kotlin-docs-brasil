[//]: # (title: Coleções)

<no-index/>


Ao programar, é útil poder agrupar dados em estruturas para processá-los depois. O Kotlin oferece coleções exatamente para isso.

O Kotlin tem as seguintes coleções para agrupar itens:

| **Tipo de coleção** | **Descrição**                                                                 |
|---------------------|-------------------------------------------------------------------------------|
| Listas              | Coleções ordenadas de itens                                                   |
| Conjuntos           | Coleções não ordenadas de itens únicos                                        |
| Mapas               | Conjuntos de pares chave-valor em que as chaves são únicas e apontam para um único valor |

Cada tipo de coleção pode ser mutável ou somente leitura.

## Lista {id="list"}

Listas armazenam os itens na ordem em que são adicionados e permitem itens duplicados. 

Para criar uma lista somente leitura ([`List`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/)), use a função
[`listOf()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/list-of.html).

Para criar uma lista mutável ([`MutableList`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list.html)),
use a função [`mutableListOf()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/mutable-list-of.html).

Ao criar listas, o Kotlin consegue inferir o tipo dos itens armazenados. Para declarar o tipo explicitamente, coloque o tipo
entre colchetes angulares `<>` após a declaração da lista:

```kotlin
fun main() { 
//sampleStart
    // Read only list
    val readOnlyShapes = listOf("triangle", "square", "circle")
    println(readOnlyShapes)
    // [triangle, square, circle]
    
    // Mutable list with explicit type declaration
    val shapes: MutableList<String> = mutableListOf("triangle", "square", "circle")
    println(shapes)
    // [triangle, square, circle]
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-lists-declaration"}

> Para evitar modificações indesejadas, você pode criar uma visão somente leitura de uma lista mutável atribuindo-a a um `List`:
> 
> ```kotlin
>     val shapes: MutableList<String> = mutableListOf("triangle", "square", "circle")
>     val shapesLocked: List<String> = shapes
> ```
> Isso também é chamado de **casting**.
> 
{style="tip"}

Listas são ordenadas, então, para acessar um item em uma lista, use o [operador de acesso indexado](operator-overloading.md#indexed-access-operator) `[]`:

```kotlin
fun main() { 
//sampleStart
    val readOnlyShapes = listOf("triangle", "square", "circle")
    println("The first item in the list is: ${readOnlyShapes[0]}")
    // The first item in the list is: triangle
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-list-access"}

Para obter o primeiro ou o último item de uma lista, use respectivamente as funções [`.first()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/first.html)
e [`.last()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/last.html):

```kotlin
fun main() { 
//sampleStart
    val readOnlyShapes = listOf("triangle", "square", "circle")
    println("The first item in the list is: ${readOnlyShapes.first()}")
    // The first item in the list is: triangle
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-list-first"}

> As funções [`.first()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/first.html) e [`.last()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/last.html)
> são exemplos de funções de **extensão**. Para chamar uma função de extensão em um objeto, escreva o nome da função
> depois do objeto, separado por um ponto `.` 
> 
> As funções de extensão são detalhadas [no tour intermediário](kotlin-tour-intermediate-extension-functions.md#extension-functions).
> Por enquanto, você só precisa saber como chamá-las. 
> 
{style="note"}

Para obter o número de itens de uma lista, use a função [`.count()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/count.html):

```kotlin
fun main() { 
//sampleStart
    val readOnlyShapes = listOf("triangle", "square", "circle")
    println("This list has ${readOnlyShapes.count()} items")
    // This list has 3 items
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-list-count"}

Para verificar se um item está em uma lista, use o [operador `in`](operator-overloading.md#in-operator):

```kotlin
fun main() {
//sampleStart
    val readOnlyShapes = listOf("triangle", "square", "circle")
    println("circle" in readOnlyShapes)
    // true
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-list-in"}

Para adicionar ou remover itens de uma lista mutável, use respectivamente as funções [`.add()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/add.html)
e [`.remove()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/remove.html):

```kotlin
fun main() { 
//sampleStart
    val shapes: MutableList<String> = mutableListOf("triangle", "square", "circle")
    // Add "pentagon" to the list
    shapes.add("pentagon") 
    println(shapes)  
    // [triangle, square, circle, pentagon]

    // Remove the first "pentagon" from the list
    shapes.remove("pentagon") 
    println(shapes)  
    // [triangle, square, circle]
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-list-add-remove"}

## Conjunto {id="set"}

Enquanto listas são ordenadas e permitem itens duplicados, conjuntos são **não ordenados** e armazenam apenas itens **únicos**.

Para criar um conjunto somente leitura ([`Set`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/)), use a função
[`setOf()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/set-of.html).

Para criar um conjunto mutável ([`MutableSet`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/)),
use a função [`mutableSetOf()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/mutable-set-of.html).

Ao criar conjuntos, o Kotlin consegue inferir o tipo dos itens armazenados. Para declarar o tipo explicitamente, coloque o tipo
entre colchetes angulares `<>` após a declaração do conjunto:

```kotlin
fun main() {
//sampleStart
    // Read-only set
    val readOnlyFruit = setOf("apple", "banana", "cherry", "cherry")
    // Mutable set with explicit type declaration
    val fruit: MutableSet<String> = mutableSetOf("apple", "banana", "cherry", "cherry")
    
    println(readOnlyFruit)
    // [apple, banana, cherry]
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-sets-declaration"}

Você viu no exemplo anterior que, como conjuntos só contêm elementos únicos, o item duplicado `"cherry"` é descartado.

> Para evitar modificações indesejadas, você pode criar uma visão somente leitura de um conjunto mutável atribuindo-o a um `Set`:
> 
> ```kotlin
>     val fruit: MutableSet<String> = mutableSetOf("apple", "banana", "cherry", "cherry")
>     val fruitLocked: Set<String> = fruit
> ```
>
{style="tip"}

> Como conjuntos são **não ordenados**, você não pode acessar um item em um índice específico.
> 
{style="note"}

Para obter o número de itens de um conjunto, use a função [`.count()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/count.html):

```kotlin
fun main() { 
//sampleStart
    val readOnlyFruit = setOf("apple", "banana", "cherry", "cherry")
    println("This set has ${readOnlyFruit.count()} items")
    // This set has 3 items
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-set-count"}

Para verificar se um item está em um conjunto, use o [operador `in`](operator-overloading.md#in-operator):

```kotlin
fun main() {
//sampleStart
    val readOnlyFruit = setOf("apple", "banana", "cherry", "cherry")
    println("banana" in readOnlyFruit)
    // true
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-set-in"}

Para adicionar ou remover itens de um conjunto mutável, use respectivamente as funções [`.add()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/add.html)
e [`.remove()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/remove.html):

```kotlin
fun main() { 
//sampleStart
    val fruit: MutableSet<String> = mutableSetOf("apple", "banana", "cherry", "cherry")
    fruit.add("dragonfruit")    // Add "dragonfruit" to the set
    println(fruit)              // [apple, banana, cherry, dragonfruit]
    
    fruit.remove("dragonfruit") // Remove "dragonfruit" from the set
    println(fruit)              // [apple, banana, cherry]
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-set-add-remove"}

## Mapa {id="map"}

Mapas armazenam itens como pares chave-valor. Você acessa o valor referenciando a chave. Pense em um mapa como um cardápio.
Você descobre o preço (valor) procurando pelo prato (chave) que quer pedir. Mapas são úteis quando você quer buscar um valor
sem usar um índice numerado, como em uma lista.

> * Toda chave em um mapa precisa ser única, para que o Kotlin entenda qual valor você quer obter. 
> * Você pode ter valores duplicados em um mapa.
>
{style="note"}

Para criar um mapa somente leitura ([`Map`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/)), use a função
[`mapOf()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/map-of.html).

Para criar um mapa mutável ([`MutableMap`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/)),
use a função [`mutableMapOf()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/mutable-map-of.html).

Ao criar mapas, o Kotlin consegue inferir o tipo dos itens armazenados. Para declarar o tipo explicitamente, coloque os tipos
das chaves e dos valores entre colchetes angulares `<>` após a declaração do mapa. Por exemplo: `MutableMap<String, Int>`.
As chaves têm o tipo `String` e os valores têm o tipo `Int`.

A forma mais fácil de criar mapas é usar [`to`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/to.html) entre cada
chave e o valor relacionado:

```kotlin
fun main() {
//sampleStart
    // Read-only map
    val readOnlyJuiceMenu = mapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
    println(readOnlyJuiceMenu)
    // {apple=100, kiwi=190, orange=100}

    // Mutable map with explicit type declaration
    val juiceMenu: MutableMap<String, Int> = mutableMapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
    println(juiceMenu)
    // {apple=100, kiwi=190, orange=100}
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-maps-declaration"}

> Para evitar modificações indesejadas, você pode criar uma visão somente leitura de um mapa mutável atribuindo-o a um `Map`:
> 
> ```kotlin
>     val juiceMenu: MutableMap<String, Int> = mutableMapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
>     val juiceMenuLocked: Map<String, Int> = juiceMenu
> ```
>
{style="tip"}

Para acessar um valor em um mapa, use o [operador de acesso indexado](operator-overloading.md#indexed-access-operator) `[]` com
a chave:

```kotlin
fun main() {
//sampleStart
    // Read-only map
    val readOnlyJuiceMenu = mapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
    println("The value of apple juice is: ${readOnlyJuiceMenu["apple"]}")
    // The value of apple juice is: 100
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-map-access"}

> Se você tentar acessar um par chave-valor com uma chave que não existe no mapa, verá um valor `null`:
>
> ```kotlin
> fun main() {
> //sampleStart
>     // Read-only map
>     val readOnlyJuiceMenu = mapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
>     println("The value of pineapple juice is: ${readOnlyJuiceMenu["pineapple"]}")
>     // The value of pineapple juice is: null
> //sampleEnd
> }
> ```
> {kotlin-runnable="true" id="kotlin-tour-map-no-key" validate="false"}
> 
> Este tour explica valores null mais adiante, no capítulo [Null safety](kotlin-tour-null-safety.md).
> 
{style="note"}

Você também pode usar o [operador de acesso indexado](operator-overloading.md#indexed-access-operator) `[]` para adicionar itens a um mapa mutável:

```kotlin
fun main() {
//sampleStart
    val juiceMenu: MutableMap<String, Int> = mutableMapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
    juiceMenu["coconut"] = 150 // Add key "coconut" with value 150 to the map
    println(juiceMenu)
    // {apple=100, kiwi=190, orange=100, coconut=150}
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-map-add-item"}

Para remover itens de um mapa mutável, use a função [`.remove()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/remove.html):

```kotlin
fun main() {
//sampleStart
    val juiceMenu: MutableMap<String, Int> = mutableMapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
    juiceMenu.remove("orange")    // Remove key "orange" from the map
    println(juiceMenu)
    // {apple=100, kiwi=190}
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-map-put-remove"}

Para obter o número de itens de um mapa, use a função [`.count()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/count.html):

```kotlin
fun main() {
//sampleStart
    // Read-only map
    val readOnlyJuiceMenu = mapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
    println("This map has ${readOnlyJuiceMenu.count()} key-value pairs")
    // This map has 3 key-value pairs
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-map-count"}

Para verificar se uma chave específica já está incluída em um mapa, use a função [`.containsKey()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/contains-key.html):

```kotlin
fun main() {
//sampleStart
    val readOnlyJuiceMenu = mapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
    println(readOnlyJuiceMenu.containsKey("kiwi"))
    // true
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-map-contains-keys"}

Para obter uma coleção das chaves ou dos valores de um mapa, use respectivamente as propriedades [`keys`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/keys.html)
e [`values`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/values.html):

```kotlin
fun main() {
//sampleStart
    val readOnlyJuiceMenu = mapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
    println(readOnlyJuiceMenu.keys)
    // [apple, kiwi, orange]
    println(readOnlyJuiceMenu.values)
    // [100, 190, 100]
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-map-keys-values"}

> [`keys`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/keys.html) e [`values`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/values.html)
> são exemplos de **propriedades** de um objeto. Para acessar a propriedade de um objeto, escreva o nome da propriedade
> depois do objeto, separado por um ponto `.`
>
> As propriedades são discutidas com mais detalhes no capítulo [Classes](kotlin-tour-classes.md).
> Neste ponto do tour, você só precisa saber como acessá-las.
>
{style="note"}

Para verificar se uma chave ou um valor está em um mapa, use o [operador `in`](operator-overloading.md#in-operator):

```kotlin
fun main() {
//sampleStart
    val readOnlyJuiceMenu = mapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
    println("orange" in readOnlyJuiceMenu.keys)
    // true
    
    // Alternatively, you don't need to use the keys property
    println("orange" in readOnlyJuiceMenu)
    // true
    
    println(200 in readOnlyJuiceMenu.values)
    // false
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-map-in"}

Para mais informações sobre o que você pode fazer com coleções, veja [Coleções](collections-overview.md).

Agora que você conhece os tipos básicos e sabe gerenciar coleções, é hora de explorar o [controle de fluxo](kotlin-tour-control-flow.md)
que você pode usar nos programas que você escrever.

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Contar o número total de itens em duas listas" id="collections-exercise-1">

Você tem uma lista de números “verdes” e uma lista de números “vermelhos”. Complete o código para imprimir quantos números
há no total.

```kotlin
// Keep these two lists as they are. Use them in main().
val greenNumbers = listOf(1, 4, 23)
val redNumbers = listOf(17, 2)

fun main() {
    // Write your code here
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/CollectionsExercise1Test.kt" validate="false" id="kotlin-tour-collections-exercise-1"}

```kotlin
val greenNumbers = listOf(1, 4, 23)
val redNumbers = listOf(17, 2)

fun main() {
    val totalCount = greenNumbers.count() + redNumbers.count()
    println(totalCount)
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/CollectionsExercise1Test.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-collections-solution-1"}

</def>
<def title="Verificar se um protocolo solicitado é aceito" id="collections-exercise-2">

Você tem um conjunto de protocolos aceitos pelo servidor. Um usuário pede para usar um protocolo específico. Complete o programa
para verificar se o protocolo solicitado é aceito ou não (`isSupported` precisa ser um valor booleano).

```kotlin
fun main() {
    val SUPPORTED = setOf("HTTP", "HTTPS", "FTP")
    val requested = "smtp"
    val isSupported = TODO() // Replace the TODO() function
    println("Support for $requested: $isSupported")
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/CollectionsExercise2Test.kt" validate="false" id="kotlin-tour-collections-exercise-2"}

<deflist collapsible="true" id="kotlin-tour-collections-exercise-2-hint">
    <def title="Dica">
        Confira o protocolo solicitado em letras maiúsculas. Você pode usar a função <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/uppercase.html"><code>.uppercase()</code></a> para isso.
    </def>
</deflist>

```kotlin
fun main() {
    val SUPPORTED = setOf("HTTP", "HTTPS", "FTP")
    val requested = "smtp"
    val isSupported = requested.uppercase() in SUPPORTED
    println("Support for $requested: $isSupported")
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/CollectionsExercise2Test.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-collections-solution-2"}

</def>
<def title="Escrever um número por extenso usando um mapa" id="collections-exercise-3">

Defina um mapa que relacione os números inteiros de 1 a 3 com a escrita por extenso deles. Use esse mapa para escrever por
extenso o número dado.

```kotlin
// Replace the empty map. Keep the variable name as number2word.
val number2word: Map<Int, String> = emptyMap()

fun main() {
    val n = 2
    println("$n is spelled as '${number2word[n]}'")
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/CollectionsExercise3Test.kt" validate="false" id="kotlin-tour-collections-exercise-3"}

```kotlin
val number2word = mapOf(1 to "one", 2 to "two", 3 to "three")

fun main() {
    val n = 2
    println("$n is spelled as '${number2word[n]}'")
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/CollectionsExercise3Test.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-collections-solution-3"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-basic-types.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-control-flow.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->
