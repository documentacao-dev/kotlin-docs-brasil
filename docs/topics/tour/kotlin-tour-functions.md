[//]: # (title: Funções)

<no-index/>


Você pode declarar suas próprias funções em Kotlin usando a palavra-chave `fun`.

```kotlin
fun hello() {
    return println("Hello, world!")
}

fun main() {
    hello()
    // Hello, world!
}
```
{kotlin-runnable="true" id="kotlin-tour-function-demo"}

Em Kotlin:

* Os parâmetros da função são escritos entre parênteses `()`.
* Cada parâmetro precisa ter um tipo, e vários parâmetros devem ser separados por vírgulas `,`.
* O tipo de retorno é escrito depois dos parênteses `()` da função, separado por dois-pontos `:`.
* O corpo de uma função é escrito entre chaves `{}`.
* A palavra-chave `return` é usada para sair da função e retornar algum valor.

> Se uma função não retorna nada útil, o tipo de retorno e a palavra-chave `return` podem ser omitidos. Saiba mais sobre
> isso em [Funções sem retorno](#functions-without-return).
>
{style="note"}

No exemplo a seguir:

* `x` e `y` são parâmetros da função.
* `x` e `y` têm o tipo `Int`.
* O tipo de retorno da função é `Int`.
* A função retorna a soma de `x` e `y` quando é chamada.

```kotlin
fun sum(x: Int, y: Int): Int {
    return x + y
}

fun main() {
    println(sum(1, 2))
    // 3
}
```
{kotlin-runnable="true" id="kotlin-tour-simple-function"}

> Nas nossas [convenções de código](coding-conventions.md#function-names), recomendamos nomear funções começando com
> letra minúscula e usar camel case, sem underscores.
>
{style="note"}

## Argumentos nomeados {id="named-arguments"}

Para deixar o código mais conciso, ao chamar a função você não precisa incluir os nomes dos parâmetros. No entanto, incluí-los
deixa o código mais fácil de ler. Isso se chama usar **argumentos nomeados**. Se você incluir os nomes dos parâmetros, poderá
escrevê-los em qualquer ordem.

> No exemplo a seguir, [templates de string](strings.md#string-templates) (`$`) são usados para acessar
> os valores dos parâmetros, convertê-los para o tipo `String` e concatená-los em uma string para impressão.
>
{style="tip"}

```kotlin
fun printMessageWithPrefix(message: String, prefix: String) {
    println("[$prefix] $message")
}

fun main() {
    // Uses named arguments with swapped parameter order
    printMessageWithPrefix(prefix = "Log", message = "Hello")
    // [Log] Hello
}
```
{kotlin-runnable="true" id="kotlin-tour-named-arguments-function"}

## Valores padrão de parâmetros {id="default-parameter-values"}

Você pode definir valores padrão para os parâmetros da função. Qualquer parâmetro com valor padrão pode ser omitido ao
chamar a função. Para declarar um valor padrão, use o operador de atribuição `=` depois do tipo:

```kotlin
fun printMessageWithPrefix(message: String, prefix: String = "Info") {
    println("[$prefix] $message")
}

fun main() {
    // Function called with both parameters
    printMessageWithPrefix("Hello", "Log") 
    // [Log] Hello
    
    // Function called only with message parameter
    printMessageWithPrefix("Hello")        
    // [Info] Hello
    
    printMessageWithPrefix(prefix = "Log", message = "Hello")
    // [Log] Hello
}
```
{kotlin-runnable="true" id="kotlin-tour-default-param-function"}

> Você pode pular parâmetros específicos que têm valores padrão, em vez de omitir todos. No entanto, depois do
> primeiro parâmetro pulado, você deve nomear todos os parâmetros seguintes.
>
{style="note"}

## Funções sem retorno {id="functions-without-return"}

Se a função não retorna um valor útil, então o tipo de retorno dela é `Unit`. `Unit` é um tipo com apenas um valor,
`Unit`. Você não precisa declarar explicitamente que `Unit` é retornado no corpo da função. Isso significa que você não
precisa usar a palavra-chave `return` nem declarar um tipo de retorno:

```kotlin
fun printMessage(message: String) {
    println(message)
    // `return Unit` or `return` is optional
}

fun main() {
    printMessage("Hello")
    // Hello
}
```
{kotlin-runnable="true" id="kotlin-tour-unit-function"}

## Funções de expressão única {id="single-expression-functions"}

Para deixar o código mais conciso, você pode usar funções de expressão única. Por exemplo, a função `sum()` pode ser encurtada:

```kotlin
fun sum(x: Int, y: Int): Int {
    return x + y
}

fun main() {
    println(sum(1, 2))
    // 3
}
```
{kotlin-runnable="true" id="kotlin-tour-simple-function-before"}

Você pode remover as chaves `{}` e declarar o corpo da função usando o operador de atribuição `=`. Quando você usa o operador de atribuição `=`, o Kotlin usa inferência de tipo, então você também pode omitir o tipo de retorno. Assim, a função `sum()` vira uma única linha:

```kotlin
fun sum(x: Int, y: Int) = x + y

fun main() {
    println(sum(1, 2))
    // 3
}
```
{kotlin-runnable="true" id="kotlin-tour-simple-function-after"}

No entanto, se você quer que outros desenvolvedores entendam o código rapidamente, é uma boa ideia definir explicitamente
o tipo de retorno, mesmo ao usar o operador de atribuição `=`.

> Se você usa chaves `{}` para declarar o corpo da função, precisa declarar o tipo de retorno, a menos que seja o tipo `Unit`.
>
{style="note"}

## Retornos antecipados em funções {id="early-returns-in-functions"}

Para interromper o processamento do código da função a partir de determinado ponto, use a palavra-chave `return`. Este exemplo
usa `if` para retornar da função antecipadamente quando a expressão condicional for verdadeira:

```kotlin
// A list of registered usernames
val registeredUsernames = mutableListOf("john_doe", "jane_smith")

// A list of registered emails
val registeredEmails = mutableListOf("john@example.com", "jane@example.com")

fun registerUser(username: String, email: String): String {
    // Early return if the username is already taken
    if (username in registeredUsernames) {
        return "Username already taken. Please choose a different username."
    }

    // Early return if the email is already registered
    if (email in registeredEmails) {
        return "Email already registered. Please use a different email."
    }

    // Proceed with the registration if the username and email are not taken
    registeredUsernames.add(username)
    registeredEmails.add(email)

    return "User registered successfully: $username"
}

fun main() {
    println(registerUser("john_doe", "newjohn@example.com"))
    // Username already taken. Please choose a different username.
    println(registerUser("new_user", "newuser@example.com"))
    // User registered successfully: new_user
}
```
{kotlin-runnable="true" id="kotlin-tour-function-early-return"}

## Prática: funções {id="practice-functions"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Calcule a área de um círculo" id="functions-exercise-1">

Escreva uma função chamada `circleArea` que recebe o raio de um círculo no formato inteiro como parâmetro e imprime a
área desse círculo.

> Neste exercício, você importa um pacote para acessar o valor de <math>π</math> por meio de `PI`. Para mais informações sobre
> importação de pacotes, veja [Pacotes e importações](packages.md).
>
{style="tip"}

<deflist collapsible="true" id="kotlin-tour-functions-exercise-1-hint">
    <def title="Dica">
        A fórmula para calcular a área de um círculo é <math>πr^2</math>, em que <math>r</math> é o raio.
    </def>
</deflist>

```kotlin
import kotlin.math.PI

// Write your code here

fun main() {
    println(circleArea(2))
}
```
{validate="false" kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/CircleAreaTest.kt" id="kotlin-tour-functions-exercise-1"}

```kotlin
import kotlin.math.PI

fun circleArea(radius: Int): Double {
    return PI * radius * radius
}

fun main() {
    println(circleArea(2)) // 12.566370614359172
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/CircleAreaTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-functions-solution-1"}

</def>
<def title="Reescreva uma função como expressão única" id="functions-exercise-2">

Reescreva a função `circleArea` do exercício anterior como uma função de expressão única.

```kotlin
import kotlin.math.PI

//sampleStart
// Write your code here
//sampleEnd

fun main() {
    println(circleArea(2))
}
```
{validate="false" kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/CircleAreaTest.kt" folded-button="false" id="kotlin-tour-functions-exercise-2"}

```kotlin
import kotlin.math.PI

fun circleArea(radius: Int): Double = PI * radius * radius

fun main() {
    println(circleArea(2)) // 12.566370614359172
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/CircleAreaTest.kt" folded-button="false" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-functions-solution-2"}

</def>
<def title="Refatore uma função usando parâmetros padrão e argumentos nomeados" id="functions-exercise-3">

Você tem uma função que converte um intervalo de tempo dado em horas, minutos e segundos para segundos. Na maioria dos casos,
você precisa passar apenas um ou dois parâmetros da função, enquanto os demais são iguais a 0. Melhore a função e o código que
a chama, usando valores padrão de parâmetros e argumentos nomeados para que o código seja mais fácil de ler.

```kotlin
// Refactor this function: give hours, minutes, and seconds default values of 0
fun intervalInSeconds(hours: Int, minutes: Int, seconds: Int) =
    ((hours * 60) + minutes) * 60 + seconds

fun main() {
    // Simplify these calls with named arguments where possible
    println(intervalInSeconds(1, 20, 15))
    println(intervalInSeconds(0, 1, 25))
    println(intervalInSeconds(2, 0, 0))
    println(intervalInSeconds(0, 10, 0))
    println(intervalInSeconds(1, 0, 1))
}
```
{validate="false" kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/IntervalInSecondsTest.kt" id="kotlin-tour-functions-exercise-3"}

```kotlin
fun intervalInSeconds(hours: Int = 0, minutes: Int = 0, seconds: Int = 0) =
    ((hours * 60) + minutes) * 60 + seconds

fun main() {
    println(intervalInSeconds(1, 20, 15))
    println(intervalInSeconds(minutes = 1, seconds = 25))
    println(intervalInSeconds(hours = 2))
    println(intervalInSeconds(minutes = 10))
    println(intervalInSeconds(hours = 1, seconds = 1))
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/IntervalInSecondsTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-functions-solution-3"}

</def>
</deflist>

## Expressões lambda {id="lambda-expressions"}

Kotlin permite escrever um código ainda mais conciso para funções usando expressões lambda.

Por exemplo, a seguinte função `uppercaseString()`:

```kotlin
fun uppercaseString(text: String): String {
    return text.uppercase()
}
fun main() {
    println(uppercaseString("hello"))
    // HELLO
}
```
{kotlin-runnable="true" id="kotlin-tour-lambda-function-before"}

Também pode ser escrita como uma expressão lambda:

```kotlin
fun main() {
    val upperCaseString = { text: String -> text.uppercase() }
    println(upperCaseString("hello"))
    // HELLO
}
```
{kotlin-runnable="true" id="kotlin-tour-lambda-variable"}

Expressões lambda podem ser difíceis de entender à primeira vista, então vamos detalhá-las. Expressões lambda são escritas
entre chaves `{}`.

Dentro da expressão lambda, você escreve:

* Os parâmetros seguidos de `->`.
* O corpo da função depois do `->`.

No exemplo anterior:

* `text` é um parâmetro da função.
* `text` tem o tipo `String`.
* A função retorna o resultado da função [`.uppercase()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/uppercase.html)
chamada em `text`.
* A expressão lambda inteira é atribuída à variável `upperCaseString` com o operador de atribuição `=`.
* A expressão lambda é chamada usando a variável `upperCaseString` como uma função e a string `"hello"` como parâmetro.
* A função `println()` imprime o resultado.

> Se você declarar uma lambda sem parâmetros, não é preciso usar `->`. Por exemplo:
> ```kotlin
> { println("Log message") }
> ```
>
{style="note"}

Expressões lambda podem ser usadas de várias maneiras. Você pode:

* [Passar uma expressão lambda como parâmetro para outra função](#pass-to-another-function)
* [Retornar uma expressão lambda de uma função](#return-from-a-function)
* [Invocar uma expressão lambda isoladamente](#invoke-separately)

### Passar para outra função {id="pass-to-another-function"}

Um ótimo exemplo de quando é útil passar uma expressão lambda para uma função é usar a função [`.filter()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/filter.html)
em coleções:

```kotlin
fun main() {
    //sampleStart
    val numbers = listOf(1, -2, 3, -4, 5, -6)
    
    val positives = numbers.filter ({ x -> x > 0 })
    
    val isNegative = { x: Int -> x < 0 }
    val negatives = numbers.filter(isNegative)
    
    println(positives)
    // [1, 3, 5]
    println(negatives)
    // [-2, -4, -6]
    //sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-lambda-filter"}

A função `.filter()` aceita uma expressão lambda como predicado e a aplica a cada elemento da lista. A função mantém um elemento somente se o predicado retornar `true`:

* `{ x -> x > 0 }` retorna `true` se o elemento for positivo.
* `{ x -> x < 0 }` retorna `true` se o elemento for negativo.

Este exemplo demonstra duas maneiras de passar uma expressão lambda para uma função:

* Para números positivos, o exemplo adiciona a expressão lambda diretamente na função `.filter()`.
* Para números negativos, o exemplo atribui a expressão lambda à variável `isNegative`. Depois, a
variável `isNegative` é usada como parâmetro da função `.filter()`. Nesse caso, você precisa especificar
o tipo dos parâmetros da função (`x`) na expressão lambda.

> Se uma expressão lambda for o único parâmetro da função, você pode omitir os parênteses `()` da função:
>
> ```kotlin
> val positives = numbers.filter { x -> x > 0 }
> ```
>
> Este é um exemplo de [lambda final](#trailing-lambdas), que veremos com mais detalhes no fim deste
> capítulo.
>
{style="note"}

Outro bom exemplo é usar a função [`.map()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/map.html)
para transformar itens de uma coleção:

```kotlin
fun main() {
    //sampleStart
    val numbers = listOf(1, -2, 3, -4, 5, -6)
    val doubled = numbers.map { x -> x * 2 }
    
    val isTripled = { x: Int -> x * 3 }
    val tripled = numbers.map(isTripled)
    
    println(doubled)
    // [2, -4, 6, -8, 10, -12]
    println(tripled)
    // [3, -6, 9, -12, 15, -18]
    //sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-lambda-map"}

A função `.map()` aceita uma expressão lambda como função de transformação:

* `{ x -> x * 2 }` pega cada elemento da lista e retorna esse elemento multiplicado por 2.
* `{ x -> x * 3 }` pega cada elemento da lista e retorna esse elemento multiplicado por 3.

### Tipos de função {id="function-types"}

Antes de retornar uma expressão lambda de uma função, primeiro você precisa entender os **tipos de função**.

Você já aprendeu sobre tipos básicos, mas as próprias funções também têm um tipo. A inferência de tipo do Kotlin
consegue inferir o tipo de uma função a partir do tipo do parâmetro. Mas pode haver momentos em que você precise
especificar explicitamente o tipo da função. O compilador precisa do tipo da função para saber o que é e o que não é
permitido para essa função.

A sintaxe de um tipo de função é composta por:

* O tipo de cada parâmetro escrito entre parênteses `()` e separado por vírgulas `,`.
* O tipo de retorno escrito depois de `->`.

Por exemplo: `(String) -> String` ou `(Int, Int) -> Int`.

É assim que fica uma expressão lambda quando um tipo de função é definido para `upperCaseString()`:

```kotlin
val upperCaseString: (String) -> String = { text -> text.uppercase() }

fun main() {
    println(upperCaseString("hello"))
    // HELLO
}
```
{kotlin-runnable="true" id="kotlin-tour-lambda-function-type"}

Se a expressão lambda não tem parâmetros, os parênteses `()` ficam vazios. Por exemplo: `() -> Unit`

> Você deve declarar os tipos de parâmetro e de retorno na expressão lambda ou como um tipo de função. Caso contrário, o
> compilador não consegue saber qual é o tipo da expressão lambda.
>
> Por exemplo, o código a seguir não funciona:
>
> `val upperCaseString = { str -> str.uppercase() }`
>
{style="note"}

### Retornar de uma função {id="return-from-a-function"}

Expressões lambda podem ser retornadas de uma função. Para que o compilador entenda qual é o tipo da expressão lambda
retornada, você precisa declarar um tipo de função.

No exemplo a seguir, a função `toSeconds()` tem o tipo de função `(Int) -> Int`, porque sempre retorna uma expressão
lambda que recebe um parâmetro do tipo `Int` e retorna um valor `Int`.

Este exemplo usa uma expressão `when` para determinar qual expressão lambda é retornada quando `toSeconds()` é chamada:

```kotlin
fun toSeconds(time: String): (Int) -> Int = when (time) {
    "hour" -> { value -> value * 60 * 60 }
    "minute" -> { value -> value * 60 }
    "second" -> { value -> value }
    else -> { value -> value }
}

fun main() {
    val timesInMinutes = listOf(2, 10, 15, 1)
    val min2sec = toSeconds("minute")
    val totalTimeInSeconds = timesInMinutes.map(min2sec).sum()
    println("Total time is $totalTimeInSeconds secs")
    // Total time is 1680 secs
}
```
{kotlin-runnable="true" id="kotlin-tour-lambda-return-from-function"}

### Invocar isoladamente {id="invoke-separately"}

Expressões lambda podem ser invocadas por conta própria, adicionando parênteses `()` depois das chaves `{}` e incluindo
os parâmetros dentro dos parênteses:

```kotlin
fun main() {
    //sampleStart
    println({ text: String -> text.uppercase() }("hello"))
    // HELLO
    //sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-lambda-standalone"}

### Lambdas finais {id="trailing-lambdas"}

Como você já viu, se uma expressão lambda for o único parâmetro da função, você pode omitir os parênteses `()` da função.
Se uma expressão lambda for passada como o último parâmetro de uma função, a expressão pode ser escrita fora dos
parênteses `()` da função. Nos dois casos, essa sintaxe se chama **lambda final** (_trailing lambda_).

Por exemplo, a função [`.fold()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/fold.html) aceita um
valor inicial e uma operação:

```kotlin
fun main() {
    //sampleStart
    // The initial value is zero. 
    // The operation sums the initial value with every item in the list cumulatively.
    println(listOf(1, 2, 3).fold(0, { x, item -> x + item })) // 6

    // Alternatively, in the form of a trailing lambda
    println(listOf(1, 2, 3).fold(0) { x, item -> x + item })  // 6
    //sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-trailing-lambda"}

Para mais informações sobre expressões lambda, veja [Expressões lambda e funções anônimas](lambdas.md#lambda-expressions-and-anonymous-functions).

O próximo passo do nosso tour é aprender sobre [classes](kotlin-tour-classes.md) em Kotlin.

## Prática: expressões lambda {id="practice-lambda-expressions" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Monte uma lista de URLs usando uma expressão lambda" id="lambdas-exercise-1">

Você tem uma lista de ações que um serviço web aceita, um prefixo comum para todas as requisições e o ID de um recurso específico.
Para requisitar uma ação `title` sobre o recurso com ID 5, você precisa criar a seguinte URL: `https://example.com/book-info/5/title`.
Use uma expressão lambda para criar uma lista de URLs a partir da lista de ações.

```kotlin
fun buildUrls(actions: List<String>, prefix: String, id: Int): List<String> {
    return TODO() // Write your code here
}

fun main() {
    val actions = listOf("title", "year", "author")
    val urls = buildUrls(actions, "https://example.com/book-info", 5)
    println(urls)
}
```
{validate="false" kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/LambdasExercise1Test.kt" id="kotlin-tour-lambdas-exercise-1"}

```kotlin
fun buildUrls(actions: List<String>, prefix: String, id: Int): List<String> {
    return actions.map { action -> "$prefix/$id/$action" }
}

fun main() {
    val actions = listOf("title", "year", "author")
    val urls = buildUrls(actions, "https://example.com/book-info", 5)
    println(urls)
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/LambdasExercise1Test.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-lambdas-solution-1"}

</def>
<def title="Repita uma ação várias vezes" id="lambdas-exercise-2">

Escreva uma função que recebe um valor `Int` e uma ação (uma função do tipo `() -> Unit`), que então repete a
ação o número de vezes informado. Depois, use essa função para imprimir “Hello” 5 vezes.

```kotlin
fun repeatN(n: Int, action: () -> Unit) {
    // Write your code here
}

fun main() {
    // Write your code here
}
```
{validate="false" kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/LambdasExercise2Test.kt" id="kotlin-tour-lambdas-exercise-2"}

```kotlin
fun repeatN(n: Int, action: () -> Unit) {
    for (i in 1..n) {
        action()
    }
}

fun main() {
    repeatN(5) {
        println("Hello")
    }
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/LambdasExercise2Test.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-lambdas-solution-2"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-control-flow.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-classes.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->
