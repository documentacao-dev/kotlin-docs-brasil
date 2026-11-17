[//]: # (title: Scope functions)

<no-index/>


Neste capítulo, você vai expandir o que aprendeu sobre extension functions e aprender a usar scope functions
para escrever código mais idiomático.

## Scope functions {id="scope-functions"}

Em programação, escopo é a área em que sua variável ou objeto é reconhecido. Os escopos mais citados são o escopo
global e o escopo local:

* **Escopo global** – uma variável ou objeto acessível de qualquer lugar do programa.
* **Escopo local** – uma variável ou objeto acessível apenas dentro do bloco ou da função em que é definido.

Em Kotlin, também existem scope functions, que permitem criar um escopo temporário em torno de um objeto e executar
algum código.

Scope functions deixam o código mais conciso, porque você não precisa referenciar o nome do objeto dentro do escopo
temporário. Dependendo da scope function, você pode acessar o objeto pela palavra-chave `this` ou usá-lo como
argumento pela palavra-chave `it`.

O Kotlin tem cinco scope functions no total: `let`, `apply`, `run`, `also` e `with`.

Cada scope function recebe uma expressão lambda e retorna o objeto ou o resultado da expressão lambda. Neste tour,
explicamos cada scope function e como usá-la.

> Você também pode assistir à palestra [Back to the Stdlib: Making the Most of Kotlin's Standard Library](https://youtu.be/DdvgvSHrN9g?feature=shared&t=1511)
> sobre scope functions, de Sebastian Aigner, developer advocate do Kotlin.
> 
{style="tip"}

### Let

Use a scope function `let` quando quiser fazer verificações de nulo no código e, depois, executar outras ações
com o objeto retornado.

Considere o exemplo:

```kotlin
fun sendNotification(recipientAddress: String): String {
    println("Yo $recipientAddress!")
    return "Notification sent!"
}

fun getNextAddress(): String {
    return "sebastian@jetbrains.com"
}

fun main() {
    val address: String? = getNextAddress()
    sendNotification(address)
}
```
{validate = "false"}

O exemplo tem duas funções:
* `sendNotification()`, que tem um parâmetro de função `recipientAddress` e retorna uma string.
* `getNextAddress()`, que não tem parâmetros de função e retorna uma string.

O exemplo cria a variável `address`, que tem o tipo `String` nullable. Isso se torna um problema ao chamar a função
`sendNotification()`, porque essa função não espera que `address` possa ser um valor `null`. Como resultado, o compilador
reporta um erro:

```text
Argument type mismatch: actual type is 'String?', but 'String' was expected.
```

Do tour para iniciantes, você já sabe que pode fazer uma verificação de nulo com uma condição if ou usar o
[operador Elvis `?:`](kotlin-tour-null-safety.md#use-elvis-operator). Mas e se você quiser usar o objeto retornado
mais adiante no código? Dá para fazer isso com uma condição if **e** um ramo else:

```kotlin
fun sendNotification(recipientAddress: String): String {
    println("Yo $recipientAddress!")
    return "Notification sent!"
}

fun getNextAddress(): String {
    return "sebastian@jetbrains.com"
}

fun main() { 
    //sampleStart
    val address: String? = getNextAddress()
    val confirm = if(address != null) {
        sendNotification(address)
    } else { null }
    //sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-scope-function-let-non-null-if"}

No entanto, uma forma mais concisa é usar a scope function `let`:

```kotlin
fun sendNotification(recipientAddress: String): String {
    println("Yo $recipientAddress!")
    return "Notification sent!"
}

fun getNextAddress(): String {
    return "sebastian@jetbrains.com"
}

fun main() {
    //sampleStart
    val address: String? = getNextAddress()
    val confirm = address?.let {
        sendNotification(it)
    }
    //sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-scope-function-let-non-null"}

O exemplo:
* Cria as variáveis `address` e `confirm`.
* Usa uma chamada segura para a scope function `let` na variável `address`.
* Cria um escopo temporário dentro da scope function `let`.
* Passa a função `sendNotification()` como expressão lambda para a scope function `let`.
* Referencia a variável `address` por meio de `it`, dentro do escopo temporário.
* Atribui o resultado à variável `confirm`.

Com essa abordagem, o código lida com o caso de a variável `address` ser `null`, e você pode usar a variável
`confirm` mais adiante no código.

### Apply

Use a scope function `apply` para inicializar objetos, como uma instância de classe, no momento da criação, em vez de
fazer isso mais adiante no código. Essa abordagem deixa o código mais fácil de ler e de manter.

Considere o exemplo:

```kotlin
class Client() {
    var token: String? = null
    fun connect() = println("connected!")
    fun authenticate() = println("authenticated!")
    fun getData() : String {
        println("getting data!")
        return "Mock data"
    }
}

val client = Client()

fun main() {
    client.token = "asdf"
    client.connect()
    // connected!
    client.authenticate()
    // authenticated!
    client.getData()
    // getting data!
}
```
{kotlin-runnable="true" id="kotlin-tour-scope-function-apply-before"}

O exemplo tem uma classe `Client` que contém uma propriedade chamada `token` e três funções membro: `connect()`,
`authenticate()` e `getData()`.

O exemplo cria `client` como instância da classe `Client` antes de inicializar sua propriedade `token` e chamar suas
funções membro na função `main()`.

Embora este exemplo seja compacto, no mundo real pode demorar até você conseguir configurar e usar a instância da classe
(e suas funções membro) depois de criá-la. No entanto, se você usar a scope function `apply`, pode criar, configurar e
usar as funções membro da instância no mesmo lugar do código:

```kotlin
class Client() {
    var token: String? = null
    fun connect() = println("connected!")
    fun authenticate() = println("authenticated!")
    fun getData() : String {
        println("getting data!")
        return "Mock data"
    }
}
//sampleStart
val client = Client().apply {
    token = "asdf"
    connect()
    // connected!
    authenticate()
    // authenticated!
}

fun main() {
    client.getData()
    // getting data!
}
//sampleEnd
```
{kotlin-runnable="true" id="kotlin-tour-scope-function-apply-after"}

O exemplo:

* Cria `client` como instância da classe `Client`.
* Usa a scope function `apply` na instância `client`.
* Cria um escopo temporário dentro da scope function `apply`, para que você não precise se referir explicitamente à instância `client` ao acessar suas propriedades ou funções.
* Passa uma expressão lambda para a scope function `apply` que atualiza a propriedade `token` e chama as funções `connect()` e `authenticate()`.
* Chama a função membro `getData()` na instância `client` dentro da função `main()`.

Como você pode ver, essa estratégia é conveniente quando você trabalha com trechos grandes de código.

### Run

Assim como `apply`, você pode usar a scope function `run` para inicializar um objeto, mas é melhor usar `run` para
inicializar um objeto em um momento específico do código **e** calcular um resultado imediatamente.

Vamos continuar o exemplo anterior da função `apply`, mas desta vez você quer que as funções `connect()` e
`authenticate()` fiquem agrupadas, para serem chamadas a cada requisição.

Por exemplo:

```kotlin
class Client() {
    var token: String? = null
    fun connect() = println("connected!")
    fun authenticate() = println("authenticated!")
    fun getData() : String {
        println("getting data!")
        return "Mock data"
    }
}

//sampleStart
val client: Client = Client().apply {
    token = "asdf"
}

fun main() {
    val result: String = client.run {
        connect()
        // connected!
        authenticate()
        // authenticated!
        getData()
        // getting data!
    }
}
//sampleEnd
```
{kotlin-runnable="true" id="kotlin-tour-scope-function-run"}

O exemplo:

* Cria `client` como instância da classe `Client`.
* Usa a scope function `apply` na instância `client`.
* Cria um escopo temporário dentro da scope function `apply`, para que você não precise se referir explicitamente à instância `client` ao acessar suas propriedades ou funções.
* Passa uma expressão lambda para a scope function `apply` que atualiza a propriedade `token`.

A função `main()`:

* Cria uma variável `result` com o tipo `String`.
* Usa a scope function `run` na instância `client`.
* Cria um escopo temporário dentro da scope function `run`, para que você não precise se referir explicitamente à instância `client` ao acessar suas propriedades ou funções.
* Passa uma expressão lambda para a scope function `run` que chama as funções `connect()`, `authenticate()` e `getData()`.
* Atribui o resultado à variável `result`.

Agora você pode usar o resultado retornado mais adiante no código.

### Also

Use a scope function `also` para executar uma ação adicional com um objeto e, em seguida, retornar o próprio objeto
para continuar usando-o no código, como para escrever um log.

Considere o exemplo:

```kotlin
fun main() {
    val medals: List<String> = listOf("Gold", "Silver", "Bronze")
    val reversedLongUppercaseMedals: List<String> =
        medals
            .map { it.uppercase() }
            .filter { it.length > 4 }
            .reversed()
    println(reversedLongUppercaseMedals)
    // [BRONZE, SILVER]
}
```
{kotlin-runnable="true" id="kotlin-tour-scope-function-also-before"}

O exemplo:

* Cria a variável `medals` que contém uma lista de strings.
* Cria a variável `reversedLongUpperCaseMedals` com o tipo `List<String>`.
* Usa a extension function `.map()` na variável `medals`.
* Passa uma expressão lambda para `.map()` que referencia `medals` pela palavra-chave `it` e chama a extension function `.uppercase()` nela.
* Usa a extension function `.filter()` na variável `medals`.
* Passa uma expressão lambda como predicado para `.filter()` que referencia `medals` pela palavra-chave `it` e verifica se o item da lista tem mais de 4 caracteres.
* Usa a extension function `.reversed()` na variável `medals`.
* Atribui o resultado à variável `reversedLongUpperCaseMedals`.
* Imprime a lista contida na variável `reversedLongUpperCaseMedals`.

Seria útil adicionar um log entre as chamadas de função para ver o que acontece com a variável `medals`.
A função `also` ajuda nisso:

```kotlin
fun main() {
    val medals: List<String> = listOf("Gold", "Silver", "Bronze")
    val reversedLongUppercaseMedals: List<String> =
        medals
            .map { it.uppercase() }
            .also { println(it) }
            // [GOLD, SILVER, BRONZE]
            .filter { it.length > 4 }
            .also { println(it) }
            // [SILVER, BRONZE]
            .reversed()
    println(reversedLongUppercaseMedals)
    // [BRONZE, SILVER]
}
```
{kotlin-runnable="true" id="kotlin-tour-scope-function-also-after"}

Agora o exemplo:

* Usa a scope function `also` na variável `medals`.
* Cria um escopo temporário dentro da scope function `also`, para que você não precise se referir explicitamente à variável `medals` ao usá-la como parâmetro de função.
* Passa uma expressão lambda para a scope function `also` que chama a função `println()` usando a variável `medals` como parâmetro de função, pela palavra-chave `it`.

Como a função `also` retorna o objeto, ela é útil não só para log, mas também para depuração, encadeamento de várias
operações e outras operações com efeitos colaterais que não afetam o fluxo principal do código.

### With

Diferente das outras scope functions, `with` não é uma extension function, então a sintaxe é outra. Você passa o
objeto receiver para `with` como argumento.

Use a scope function `with` quando quiser chamar várias funções em um objeto.

Considere este exemplo:

```kotlin
class Canvas {
    fun rect(x: Int, y: Int, w: Int, h: Int): Unit = println("$x, $y, $w, $h")
    fun circ(x: Int, y: Int, rad: Int): Unit = println("$x, $y, $rad")
    fun text(x: Int, y: Int, str: String): Unit = println("$x, $y, $str")
}

fun main() {
    val mainMonitorPrimaryBufferBackedCanvas = Canvas()

    mainMonitorPrimaryBufferBackedCanvas.text(10, 10, "Foo")
    mainMonitorPrimaryBufferBackedCanvas.rect(20, 30, 100, 50)
    mainMonitorPrimaryBufferBackedCanvas.circ(40, 60, 25)
    mainMonitorPrimaryBufferBackedCanvas.text(15, 45, "Hello")
    mainMonitorPrimaryBufferBackedCanvas.rect(70, 80, 150, 100)
    mainMonitorPrimaryBufferBackedCanvas.circ(90, 110, 40)
    mainMonitorPrimaryBufferBackedCanvas.text(35, 55, "World")
    mainMonitorPrimaryBufferBackedCanvas.rect(120, 140, 200, 75)
    mainMonitorPrimaryBufferBackedCanvas.circ(160, 180, 55)
    mainMonitorPrimaryBufferBackedCanvas.text(50, 70, "Kotlin")
}
```
{kotlin-runnable="true" id="kotlin-tour-scope-function-with-before"}

O exemplo cria uma classe `Canvas` com três funções membro: `rect()`, `circ()` e `text()`. Cada uma dessas funções
membro imprime uma mensagem montada a partir dos parâmetros de função que você fornece.

O exemplo cria `mainMonitorPrimaryBufferBackedCanvas` como instância da classe `Canvas` e, em seguida, chama uma
sequência de funções membro nessa instância, com parâmetros de função diferentes.

Você pode ver que esse código é difícil de ler. Se você usar a função `with`, o código fica mais enxuto:

```kotlin
class Canvas {
    fun rect(x: Int, y: Int, w: Int, h: Int): Unit = println("$x, $y, $w, $h")
    fun circ(x: Int, y: Int, rad: Int): Unit = println("$x, $y, $rad")
    fun text(x: Int, y: Int, str: String): Unit = println("$x, $y, $str")
}

fun main() {
    //sampleStart
    val mainMonitorSecondaryBufferBackedCanvas = Canvas()
    with(mainMonitorSecondaryBufferBackedCanvas) {
        text(10, 10, "Foo")
        rect(20, 30, 100, 50)
        circ(40, 60, 25)
        text(15, 45, "Hello")
        rect(70, 80, 150, 100)
        circ(90, 110, 40)
        text(35, 55, "World")
        rect(120, 140, 200, 75)
        circ(160, 180, 55)
        text(50, 70, "Kotlin")
    }
    //sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-scope-function-with-after"}

Este exemplo:
* Usa a scope function `with` com a instância `mainMonitorSecondaryBufferBackedCanvas` como receiver.
* Cria um escopo temporário dentro da scope function `with`, para que você não precise se referir explicitamente à instância `mainMonitorSecondaryBufferBackedCanvas` ao chamar suas funções membro.
* Passa uma expressão lambda para a scope function `with` que chama uma sequência de funções membro com parâmetros de função diferentes.

Agora que esse código é bem mais fácil de ler, você tem menos chances de cometer erros.

## Visão geral dos casos de uso {id="use-case-overview"}

Esta seção apresentou as scope functions disponíveis no Kotlin e seus principais casos de uso, para deixar seu
código mais idiomático. Você pode usar esta tabela como referência rápida. Você não precisa entender por completo
como essas funções funcionam para usá-las no código.

| Scope function | Acesso a `x` por meio de | Valor de retorno | Caso de uso                                                                                                  |
|----------------|--------------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| `let`          | `it`                     | Resultado da expressão lambda | Fazer verificações de nulo no código e, depois, executar outras ações com o objeto retornado. |
| `apply`        | `this`                   | `x`              | Inicializar objetos no momento da criação.                                                                   |
| `run`          | `this`                   | Resultado da expressão lambda | Inicializar objetos no momento da criação **E** calcular um resultado.                       |
| `also`         | `it`                     | `x`              | Executar ações adicionais antes de retornar o objeto.                                                        |
| `with`         | `this`                   | Resultado da expressão lambda | Chamar várias funções em um objeto.                                                                          |

Para mais informações sobre scope functions, consulte [Scope functions](scope-functions.md).

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Reescreva uma função usando chamadas seguras e let" id="scope-functions-exercise-1">

Reescreva a função `.getPriceInEuros()` como uma função de expressão única que usa os operadores de chamada segura `?.`
e a scope function `let`.

<deflist collapsible="true">
    <def title="Dica">
        Use os operadores de chamada segura <code>?.</code> para acessar com segurança a propriedade <code>priceInDollars</code>
        da função <code>getProductInfo()</code>. Depois, use a scope function <code>let</code> para converter o valor de
        <code>priceInDollars</code> em euros.
    </def>
</deflist>

```kotlin
data class ProductInfo(val priceInDollars: Double?)

class Product {
    fun getProductInfo(): ProductInfo? {
        return ProductInfo(100.0)
    }
}

// Rewrite this function
fun Product.getPriceInEuros(): Double? {
    val info = getProductInfo()
    if (info == null) return null
    val price = info.priceInDollars
    if (price == null) return null
    return convertToEuros(price)
}

fun convertToEuros(dollars: Double): Double {
    return dollars * 0.85
}

fun main() {
    val product = Product()
    val priceInEuros = product.getPriceInEuros()

    if (priceInEuros != null) {
        println("Price in Euros: €$priceInEuros")
        // Price in Euros: €85.0
    } else {
        println("Price information is not available.")
    }
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/GetPriceInEurosTest.kt" validate="false" id="kotlin-tour-scope-functions-exercise-1"}

```kotlin
data class ProductInfo(val priceInDollars: Double?)

class Product {
    fun getProductInfo(): ProductInfo? {
        return ProductInfo(100.0)
    }
}

fun Product.getPriceInEuros() = getProductInfo()?.priceInDollars?.let { convertToEuros(it) }

fun convertToEuros(dollars: Double): Double {
    return dollars * 0.85
}

fun main() {
    val product = Product()
    val priceInEuros = product.getPriceInEuros()

    if (priceInEuros != null) {
        println("Price in Euros: €$priceInEuros")
        // Price in Euros: €85.0
    } else {
        println("Price information is not available.")
    }
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/GetPriceInEurosTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-scope-functions-solution-1"}

</def>
<def title="Encadeie apply e also" id="scope-functions-exercise-2">

Você tem uma função `updateEmail()` que atualiza o endereço de e-mail de um usuário. Use a scope function `apply` para
atualizar o endereço de e-mail e, depois, a scope function `also` para imprimir uma mensagem de log:
`Updating email for user with ID: ${it.id}`.

```kotlin
data class User(val id: Int, var email: String)

fun updateEmail(user: User, newEmail: String): User = TODO("Replace the TODO() function")

fun main() {
    val user = User(1, "old_email@example.com")
    val updatedUser = updateEmail(user, "new_email@example.com")
    // Updating email for user with ID: 1

    println("Updated User: $updatedUser")
    // Updated User: User(id=1, email=new_email@example.com)
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/UpdateEmailTest.kt" validate="false" id="kotlin-tour-scope-functions-exercise-2"}

```kotlin
data class User(val id: Int, var email: String)

fun updateEmail(user: User, newEmail: String): User = user.apply {
    this.email = newEmail
}.also { println("Updating email for user with ID: ${it.id}") }

fun main() {
    val user = User(1, "old_email@example.com")
    val updatedUser = updateEmail(user, "new_email@example.com")
    // Updating email for user with ID: 1

    println("Updated User: $updatedUser")
    // Updated User: User(id=1, email=new_email@example.com)
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/UpdateEmailTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-scope-functions-solution-2"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-intermediate-extension-functions.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-intermediate-lambdas-receiver.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->
