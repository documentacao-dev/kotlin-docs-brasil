[//]: # (title: Objetos)

<no-index/>


Neste capítulo, você vai ampliar sua compreensão sobre classes explorando declarações de object. Esse conhecimento vai
ajudar você a gerenciar comportamento de forma eficiente nos seus projetos.

## Declarações de object {id="object-declarations"}

No Kotlin, você pode usar **declarações de object** para declarar uma classe com uma única instância. De certa forma,
você declara a classe e cria a instância única _ao mesmo tempo_. Declarações de object são úteis quando você quer criar
uma classe para usar como um ponto de referência único no seu programa ou para coordenar comportamento em todo um sistema.

> Uma classe que tem apenas uma instância, facilmente acessível, é chamada de **singleton**.
>
{style="tip"}

Objects no Kotlin são **lazy**, ou seja, são criados somente quando acessados. O Kotlin também garante que todos os
objects sejam criados de forma thread-safe, para que você não precise verificar isso manualmente.

Para criar uma declaração de object, use a palavra-chave `object`:

```kotlin
object DoAuth {}
```

Depois do nome do seu `object`, adicione quaisquer propriedades ou funções membro dentro do corpo do object, definido
por chaves `{}`.

> Objects não podem ter construtores, então não têm cabeçalhos como as classes.
>
{style="note"}

Por exemplo, suponha que você queira criar um object chamado `DoAuth` responsável pela autenticação:

```kotlin
object DoAuth {
    fun takeParams(username: String, password: String) {
        println("input Auth parameters = $username:$password")
    }
}

fun main(){
    // The object is created when the takeParams() function is called
    DoAuth.takeParams("coding_ninja", "N1njaC0ding!")
    // input Auth parameters = coding_ninja:N1njaC0ding!
}
```
{kotlin-runnable="true" id="kotlin-tour-object-declarations"}

O object tem uma função membro chamada `takeParams`, que aceita as variáveis `username` e `password` como parâmetros e
imprime uma string no console. O object `DoAuth` só é criado quando a função é chamada pela primeira vez.

> Objects podem herdar de classes e interfaces. Por exemplo:
> 
> ```kotlin
> interface Auth {
>     fun takeParams(username: String, password: String)
> }
>
> object DoAuth : Auth {
>     override fun takeParams(username: String, password: String) {
>         println("input Auth parameters = $username:$password")
>     }
> }
> ```
>
{style="note"}

#### Data objects

Para facilitar a impressão do conteúdo de uma declaração de object, o Kotlin tem **data objects**. Assim como as data
classes, que você conheceu no tour para iniciantes, os data objects vêm automaticamente com funções membro adicionais:
`toString()` e `equals()`.

> Diferente das data classes, os data objects não vêm automaticamente com a função membro `copy()`, porque têm uma única
> instância que não pode ser copiada.
>
{type ="note"}

Para criar um data object, use a mesma sintaxe das declarações de object, mas com o prefixo da palavra-chave `data`:

```kotlin
data object AppConfig {}
```

Por exemplo:

```kotlin
data object AppConfig {
    var appName: String = "My Application"
    var version: String = "1.0.0"
}

fun main() {
    println(AppConfig)
    // AppConfig
    
    println(AppConfig.appName)
    // My Application
}
```
{kotlin-runnable="true" id="kotlin-tour-data-objects"}

Para mais informações sobre data objects, veja [](object-declarations.md#data-objects).

#### Companion objects

No Kotlin, uma classe pode ter um object: um **companion** object. Você só pode ter **um** companion object por classe.
Um companion object é criado somente quando a sua classe é referenciada pela primeira vez.

Quaisquer propriedades ou funções declaradas dentro de um companion object são compartilhadas por todas as instâncias
da classe.

Para criar um companion object dentro de uma classe, use a mesma sintaxe de uma declaração de object, mas com o prefixo
da palavra-chave `companion`:

```kotlin
companion object Bonger {}
```

> Um companion object não precisa ter nome. Se você não definir um, o padrão é `Companion`.
> 
{style="note"}

Para acessar qualquer propriedade ou função do companion object, referencie o nome da classe. Por exemplo:

```kotlin
class BigBen {
    companion object Bonger {
        fun getBongs(nTimes: Int) {
            repeat(nTimes) { print("BONG ") }
            }
        }
    }

fun main() {
    // Companion object is created when the class is referenced for the
    // first time.
    BigBen.getBongs(12)
    // BONG BONG BONG BONG BONG BONG BONG BONG BONG BONG BONG BONG 
}
```
{kotlin-runnable="true" id="kotlin-tour-classes-companion-object"}

Este exemplo cria uma classe chamada `BigBen` que contém um companion object chamado `Bonger`. O companion object tem uma
função membro chamada `getBongs()`, que aceita um inteiro e imprime `"BONG"` no console o mesmo número de vezes que o
inteiro.

Na função `main()`, a função `getBongs()` é chamada referenciando o nome da classe. Neste momento, o companion object é
criado. A função `getBongs()` é chamada com o parâmetro `12`.

Para mais informações, veja [](object-declarations.md#companion-objects).

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Implementar um data object para rastreamento de pedidos" id="objects-exercise-1">

Você administra uma cafeteria e tem um sistema para rastrear os pedidos dos clientes. Considere o código abaixo e complete
a declaração do segundo data object para que o código a seguir, na função `main()`, seja executado com sucesso:

```kotlin
interface Order {
    val orderId: String
    val customerName: String
    val orderTotal: Double
}

data object OrderOne: Order {
    override val orderId = "001"
    override val customerName = "Alice"
    override val orderTotal = 15.50
}

data object // Write your code here

fun main() {
    // Print the name of each data object
    println("Order name: $OrderOne")
    // Order name: OrderOne
    println("Order name: $OrderTwo")
    // Order name: OrderTwo

    // Check if the orders are identical
    println("Are the two orders identical? ${OrderOne == OrderTwo}")
    // Are the two orders identical? false

    if (OrderOne == OrderTwo) {
        println("The orders are identical.")
    } else {
        println("The orders are unique.")
        // The orders are unique.
    }

    println("Do the orders have the same customer name? ${OrderOne.customerName == OrderTwo.customerName}")
    // Do the orders have the same customer name? false
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/OrderTwoTest.kt" validate="false" id="kotlin-tour-objects-exercise-1"}

```kotlin
interface Order {
    val orderId: String
    val customerName: String
    val orderTotal: Double
}

data object OrderOne: Order {
    override val orderId = "001"
    override val customerName = "Alice"
    override val orderTotal = 15.50
}

data object OrderTwo: Order {
    override val orderId = "002"
    override val customerName = "Bob"
    override val orderTotal = 12.75
}

fun main() {
    // Print the name of each data object
    println("Order name: $OrderOne")
    // Order name: OrderOne
    println("Order name: $OrderTwo")
    // Order name: OrderTwo

    // Check if the orders are identical
    println("Are the two orders identical? ${OrderOne == OrderTwo}")
    // Are the two orders identical? false

    if (OrderOne == OrderTwo) {
        println("The orders are identical.")
    } else {
        println("The orders are unique.")
        // The orders are unique.
    }

    println("Do the orders have the same customer name? ${OrderOne.customerName == OrderTwo.customerName}")
    // Do the orders have the same customer name? false
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/OrderTwoTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-objects-solution-1"}

</def>
<def title="Criar uma declaração de object" id="objects-exercise-2">

Crie uma declaração de object que herde da interface `Vehicle` para criar um tipo de veículo único: `FlyingSkateboard`.
Implemente a propriedade `name` e a função `move()` no seu object para que o código a seguir, na função `main()`, seja
executado com sucesso:

```kotlin
interface Vehicle {
    val name: String
    fun move(): String
}

object // Write your code here

fun main() {
    println("${FlyingSkateboard.name}: ${FlyingSkateboard.move()}")
    // Flying Skateboard: Glides through the air with a hover engine
    println("${FlyingSkateboard.name}: ${FlyingSkateboard.fly()}")
    // Flying Skateboard: Woooooooo
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/FlyingSkateboardTest.kt" validate="false" id="kotlin-tour-objects-exercise-2"}

```kotlin
interface Vehicle {
    val name: String
    fun move(): String
}

object FlyingSkateboard : Vehicle {
    override val name = "Flying Skateboard"
    override fun move() = "Glides through the air with a hover engine"

   fun fly(): String = "Woooooooo"
}

fun main() {
    println("${FlyingSkateboard.name}: ${FlyingSkateboard.move()}")
    // Flying Skateboard: Glides through the air with a hover engine
    println("${FlyingSkateboard.name}: ${FlyingSkateboard.fly()}")
    // Flying Skateboard: Woooooooo
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/FlyingSkateboardTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-objects-solution-2"}

</def>
<def title="Validar um endereço de e-mail antes de criar um usuário" id="objects-exercise-3">

Você está construindo um módulo de cadastro de usuários para um app. Você quer manter a validação de e-mail associada à
classe `User`, mas não quer criar uma instância `User` desnecessária se o endereço de e-mail for inválido.

Neste exercício, considere um endereço de e-mail válido se ele contiver `@` e `.`. Complete a data class para que o código
a seguir, na função `main()`, seja executado com sucesso:

<deflist collapsible="true">
    <def title="Dica">
        Adicione uma função de validação de e-mail em um companion object da classe `User`, para que você possa chamar a função diretamente em `User`.
    </def>
</deflist>

```kotlin
data class User(val name: String, val email: String) {
    // Write your code here
}

fun main() {
    val candidates = listOf(
        Pair("Alice", "alice@example.com"),
        Pair("Bob", "bob2example-com")
    )

    for ((name, email) in candidates) {
        if (User.isValidEmail(email)) {
            val user = User(name, email)
            println("Registered: ${user.name}, ${user.email}")
            // Registered: Alice, alice@example.com
        } else {
            println("Error: '${email}' is not valid. The email should contain '@' and '.'")
            // Error: 'bob2example-com' is not valid. The email should contain '@' and '.'
        }
    }
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/UserTest.kt" validate="false" id="kotlin-tour-objects-exercise-3"}

```kotlin
data class User(val name: String, val email: String) {
    companion object {
        fun isValidEmail(email: String): Boolean =
            email.contains('@') && email.contains('.')
    }
}

fun main() {
    val candidates = listOf(
        Pair("Alice", "alice@example.com"),
        Pair("Bob", "bob2example-com")
    )

    for ((name, email) in candidates) {
        if (User.isValidEmail(email)) {
            val user = User(name, email)
            println("Registered: ${user.name}, ${user.email}")
            // Registered: Alice, alice@example.com
        } else {
            println("Error: '${email}' is not valid. The email should contain '@' and '.'")
            // Error: 'bob2example-com' is not valid. The email should contain '@' and '.'
        }
    }
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/UserTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-objects-solution-3"}

> Como extensão deste exercício, experimente usar funções em companion objects como métodos factory para construir
> instâncias de uma classe. Para um exemplo e mais informações sobre esse padrão, veja
> [](object-declarations.md#companion-objects).
>
{style="tip"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-intermediate-classes-interfaces.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-intermediate-open-special-classes.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->