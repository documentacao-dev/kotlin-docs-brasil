[//]: # (title: Aliases de tipo)

Aliases de tipo fornecem nomes alternativos para tipos existentes. Eles podem tornar expressões de tipo longas ou muito usadas
mais curtas e fáceis de entender.

Por exemplo, você pode criar aliases para tipos genéricos, tipos de função e classes internas ou aninhadas:

```kotlin
// Generic types
typealias UserIndex = Map<Long, User>
typealias FileTable<K> = MutableMap<K, MutableList<File>>

// Function types
typealias RequestHandler = (Request) -> Response
typealias Predicate<T> = (T) -> Boolean

// Inner and nested classes
class Database {
    inner class Transaction
}
typealias DatabaseTransaction = Database.Transaction
```

Um alias de tipo não cria um novo tipo. Ele introduz um nome alternativo para um tipo existente. O alias e o tipo
subjacente são intercambiáveis. Por exemplo, quando você adiciona `typealias Predicate<T>` e usa `Predicate<Int>`, o compilador
expande para `(Int) -> Boolean`. Você pode usar um valor declarado com o alias em qualquer lugar onde o tipo subjacente for esperado, e
vice-versa:

```kotlin
typealias Predicate<T> = (T) -> Boolean

fun evaluate(predicate: Predicate<Int>) = predicate(42)

fun main() {
    val isPositive: (Int) -> Boolean = { it > 0 }
    println(evaluate(isPositive))
    // true

    val isValid: Predicate<Int> = { it > 0 }
    println(listOf(1, -2).filter(isValid))
    // [1]
}
```
{kotlin-runnable="true"}

## Declarar aliases de tipo {id="declare-type-aliases"}

Você pode declarar um alias de tipo:

* No nível superior de um arquivo Kotlin, como um [alias de tipo de nível superior](#top-level-type-aliases).
* Dentro de uma classe, interface ou object, como um [alias de tipo aninhado](#nested-type-aliases).

Você não pode declarar um alias de tipo em um escopo local, como dentro de uma função ou de uma [expressão lambda](lambdas.md#lambda-expressions-and-anonymous-functions).

A localização da declaração determina o escopo de um alias de tipo, enquanto a visibilidade determina quais trechos de código podem acessá-lo.
Por padrão, um alias de tipo é `public`. Um [alias de tipo aninhado](#nested-type-aliases) é acessível apenas onde sua classe, interface
ou object que o contém é acessível. Por exemplo, um alias `public` dentro de uma classe `internal` não é acessível de fora do módulo.

Um alias de tipo não pode expor um tipo subjacente com [visibilidade](visibility-modifiers.md) mais restritiva que a sua própria. Por exemplo, um alias
`public` não pode se referir a uma classe `private`.

### Aliases de tipo de nível superior {id="top-level-type-aliases"}

Um alias de tipo de nível superior é uma declaração no nível do pacote. Dentro do mesmo pacote, você pode se referir a um alias pelo nome não qualificado.
Para usar o alias a partir de outro pacote, importe o alias ou referencie-o pelo nome qualificado:

```kotlin
// UserId.kt
package org.example.users

typealias UserId = Long

// Refers to the alias within the same package by its unqualified name
fun createUser(id: UserId) {
    // ...
}

// UserService.kt
package org.example.services

import org.example.users.UserId

// Uses the imported alias by its unqualified name
fun findUser(id: UserId) {
    // ...
}

// Uses the fully qualified name
fun deleteUser(id: org.example.users.UserId) {
    // ...
}
```

### Aliases de tipo aninhados {id="nested-type-aliases"}

Aliases de tipo aninhados permitem um código mais limpo e fácil de manter, melhorando o encapsulamento, reduzindo a poluição no nível do pacote
e simplificando implementações internas. Aliases de tipo aninhados seguem as mesmas regras de escopo e de resolução de nomes das [classes aninhadas](nested-classes.md).

Declare um alias de tipo dentro de uma classe, interface ou object quando o nome alternativo for relevante apenas no contexto
dessa declaração. Isso mantém o alias próximo do código que o utiliza e evita adicionar mais um nome ao escopo do pacote.

Dentro da declaração que o contém, você pode se referir ao alias pelo nome não qualificado. Fora dela, qualifique
o alias com o nome da declaração que o contém:

```kotlin
class UserRepository {
    typealias UserIndex = Map<UserId, User>

    // Refers to the alias by its unqualified name inside UserRepository
    fun saveAll(users: UserIndex) {
        // ...
    }
}

// Refers to the alias by its qualified name outside UserRepository
fun synchronizeUsers(users: UserRepository.UserIndex) {
    // ...
}
```

> Aliases de tipo aninhados não são aceitos em [declarações `expect/actual`](https://kotlinlang.org/docs/multiplatform/multiplatform-expect-actual.html) do Kotlin Multiplatform.
>
{style="note"}

#### Parâmetros de tipo {id="type-parameters"}

Para usar parâmetros de tipo em um alias de tipo aninhado, adicione-os à declaração do alias:

```kotlin
class Graph<Node> {
    typealias Path<T> = List<T>
}

val cityPath: Graph.Path<String> = listOf("London", "Berlin")
```

Neste exemplo, `Path` declara seu parâmetro de tipo `T`. Em `Graph.Path<String>`, `String` é o argumento de tipo para `T`
e é independente do parâmetro de tipo `Node` declarado por `Graph`.

Se você se referir a um parâmetro de tipo declarado pela sua classe ou interface que o contém, o compilador reporta um erro:

```kotlin
class Graph<Node> {
    typealias Path = List<Node>
    // Unresolved reference 'Node'.
}
```

Aqui, `Path` se refere a `Node` de `Graph` em vez de declarar seu próprio parâmetro de tipo.

<!-- ia-translate: true -->
