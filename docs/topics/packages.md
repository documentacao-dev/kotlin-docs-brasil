[//]: # (title: Pacotes e imports)

Em um projeto Kotlin, o código é organizado usando pacotes e imports:

* Um **pacote** é um contêiner para um ou mais arquivos Kotlin. Os arquivos são vinculados a um pacote por meio de um cabeçalho `package`.
* Um **import** é uma diretiva que torna entidades de outros pacotes disponíveis no arquivo atual.

## Cabeçalhos de pacote {id="package-headers"}

Um arquivo de código-fonte pode começar com um cabeçalho de pacote:

```kotlin
package org.example

fun printMessage() { /*...*/ }
class Message(val text: String) { /*...*/ }
```

Todo o conteúdo do arquivo de código-fonte, como classes e funções, pertence a esse pacote.
O nome totalmente qualificado de cada entidade combina o nome do pacote com o nome da entidade.
Neste exemplo:

* O nome totalmente qualificado de `printMessage()` é `org.example.printMessage`.
* O nome totalmente qualificado de `Message` é `org.example.Message`.

Se um arquivo não tiver cabeçalho de pacote, o conteúdo dele pertence ao pacote raiz.

## Imports

Para usar uma entidade de um arquivo em outro pacote, use uma diretiva `import`.
Além dos imports padrão, cada arquivo pode declarar os próprios imports.

### Importar uma única entidade {id="import-a-single-entity"}

Importe uma entidade específica para usá-la sem qualificação:

```kotlin
// Message is accessible without qualification
import org.example.Message 

fun main() {
    val message = Message("Hello")
    println(message.text)
}
```

### Importar o conteúdo de um escopo {id="import-the-contents-of-a-scope"}

Imports com asterisco `*` importam todas as entidades nomeadas dentro do escopo correspondente:

```kotlin
// Everything in org.example is accessible
import org.example.* 

fun main() {
    printMessage()
    val message = Message("Hi")
}
```

Se você importar uma entidade com um import com asterisco e também com um import explícito,
o import explícito tem prioridade na resolução de sobrecarga.

### Resolver conflitos de nome com aliases {id="resolve-name-clashes-with-aliases"}

Se duas entidades importadas tiverem o mesmo nome, use a palavra-chave `as` para renomear localmente uma delas:

```kotlin
// Message refers to org.example.Message
import org.example.Message

// TestMessage refers to org.test.Message
import org.test.Message as TestMessage

fun main() {
    val a = Message("from example")
    val b = TestMessage("from test")
}
```

### O que você pode importar {id="what-you-can-import"}

A palavra-chave `import` não se limita a classes. Você pode importar qualquer uma das entidades a seguir,
seja ela de um pacote, de uma classe, de um `object` ou de um enum:

* Funções e propriedades de nível superior declaradas diretamente dentro de um pacote:
    ```kotlin
    import org.example.printMessage // Top-level function
    import org.example.VERSION      // Top-level property
    ```
* Funções e propriedades de [declarações de `object`](object-declarations.md#object-declarations-overview):
    ```kotlin
    import org.example.Config.DEFAULT_TIMEOUT // Property from an object
    import org.example.Config.loadSettings    // Function from an object
    ```
* Membros de um [companion object](object-declarations.md#companion-objects), referenciados pelo nome da classe que o contém:
    ```kotlin
    import org.example.MyClass.create // Refers to MyClass.Companion.create
    ```
* [Constantes de enum](enum-classes.md):
    ```kotlin
    import org.example.Color.RED
    import org.example.Color.GREEN
    ```
* Classes aninhadas:
    ```kotlin
    import org.example.Outer.Nested
    ```

## Imports padrão {id="default-imports"}

O Kotlin inclui os seguintes imports por padrão:

* [kotlin.*](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/index.html)
* [kotlin.annotation.*](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/index.html)
* [kotlin.collections.*](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/index.html)
* [kotlin.comparisons.*](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/index.html)
* [kotlin.io.*](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/index.html)
* [kotlin.ranges.*](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/index.html)
* [kotlin.sequences.*](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/index.html)
* [kotlin.text.*](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/index.html)
* [kotlin.math.*](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/index.html)

Dependendo da plataforma de destino, o Kotlin importa pacotes adicionais:

* JVM:
  * [java.lang.*](https://docs.oracle.com/javase/8/docs/api/java/lang/package-summary.html)
  * [kotlin.jvm.*](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/index.html)

* JS:
  * [kotlin.js.*](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/index.html)

## Visibilidade e imports {id="visibility-and-imports"}

A possibilidade de importar uma entidade depende dos [modificadores de visibilidade](visibility-modifiers.md):

* Entidades `public` podem ser importadas em qualquer lugar.
* Entidades `internal` podem ser importadas apenas dentro do mesmo módulo.
* Entidades `protected` não podem ser importadas.
* Entidades `private` de nível superior são acessíveis apenas dentro do arquivo em que são declaradas.
* Outras entidades `private` não podem ser importadas.

<!-- ia-translate: true -->
