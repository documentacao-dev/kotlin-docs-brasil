[//]: # (title: Extension functions)

<no-index/>


Neste capítulo, você vai explorar funções especiais do Kotlin que deixam seu código mais conciso e legível. Veja como elas podem ajudar você a usar padrões de design eficientes e levar seus projetos para o próximo nível.

## Extension functions {id="extension-functions"}

No desenvolvimento de software, muitas vezes você precisa modificar o comportamento de um programa sem alterar o código-fonte original.
Por exemplo, talvez você queira adicionar funcionalidades extras a uma classe de uma biblioteca de terceiros.

Você pode fazer isso adicionando _extension functions_ para estender uma classe. Você chama extension functions da mesma forma que chama funções membro de uma classe, usando um ponto `.`.

Antes de apresentar a sintaxe completa das extension functions, você precisa entender o que é um **receiver**.
O receiver é aquilo sobre o qual a função é chamada. Em outras palavras, o receiver é onde, ou com quem, a informação é compartilhada.

![Um exemplo de sender e receiver](receiver-highlight.png){width="500"}

Neste exemplo, a função `main()` chama a função [`.first()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/first.html) para retornar o primeiro elemento de uma lista.
A função `.first()` é chamada **sobre** a variável `readOnlyShapes`, então a variável `readOnlyShapes` é o receiver.

Para criar uma extension function, escreva o nome da classe que você quer estender, seguido de um `.` e do nome da função.
Continue com o restante da declaração da função, incluindo seus parâmetros e o tipo de retorno.

Por exemplo:

```kotlin
fun String.bold(): String = "<b>$this</b>"

fun main() {
    // "hello" is the receiver
    println("hello".bold())
    // <b>hello</b>
}
```
{kotlin-runnable="true" id="kotlin-tour-extension-function"}

Neste exemplo:

* `String` é a classe estendida.
* `bold` é o nome da extension function.
* O tipo de retorno da extension function `.bold()` é `String`.
* `"hello"`, uma instância de `String`, é o receiver.
* O receiver é acessado dentro do corpo pela [palavra-chave](keyword-reference.md): `this`.
* Um template de string (`$`) é usado para acessar o valor de `this`.
* A extension function `.bold()` recebe uma string e a retorna dentro de um elemento HTML `<b>`, usado para texto em negrito.

## Design orientado a extension functions {id="extension-oriented-design"}

Você pode definir extension functions em qualquer lugar, o que permite criar designs orientados a extension functions. Esses designs separam a funcionalidade central de recursos úteis, mas não essenciais, tornando o código mais fácil de ler e manter.

Um bom exemplo é a classe [`HttpClient`](https://api.ktor.io/ktor-client-core/io.ktor.client/-http-client/index.html) da biblioteca Ktor, que ajuda a fazer requisições de rede. O núcleo da funcionalidade dela é uma única função `request()`, que recebe todas as informações necessárias para uma requisição HTTP:

```kotlin
class HttpClient {
    fun request(method: String, url: String, headers: Map<String, String>): HttpResponse {
        // Network code
    }
}
```
{validate="false"}

Na prática, as requisições HTTP mais populares são as requisições GET e POST. Faz sentido para a biblioteca fornecer nomes mais curtos para esses casos de uso comuns. No entanto, eles não exigem escrever código de rede novo, apenas uma chamada específica de requisição. Em outras palavras, são candidatos perfeitos para serem definidos como extension functions separadas `.get()` e `.post()`:

```kotlin
fun HttpClient.get(url: String): HttpResponse = request("GET", url, emptyMap())
fun HttpClient.post(url: String): HttpResponse = request("POST", url, emptyMap())
```
{validate="false"}

Essas funções `.get()` e `.post()` estendem a classe `HttpClient`. Elas podem usar diretamente a função `request()` da classe `HttpClient`, porque são chamadas sobre uma instância da classe `HttpClient` como receiver. Você pode usar essas extension functions para chamar a função `request()` com o método HTTP apropriado, o que simplifica seu código e facilita o entendimento:

```kotlin
class HttpClient {
    fun request(method: String, url: String, headers: Map<String, String>): HttpResponse {
        println("Requesting $method to $url with headers: $headers")
        return HttpResponse("Response from $url")
    }
}

fun HttpClient.get(url: String): HttpResponse = request("GET", url, emptyMap())

fun main() {
    val client = HttpClient()

    // Making a GET request using request() directly
    val getResponseWithMember = client.request("GET", "https://example.com", emptyMap())

    // Making a GET request using the get() extension function
    // The client instance is the receiver
    val getResponseWithExtension = client.get("https://example.com")
}
```
{validate="false"}

Essa abordagem orientada a extension functions é amplamente usada na [biblioteca padrão](https://kotlinlang.org/api/latest/jvm/stdlib/) do Kotlin e em outras bibliotecas. Por exemplo, a classe `String` tem muitas [extension functions](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/#extension-functions) para ajudar você a trabalhar com strings.

Para mais informações sobre extension functions, consulte [Extensões](extensions.md).

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Verifique se um inteiro é positivo" id="extension-functions-exercise-1">

Escreva uma extension function chamada `isPositive` que recebe um inteiro e verifica se ele é positivo.

```kotlin
fun Int.// Write your code here

fun main() {
    println(1.isPositive())
    // true
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/IsPositiveTest.kt" validate="false" id="kotlin-tour-extension-functions-exercise-1"}

```kotlin
fun Int.isPositive(): Boolean = this > 0

fun main() {
    println(1.isPositive())
    // true
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/IsPositiveTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-extension-functions-solution-1"}

</def>
<def title="Converta uma string para minúsculas" id="extension-functions-exercise-2">

Escreva uma extension function chamada `toLowercaseString` que recebe uma string e retorna uma versão em minúsculas.

<deflist collapsible="true">
    <def title="Dica">
        Use a função <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/lowercase.html"> <code>.lowercase()</code>
        </a> do tipo <code>String</code>. 
    </def>
</deflist>

```kotlin
fun // Write your code here

fun main() {
    println("Hello World!".toLowercaseString())
    // hello world!
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/ToLowercaseStringTest.kt" validate="false" id="kotlin-tour-extension-functions-exercise-2"}

```kotlin
fun String.toLowercaseString(): String = this.lowercase()

fun main() {
    println("Hello World!".toLowercaseString())
    // hello world!
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/ToLowercaseStringTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-extension-functions-solution-2"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-null-safety.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-intermediate-scope-functions.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->
