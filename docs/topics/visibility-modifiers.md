[//]: # (title: Modificadores de visibilidade)

Classes, objects, interfaces, construtores e funções, além de propriedades e seus setters, podem ter *modificadores de visibilidade*.
Os getters sempre têm a mesma visibilidade de suas propriedades.

Existem quatro modificadores de visibilidade no Kotlin: `private`, `protected`, `internal` e `public`.
A visibilidade padrão é `public`.

Nesta página, você vai aprender como os modificadores se aplicam a diferentes tipos de escopos de declaração.

## Pacotes {id="packages"}

Funções, propriedades, classes, objects e interfaces podem ser declarados no "nível superior" diretamente dentro de um pacote:

```kotlin
// file name: example.kt
package foo

fun baz() { ... }
class Bar { ... }
```

* Se você não usar um modificador de visibilidade, `public` é usado por padrão, o que significa que suas declarações ficam
  visíveis em qualquer lugar.
* Se você marcar uma declaração como `private`, ela ficará visível apenas dentro do arquivo que contém a declaração.
* Se você marcar como `internal`, ela ficará visível em qualquer lugar do mesmo [módulo](#modules).
* O modificador `protected` não está disponível para declarações de nível superior.

>Para usar uma declaração de nível superior visível a partir de outro pacote, você deve [importá-la](packages.md#imports).
>
{style="note"}

Exemplos:

```kotlin
// file name: example.kt
package foo

private fun foo() { ... } // visible inside example.kt

public var bar: Int = 5 // property is visible everywhere
    private set         // setter is visible only in example.kt
    
internal val baz = 6    // visible inside the same module
```

## Membros de classe {id="class-members"}

Para membros declarados dentro de uma classe:

* `private` significa que o membro é visível apenas dentro desta classe (incluindo todos os seus membros).
* `protected` significa que o membro tem a mesma visibilidade de um marcado como `private`, mas também fica visível nas subclasses.
* `internal` significa que qualquer cliente *dentro deste módulo* que enxergar a classe declarante enxerga os membros `internal` dela.
* `public` significa que qualquer cliente que enxergar a classe declarante enxerga os membros `public` dela.

> No Kotlin, uma classe externa não enxerga os membros private de suas classes internas.
>
{style="note"}

Se você sobrescrever um membro `protected` ou `internal` e não especificar a visibilidade explicitamente, o membro
que sobrescreve também terá a mesma visibilidade do original.

Exemplos:

```kotlin
open class Outer {
    private val a = 1
    protected open val b = 2
    internal open val c = 3
    val d = 4  // public by default
    
    protected class Nested {
        public val e: Int = 5
    }
}

class Subclass : Outer() {
    // a is not visible
    // b, c and d are visible
    // Nested and e are visible

    override val b = 5   // 'b' is protected
    override val c = 7   // 'c' is internal
}

class Unrelated(o: Outer) {
    // o.a, o.b are not visible
    // o.c and o.d are visible (same module)
    // Outer.Nested is not visible, and Nested::e is not visible either 
}
```

### Construtores {id="constructors"}

Use a sintaxe a seguir para especificar a visibilidade do construtor primário de uma classe:

> Você precisa adicionar a palavra-chave `constructor` explicitamente.
>
{style="note"}

```kotlin
class C private constructor(a: Int) { ... }
```

Aqui o construtor é `private`. Por padrão, todos os construtores são `public`, o que na prática significa que eles
ficam visíveis em qualquer lugar onde a classe é visível (ou seja, um construtor de uma classe `internal` é visível apenas
dentro do mesmo módulo).

Para classes seladas, os construtores são `protected` por padrão. Para mais informações, consulte [Classes seladas](sealed-classes.md#constructors).

### Declarações locais {id="local-declarations"}

Variáveis, funções e classes locais não podem ter modificadores de visibilidade.

## Módulos {id="modules"}

O modificador de visibilidade `internal` significa que o membro é visível dentro do mesmo módulo. Mais especificamente,
um módulo é um conjunto de arquivos Kotlin compilados juntos, por exemplo:

* Um módulo do IntelliJ IDEA.
* Um projeto Maven.
* Um source set do Gradle (com a exceção de que o source set `test` pode acessar as declarações internal de `main`).

<!-- ia-translate: true -->
