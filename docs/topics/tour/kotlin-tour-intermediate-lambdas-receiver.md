[//]: # (title: Expressões lambda com receiver)

<no-index/>


Neste capítulo, você vai aprender a usar receivers com outro tipo de função, as expressões lambda, e como elas podem
ajudar a criar uma linguagem específica de domínio (DSL).

## Expressões lambda com receiver {id="lambda-expressions-with-receiver"}

No tour para iniciantes, você aprendeu a usar [expressões lambda](kotlin-tour-functions.md#lambda-expressions). Expressões lambda também podem ter um receiver. 
Nesse caso, elas podem acessar quaisquer funções ou propriedades membro do receiver sem precisar especificar o receiver explicitamente a cada vez. Sem essas referências extras, seu código fica mais fácil de ler e de manter.

> Expressões lambda com receiver também são conhecidas como literais de função com receiver.
>
{style="tip"}

A sintaxe de uma expressão lambda com receiver é diferente na definição do tipo da função. Primeiro, escreva o receiver
que você quer estender. Em seguida, coloque um `.` e complete o restante da definição do tipo da função. Por exemplo:

```kotlin
MutableList<Int>.() -> Unit
```

Esse tipo de função tem:

* `MutableList<Int>` como receiver.
* Nenhum parâmetro de função dentro dos parênteses `()`.
* Nenhum valor de retorno: `Unit`.

Considere este exemplo que desenha formas em um canvas:

```kotlin
class Canvas {
    fun drawCircle() = println("🟠 Drawing a circle")
    fun drawSquare() = println("🟥 Drawing a square")
}

// Lambda expression with receiver definition
fun render(block: Canvas.() -> Unit): Canvas {
    val canvas = Canvas()
    // Use the lambda expression with receiver
    canvas.block()
    return canvas
}

fun main() {
    render {
        drawCircle()
        // 🟠 Drawing a circle
        drawSquare()
        // 🟥 Drawing a square
    }
}
```
{kotlin-runnable="true" id="kotlin-intermediate-tour-lambda-expression-with-receiver"}

Neste exemplo:

* A classe `Canvas` tem duas funções que simulam o desenho de um círculo ou de um quadrado.
* A função `render()` recebe um parâmetro `block` e retorna uma instância da classe `Canvas`.
* O parâmetro `block` é uma expressão lambda com receiver, em que a classe `Canvas` é o receiver.
* A função `render()` cria uma instância da classe `Canvas` e chama a expressão lambda `block()` na instância `canvas`, usando-a como receiver.
* A função `main()` chama a função `render()` com uma expressão lambda, que é passada para o parâmetro `block`.
* Dentro da lambda passada para a função `render()`, o programa chama as funções `drawCircle()` e `drawSquare()` em uma instância da classe `Canvas`.

  Como as funções `drawCircle()` e `drawSquare()` são chamadas na expressão lambda com receiver, elas podem ser chamadas
  diretamente, como se estivessem dentro da classe `Canvas`.

Expressões lambda com receiver são úteis quando você quer criar uma linguagem específica de domínio (DSL). Como você tem
acesso às funções e propriedades membro do receiver sem referenciar o receiver explicitamente, seu código fica mais enxuto.

Para demonstrar isso, considere um exemplo que configura itens em um menu. Vamos começar com uma classe `MenuItem` e uma
classe `Menu` que contém uma função para adicionar itens ao menu, chamada `item()`, além de uma lista com todos os itens
do menu, `items`:

```kotlin
class MenuItem(val name: String)

class Menu(val name: String) {
    val items = mutableListOf<MenuItem>()

    fun item(name: String) {
        items.add(MenuItem(name))
    }
}
```

Vamos usar uma expressão lambda com receiver passada como parâmetro de função (`init`) para a função `menu()`, que monta
um menu como ponto de partida:

```kotlin
fun menu(name: String, init: Menu.() -> Unit): Menu {
    // Creates an instance of the Menu class
    val menu = Menu(name)
    // Calls the lambda expression with receiver init() on the class instance
    menu.init()
    return menu
}
```

Agora você pode usar a DSL para configurar um menu e criar uma função `printMenu()` para imprimir a estrutura do menu no console:

```kotlin
class MenuItem(val name: String)

class Menu(val name: String) {
    val items = mutableListOf<MenuItem>()

    fun item(name: String) {
        items.add(MenuItem(name))
    }
}

fun menu(name: String, init: Menu.() -> Unit): Menu {
    val menu = Menu(name)
    menu.init()
    return menu
}

//sampleStart
fun printMenu(menu: Menu) {
    println("Menu: ${menu.name}")
    menu.items.forEach { println("  Item: ${it.name}") }
}

// Use the DSL
fun main() {
    // Create the menu
    val mainMenu = menu("Main Menu") {
        // Add items to the menu
        item("Home")
        item("Settings")
        item("Exit")
    }

    // Print the menu
    printMenu(mainMenu)
    // Menu: Main Menu
    //   Item: Home
    //   Item: Settings
    //   Item: Exit
}
//sampleEnd
```
{kotlin-runnable="true" id="kotlin-intermediate-tour-lambda-expression-with-receiver-dsl"}

Como você pode ver, usar uma expressão lambda com receiver simplifica bastante o código necessário para criar seu menu.
Expressões lambda são úteis não só para criação e montagem, mas também para configuração. Elas são comumente usadas na
construção de DSLs para APIs, frameworks de UI e builders de configuração, produzindo código enxuto e permitindo que você
se concentre mais facilmente na estrutura e na lógica do código subjacente.

O ecossistema do Kotlin tem vários exemplos desse padrão de design, como as funções [`buildList()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/build-list.html)
e [`buildString()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/build-string.html) da biblioteca padrão.

> Expressões lambda com receivers podem ser combinadas com **builders com segurança de tipos** em Kotlin para criar DSLs
> que detectam problemas de tipo em tempo de compilação, em vez de em tempo de execução. Para saber mais, veja
> [Builders com segurança de tipos](type-safe-builders.md).
>
{style="tip"}

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Processar dados com uma expressão lambda com receiver" id="lambda-receivers-exercise-1">

Você tem uma função `fetchData()` que aceita uma expressão lambda com receiver. Atualize a expressão lambda para usar
a função `append()`, de modo que a saída do código seja: `Data received - Processed`.

```kotlin
fun fetchData(callback: StringBuilder.() -> Unit) {
    val builder = StringBuilder("Data received")
    builder.callback()
}

fun main() {
    fetchData {
        // Write your code here
        // Data received - Processed
    }
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/FetchDataTest.kt" validate="false" id="kotlin-tour-lambda-receivers-exercise-1"}

```kotlin
fun fetchData(callback: StringBuilder.() -> Unit) {
    val builder = StringBuilder("Data received")
    builder.callback()
}

fun main() {
    fetchData {
        append(" - Processed")
        println(this.toString())
        // Data received - Processed
    }
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/FetchDataTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-lambda-receivers-solution-1"}

</def>
<def title="Tratar um evento de clique duplo" id="lambda-receivers-exercise-2">

Você tem uma classe `Button` e as data classes `ButtonEvent` e `Position`. Escreva um código que dispare a função membro
`onEvent()` da classe `Button` para acionar um evento de clique duplo. Seu código deve imprimir `"Double click!"`.

```kotlin
class Button {
    fun onEvent(action: ButtonEvent.() -> Unit) {
        // Simulate a double-click event (not a right-click)
        val event = ButtonEvent(isRightClick = false, amount = 2, position = Position(100, 200))
        event.action() // Trigger the event callback
    }
}

data class ButtonEvent(
    val isRightClick: Boolean,
    val amount: Int,
    val position: Position
)

data class Position(
    val x: Int,
    val y: Int
)

fun main() {
    val button = Button()

    button.onEvent {
        // Write your code here
        // Double click!
    }
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/ButtonEventTest.kt" validate="false" id="kotlin-tour-lambda-receivers-exercise-2"}

```kotlin
class Button {
    fun onEvent(action: ButtonEvent.() -> Unit) {
        // Simulate a double-click event (not a right-click)
        val event = ButtonEvent(isRightClick = false, amount = 2, position = Position(100, 200))
        event.action() // Trigger the event callback
    }
}

data class ButtonEvent(
    val isRightClick: Boolean,
    val amount: Int,
    val position: Position
)

data class Position(
    val x: Int,
    val y: Int
)

fun main() {
    val button = Button()
    
    button.onEvent {
        if (!isRightClick && amount == 2) {
            println("Double click!")
            // Double click!
        }
    }
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/ButtonEventTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-lambda-receivers-solution-2"}

</def>
<def title="Criar uma lista incrementada" id="lambda-receivers-exercise-3">

Escreva uma função que crie uma cópia de uma lista de inteiros em que cada elemento seja incrementado em 1. Use o
esqueleto de função fornecido, que estende `List<Int>` com uma função `incremented`.

```kotlin
fun List<Int>.incremented(): List<Int> {
    val originalList = this
    return buildList {
        // Write your code here
    }
}

fun main() {
    val originalList = listOf(1, 2, 3)
    val newList = originalList.incremented()
    println(newList)
    // [2, 3, 4]
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/IncrementedTest.kt" validate="false" id="kotlin-tour-lambda-receivers-exercise-3"}

```kotlin
fun List<Int>.incremented(): List<Int> {
    val originalList = this
    return buildList {
        for (n in originalList) add(n + 1)
    }
}

fun main() {
    val originalList = listOf(1, 2, 3)
    val newList = originalList.incremented()
    println(newList)
    // [2, 3, 4]
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/IncrementedTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-lambda-receivers-solution-3"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-intermediate-scope-functions.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-intermediate-classes-interfaces.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->