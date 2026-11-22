[//]: # (title: Arrays)
<web-summary>Aprenda a criar, acessar, modificar, comparar e converter arrays em Kotlin.</web-summary>

Um array é uma estrutura de dados que armazena um número fixo de valores do mesmo tipo ou de seus subtipos.
Os elementos de um array são ordenados e acessados por índice.

O Kotlin oferece a classe [`Array<T>`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/) e [arrays de tipos primitivos](#primitive-type-arrays).

## Quando usar arrays {id="when-to-use-arrays"}

Use arrays para interoperabilidade com APIs Java ou requisitos de baixo nível. Por exemplo, se você tem requisitos de desempenho
além do que aplicações comuns exigem, ou precisa criar estruturas de dados personalizadas.

Na maioria dos casos, prefira [coleções](collections-overview.md).

| Funcionalidade                                      | Arrays                                                                                                                                               | Coleções                                          |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Tamanho                                             | Fixo                                                                                                                                                 | Depende do tipo                                   |
| Variante somente leitura                            | Não, sempre mutável                                                                                                                                  | Sim (`List` e `Set`)                              |
| Adicionar e remover elementos                       | Sem suporte nativo.<br/> Aloque e copie para um novo array                                                                                           | Sim (coleções mutáveis)                           |
| Igualdade estrutural com `==`                       | Não, compara referências.<br/> Use [`.contentEquals()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/content-equals.html) no lugar | Sim                                               |
| Valores primitivos                                  | Arrays de tipos primitivos armazenam valores<br/> sem boxing                                                                                         | Geralmente com boxing                             |
| Interoperabilidade com Java                         | Mapeia para `T[]`                                                                                                                                    | Mapeia para `java.util.List` e<br/> `java.util.Set` |
| Filtragem e transformações<br/> no estilo funcional | Limitado                                                                                                                                             | Extenso                                           |

Saiba como [converter arrays em coleções](#convert-to-collections).

## Criar arrays {id="create-arrays"}

Para criar arrays, você pode usar:

* As funções [`arrayOf()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/array-of.html), [`arrayOfNulls()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/array-of-nulls.html#kotlin$arrayOfNulls(kotlin.Int)),
ou [`emptyArray()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/empty-array.html).
* O construtor `Array`.

> Declarar um array com `val` apenas impede a reatribuição da variável, mas não torna o conteúdo somente leitura.
> Os elementos são mutáveis tanto em arrays `val` quanto em arrays `var`. A distinção afeta apenas a referência, não o conteúdo.
> Para uma visão somente leitura, use [coleções](collections-overview.md).
> 
{style="note"}

### Array com valores {id="array-with-values"}

Para criar um array tipado a partir de um conjunto conhecido de valores, use a função [`arrayOf()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/array-of.html).
O Kotlin infere o tipo automaticamente:

```kotlin
fun main() {
//sampleStart
    val simpleArray = arrayOf(1, 2, 3) // Array<Int>
    println(simpleArray.joinToString())
    // 1, 2, 3
//sampleEnd
}
```
{kotlin-runnable="true" id="arrays-simple-array-kotlin"}

### Array vazio {id="empty-array"}

Para criar um array sem elementos, use a função [`emptyArray()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/empty-array.html).
Você pode especificar o tipo dos elementos do lado esquerdo ou direito da atribuição:

```kotlin
val emptyArrayRight = emptyArray<String>()
val emptyArrayLeft: Array<String> = emptyArray()
```

Saiba [como adicionar elementos](#add-and-remove-elements) a um array.

### Array com nulls {id="array-with-nulls"}

Para criar um array de um tamanho determinado preenchido com elementos `null`,
use a função [`arrayOfNulls()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/array-of-nulls.html#kotlin$arrayOfNulls(kotlin.Int)):

```kotlin
fun main() {
//sampleStart
    val nullArray: Array<Int?> = arrayOfNulls(3)
    println(nullArray.joinToString())
    // null, null, null
//sampleEnd
}
```
{kotlin-runnable="true" id="arrays-null-array-kotlin"}

### Construtor de array {id="array-constructor"}

O construtor `Array` recebe o tamanho do array e uma função que retorna os valores dos elementos:

```kotlin
fun main() {
//sampleStart
    val zeroes = Array<Int>(3) { 0 }
    println(zeroes.joinToString())
    // 0, 0, 0
    
    val squares = Array(5) { i -> i * i }
    println(squares.joinToString())
    // 0, 1, 4, 9, 16
//sampleEnd
}
```
{kotlin-runnable="true" id="arrays-array-constructor-kotlin"}

### Arrays aninhados {id="nested-arrays"}

Para criar um array aninhado ou multidimensional, use um array de arrays.
Arrays aninhados não precisam ser do mesmo tipo nem ter o mesmo tamanho.

```kotlin
fun main() {
//sampleStart
    // Creates a two-dimensional array
    val twoDArray = Array(2) { Array<Int>(2) { 0 } }
    println(twoDArray.contentDeepToString())
    // [[0, 0], [0, 0]]

    // Creates a three-dimensional array
    val threeDArray = Array(3) { Array(3) { Array<Int>(3) { 0 } } }
    println(threeDArray.contentDeepToString())
    // [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
//sampleEnd
}
```
{kotlin-runnable="true" id="arrays-multidimensional-array-kotlin"}

### Arrays de tipos primitivos {id="primitive-type-arrays"}

Se você usa a classe `Array` com valores primitivos, o compilador encapsula esses valores em objetos (boxing).
Para evitar o custo do boxing, você pode usar arrays de tipos primitivos dedicados.
Eles não são subclasses da classe [`Array<T>`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/), mas oferecem um conjunto semelhante de funções e propriedades.

| Tipo do Kotlin                                                                          | Equivalente em Java |
|-----------------------------------------------------------------------------------------|---------------------|
| [`BooleanArray`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean-array/)   | `boolean[]`         |
| [`ByteArray`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/)         | `byte[]`            |
| [`CharArray`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-array/)         | `char[]`            |
| [`DoubleArray`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/)     | `double[]`          |
| [`FloatArray`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float-array/)       | `float[]`           |
| [`IntArray`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/)           | `int[]`             |
| [`LongArray`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long-array/)         | `long[]`            |
| [`ShortArray`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-short-array/)       | `short[]`           |

> O Kotlin não tem um tipo `StringArray` dedicado. `String` não é um primitivo, então
> use as funções [`arrayOf()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/array-of.html) ou `arrayOf<String>()` com tipo inferido, em vez disso.
> 
{style="note"}

Para criar um array de tipo primitivo, use uma das seguintes opções:

* Funções construtoras:

  ```kotlin
  fun main() {
  //sampleStart
      // Creates an Int array of size 5 with the values initialized to zero
      val primitiveTypeArray = IntArray(5)
      println(primitiveTypeArray.joinToString())
      // 0, 0, 0, 0, 0
  
      // Creates an Int array and takes an initializer function
      val squares = IntArray(5) { i -> i * i }
      println(squares.joinToString())
      // 0, 1, 4, 9, 16
  //sampleEnd
  }
  ```
  {kotlin-runnable="true" id="arrays-primitive-type-array-kotlin"}

* Funções de fábrica:

  ```kotlin
  fun main() {
  //sampleStart
      // Creates an Int array with 5 elements
      val numbers = intArrayOf(1, 2, 3, 4, 5)
      println(numbers.joinToString())
      // 1, 2, 3, 4, 5

      // Creates a Char array with 3 elements
      val characters = charArrayOf('K', 't', 'l')
      println(characters.joinToString())
      // K, t, l

      // Creates a Double array with 3 elements
      val doubles = doubleArrayOf(0.22, 4.16, 0.5)
      println(doubles.joinToString()) 
      // 0.22, 4.16, 0.5
  //sampleEnd
  }
  ```
  {kotlin-runnable="true"}

> Para converter arrays de tipos primitivos em arrays de tipos objeto, use a função [`.toTypedArray()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/to-typed-array.html).
>
> Para converter arrays de tipos objeto em arrays de tipos primitivos, use [`.toBooleanArray()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/to-boolean-array.html),
> [`.toByteArray()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/to-byte-array.html), [`.toCharArray()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/to-char-array.html),
> e assim por diante.
>
{style="note"}

## Trabalhar com arrays {id="work-with-arrays"}

Arrays aceitam muitas das mesmas operações que as coleções, incluindo iteração,
busca, ordenação e transformações.
No Kotlin, você pode trabalhar com arrays usando-os para passar um número variável de argumentos para uma função ou realizando operações
sobre os próprios arrays.
Veja as propriedades e funções mais comuns na tabela a seguir:

| Membro                                                                                                                                                                                                 | Retorna                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| [`size`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/size.html)                                                                                                                        | O número de elementos                         |
| [`indices`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/indices.html)                                                                                                             | O intervalo de índices válidos                |
| [`lastIndex`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/last-index.html)                                                                                                        | O último índice válido                        |
| [`first()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/first.html) e [`last()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/last.html)                    | Primeiro e último elemento                    |
| [`isEmpty()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/is-empty.html) e [`isNotEmpty()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/is-not-empty.html) | `true` se o array estiver vazio ou não vazio  |
| [`contains()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/contains.html)                                                                                                         | `true` se o array tiver o elemento            |

> Saiba mais sobre propriedades e funções de arrays na [referência da API](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/).
> 
{style="tip"}

Esta seção apresenta algumas das operações mais usadas.

### Acessar e modificar elementos {id="access-and-modify-elements"}

Para acessar e modificar elementos em um array, use o [operador de acesso por índice](operator-overloading.md#indexed-access-operator)
(`[]`):

```kotlin
fun main() {
//sampleStart
    val simpleArray = arrayOf(1, 2, 3)
    val twoDArray = Array(2) { Array<Int>(2) { 0 } }

    // Accesses the element and modifies it
    simpleArray[0] = 10
    twoDArray[0][0] = 2

    // Prints the modified element
    println(simpleArray[0]) 
    // 10
    println(twoDArray[0][0]) 
    // 2
//sampleEnd
}
```
{kotlin-runnable="true" id="arrays-access-array-kotlin"}

> Se você tentar acessar um índice fora dos limites de um array, o Kotlin lança `ArrayIndexOutOfBoundsException` em tempo de execução.
>
{style="note"} 

Você também pode usar a função [`fill(element, fromIndex, toIndex)`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/fill.html) para substituir elementos em um intervalo, no próprio array.
`fromIndex` é inclusivo, e `toIndex` é exclusivo:

```kotlin
fun main() {
//sampleStart
    val arr = IntArray(3)
    println(arr.joinToString())
    // 0, 0, 0
    
   arr.fill(1)
   println(arr.joinToString())
   // 1, 1, 1
  
   arr.fill(0, 0, 2)
   println(arr.joinToString())
   // 0, 0, 1
//sampleEnd
}
```
{kotlin-runnable="true"}

No Kotlin, arrays são _invariantes_. Isso significa que `Array<String>` não é um subtipo
de `Array<Any>`. Isso evita possíveis falhas de tipo em tempo de execução. Para expressar covariância, use a
[projeção de tipo](generics.md#type-projections) `Array<out Any>`:

```kotlin
fun main() {
//sampleStart
    fun printArr(arr: Array<out Any>) {
        for (item in arr) print("$item, ")
    }

    printArr(arrayOf("k", "t", "n"))  
    // k, t, n, 
//sampleEnd
}
```
{kotlin-runnable="true"}

### Adicionar e remover elementos {id="add-and-remove-elements"}

Como arrays têm tamanho fixo, eles não oferecem as funções `.add()` e `.remove()`. Para realizar essas operações,
você precisa criar um novo array. Para isso, você pode usar uma das seguintes opções:

* Use a função [`.copyOf`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/copy-of.html):

  ```kotlin
  fun main() {
  //sampleStart
      var arr = intArrayOf(0, 1, 2)
      
      arr = arr.copyOf(arr.size + 1)
      println(arr.joinToString())
      // 0, 1, 2, 0

      arr[arr.lastIndex] = 3
      println(arr.joinToString())
      // 0, 1, 2, 3
  //sampleEnd
  }
  ```
  {kotlin-runnable="true"}

* Use os operadores `+` ou `+=`:

  ```kotlin
  fun main() {
  //sampleStart
      var arr = intArrayOf(0, 1, 2)

      arr += 3
      println(arr.joinToString())
      // 0, 1, 2, 3

      arr = arr + intArrayOf(4, 5)
      println(arr.joinToString())
      // 0, 1, 2, 3, 4, 5
  //sampleEnd
  }
  ```
  {kotlin-runnable="true"}

> Se você precisar adicionar ou remover elementos com frequência,
> use [coleções mutáveis](collections-overview.md#read-only-and-mutable-collections).
>
{style="tip"}

### Comparar arrays {id="compare-arrays"}

Para comparar se dois arrays têm os mesmos elementos na mesma ordem, use as funções [`.contentEquals()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/content-equals.html)
e [`.contentDeepEquals()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/content-deep-equals.html):

```kotlin
fun main() {
//sampleStart
    val simpleArray = arrayOf(1, 2, 3)
    val anotherArray = arrayOf(1, 2, 3)

    // Compares contents of arrays
    println(simpleArray.contentEquals(anotherArray))
    // true

    // Using infix notation, compares contents of arrays after an element 
    // is changed
    simpleArray[0] = 10
    println(simpleArray contentEquals anotherArray)
    // false
//sampleEnd
}
```
{kotlin-runnable="true" id="arrays-compare-array-kotlin"}

> Não use os [operadores](equality.md#structural-equality) de igualdade (`==`) e desigualdade (`!=`) para comparar o conteúdo
> de arrays. Esses operadores verificam se as variáveis atribuídas apontam para o mesmo objeto.
>
> Para saber mais sobre por que os arrays no Kotlin se comportam dessa forma, veja nosso [post no blog](https://blog.jetbrains.com/kotlin/2015/09/feedback-request-limitations-on-data-classes/#Appendix.Comparingarrays).
>
{style="warning"}

### Transformar arrays {id="transform-arrays"}

O Kotlin tem muitas funções úteis para transformar arrays. Esta seção destaca algumas delas.
Veja a lista completa na nossa [referência da API](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/).

#### Soma {id="sum"}

Para retornar a soma de todos os elementos de um array, use a função [`.sum()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/sum.html):

```kotlin
fun main() {
//sampleStart
    val sumArray = arrayOf(1, 2, 3)
    println(sumArray.sum())
    // 6
//sampleEnd
}
```
{kotlin-runnable="true" id="arrays-sum-array-kotlin"}

> A função `.sum()` só pode ser usada com arrays de [tipos numéricos](numbers.md), como `Int`.
>
{style="note"}

#### Ordenar e embaralhar {id="sort-and-shuffle"}

Você pode ordenar os elementos do array de acordo com a ordem natural com a função [`.sort()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sort.html) ou
embaralhá-los aleatoriamente com a função [`.shuffle()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/shuffle.html):

```kotlin
fun main() {
//sampleStart
    val simpleArray = arrayOf(1, 2, 3)

    // Randomly shuffles elements
    simpleArray.shuffle()
    println(simpleArray.joinToString())
  
    // Sorts elements
    simpleArray.sort()
    println(simpleArray.joinToString())
    // 1, 2, 3
//sampleEnd
}
```
{kotlin-runnable="true" id="arrays-shuffle-array-kotlin"}

Para obter um novo array ordenado sem modificar o original, use a função
[`.sortedArray()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sorted-array.html).

### Passar um número variável de argumentos para uma função {id="pass-variable-number-of-arguments-to-a-function"}

No Kotlin, você pode passar um número variável de argumentos para uma função por meio do parâmetro
[`vararg`](functions.md#variable-number-of-arguments-varargs). Isso é útil quando você não sabe de antemão o número de argumentos, como ao formatar uma mensagem ou criar uma consulta SQL.

Para passar um array com um número variável de argumentos para uma função, use o _operador spread_
(`*`). O operador spread passa cada elemento do array como argumentos individuais para a função escolhida:

```kotlin
fun main() {
    val lettersArray = arrayOf("c", "d")
    printAllStrings("a", "b", *lettersArray)
    // abcd
}

fun printAllStrings(vararg strings: String) {
    for (string in strings) {
        print(string)
    }
}
```
{kotlin-runnable="true" id="arrays-vararg-array-kotlin"}

Para mais informações, veja [Número variável de argumentos (varargs)](functions.md#variable-number-of-arguments-varargs).

## Converter para coleções {id="convert-to-collections"}

Se você trabalha com APIs diferentes, em que algumas usam arrays e outras usam coleções, pode converter arrays em coleções e vice-versa.
Para isso, use as funções [`.toList()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/to-list.html), [`.toSet()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/to-set.html) e [`.toMap()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/to-map.html).
Essas funções copiam o conteúdo do array para uma cópia independente. Elas não refletem alterações posteriores no array.

### Converter para List ou Set {id="convert-to-list-or-set"}

Para converter um array em `List` ou `Set`, use as funções [`.toList()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/to-list.html)
e [`.toSet()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/to-set.html):

```kotlin
fun main() {
//sampleStart
    val simpleArray = arrayOf("a", "b", "c", "c")

    // Converts to a Set
    println(simpleArray.toSet())
    // [a, b, c]

    // Converts to a List
    println(simpleArray.toList())
    // [a, b, c, c]
//sampleEnd
}
```
{kotlin-runnable="true" id="arrays-convert-list-set-kotlin"}

A menos que você tenha certeza absoluta de que o array original não será alterado nem compartilhado em outro lugar,
não use [`.asList()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-list.html)
e as demais funções `as*` relacionadas. Essas funções envolvem o array original em vez de copiá-lo. Por isso,
alterações no array são refletidas na lista e vice-versa.

```kotlin
fun main() {
//sampleStart
    val simpleArray = arrayOf("a", "b", "c")

    val list = simpleArray.asList()
    simpleArray[0] = "d"
    println(list)
    // [d, b, c]
//sampleEnd
}
```
{kotlin-runnable="true"}

### Converter para Map {id="convert-to-map"}

Para converter um array em `Map`, use a função [`.toMap()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/to-map.html).

Você só pode converter um array de [`Pair<K,V>`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/) em `Map`.
O primeiro valor de uma instância de `Pair` se torna uma chave, e o segundo se torna um valor.
Se a mesma chave aparecer mais de uma vez, o último valor é usado.

Este exemplo usa a [notação infix](functions.md#infix-notation)
para chamar a função [`.to`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/to.html) e criar tuplas de `Pair`:

```kotlin
fun main() {
//sampleStart
    val pairArray = arrayOf("apple" to 120, "banana" to 150, "cherry" to 90, "apple" to 140)

    // Converts to a Map
    // Fruits are keys, calorie numbers are values
    // The latest "apple" value overwrites the first one
    println(pairArray.toMap())
    // {apple=140, banana=150, cherry=90}
//sampleEnd
}
```
{kotlin-runnable="true" id="arrays-convert-map-kotlin"}

## Próximos passos {id="what-s-next"}

* Saiba mais sobre por que recomendamos usar coleções na maioria dos casos na [visão geral de coleções](collections-overview.md).
* Conheça outros [tipos básicos](types-overview.md).
* Se você é desenvolvedor Java, leia nosso [guia de migração de coleções de Java para Kotlin](java-to-kotlin-collections-guide.md).

<!-- ia-translate: true -->
