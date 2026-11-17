[//]: # (title: Controle de fluxo)

<no-index/>


Assim como outras linguagens de programação, o Kotlin consegue tomar decisões conforme um trecho de código seja verdadeiro ou não. Esses trechos de código são chamados de **expressões condicionais**. O Kotlin também consegue criar e percorrer
laços de repetição.

## Expressões condicionais {id="conditional-expressions"}

O Kotlin oferece `if` e `when` para verificar expressões condicionais. 

> Se você precisar escolher entre `if` e `when`, recomendamos usar `when`, porque ele:
> 
> * Deixa seu código mais fácil de ler.
> * Facilita adicionar outro ramo.
> * Gera menos erros no código.
> 
{style="note"}

### If

Para usar `if`, coloque a expressão condicional entre parênteses `()` e a ação a ser executada caso o resultado seja verdadeiro
entre chaves `{}`:

```kotlin
fun main() {
//sampleStart
    val d: Int
    val check = true

    if (check) {
        d = 1
    } else {
        d = 2
    }

    println(d)
    // 1
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-if"}

O Kotlin não tem o operador ternário `condition ? then : else`. Em vez disso, `if` pode ser usado como expressão. Se houver
apenas uma linha de código por ação, as chaves `{}` são opcionais:

```kotlin
fun main() { 
//sampleStart
    val a = 1
    val b = 2

    println(if (a > b) a else b) // Returns a value: 2
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-if-expression"}

### When

Use `when` quando você tiver uma expressão condicional com vários ramos.

Para usar `when`:

* Coloque o valor que você quer avaliar entre parênteses `()`.
* Coloque os ramos entre chaves `{}`.
* Use `->` em cada ramo para separar cada verificação da ação a ser executada se a verificação for bem-sucedida.

`when` pode ser usado como **instrução** ou como expressão. Uma instrução não retorna nada, mas executa ações.

Veja um exemplo de uso de `when` como instrução:

```kotlin
fun main() {
//sampleStart
    val obj = "Hello"

    when (obj) {
        // Checks whether obj equals to "1"
        "1" -> println("One")
        // Checks whether obj equals to "Hello"
        "Hello" -> println("Greeting")
        // Default statement
        else -> println("Unknown")     
    }
    // Greeting
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-when-statement"}

> Observe que todas as condições dos ramos são verificadas em sequência até que uma delas seja satisfeita. Assim, apenas o primeiro
> ramo adequado é executado.
>
{style="note"}

Uma **expressão** retorna um valor que pode ser usado depois no código.

Veja um exemplo de uso de `when` como expressão. A expressão `when` é atribuída imediatamente a uma variável, que é usada
depois com a função `println()`:

```kotlin
fun main() {
//sampleStart    
    val obj = "Hello"    
    
    val result = when (obj) {
        // If obj equals "1", sets result to "one"
        "1" -> "One"
        // If obj equals "Hello", sets result to "Greeting"
        "Hello" -> "Greeting"
        // Sets result to "Unknown" if no previous condition is satisfied
        else -> "Unknown"
    }
    println(result)
    // Greeting
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-when-expression"}

Os exemplos de `when` que você viu até agora tinham um sujeito: `obj`. Mas `when` também pode ser usado sem sujeito.

Este exemplo usa uma expressão `when` **sem** sujeito para verificar uma cadeia de expressões booleanas:

```kotlin
fun main() {
    val trafficLightState = "Red" // This can be "Green", "Yellow", or "Red"

    val trafficAction = when {
        trafficLightState == "Green" -> "Go"
        trafficLightState == "Yellow" -> "Slow down"
        trafficLightState == "Red" -> "Stop"
        else -> "Malfunction"
    }

    println(trafficAction)
    // Stop
}
```
{kotlin-runnable="true" id="kotlin-tour-when-expression-boolean"}

No entanto, você pode ter o mesmo código com `trafficLightState` como sujeito:

```kotlin
fun main() {
    val trafficLightState = "Red" // This can be "Green", "Yellow", or "Red"

    val trafficAction = when (trafficLightState) {
        "Green" -> "Go"
        "Yellow" -> "Slow down"
        "Red" -> "Stop"
        else -> "Malfunction"
    }

    println(trafficAction)  
    // Stop
}
```
{kotlin-runnable="true" id="kotlin-tour-when-expression-boolean-subject"}

Usar `when` com um sujeito deixa seu código mais fácil de ler e de manter. Quando você usa um sujeito em uma expressão `when`,
o Kotlin também ajuda a verificar se todos os casos possíveis estão cobertos. Caso contrário, se você não usar um sujeito em uma
expressão `when`, precisa fornecer um ramo `else`.

## Prática: expressões condicionais {id="practice-conditional-expressions"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Verifique se dois dados dão o mesmo resultado" id="conditional-expressions-exercise-1">

Crie um jogo simples em que você ganha se, ao jogar dois dados, o resultado for o mesmo número. Use `if` para imprimir `You win :)`
se os dados baterem ou `You lose :(` caso contrário.

> Neste exercício, você importa um pacote para usar a função `Random.nextInt()`, que retorna um `Int` aleatório.
> Para mais informações sobre como importar pacotes, veja [Pacotes e imports](packages.md).
>
{style="tip"}

<deflist collapsible="true">
    <def title="Dica">
        Use o <a href="operator-overloading.md#equality-and-inequality-operators">operador de igualdade</a> (<code>==</code>) para comparar os resultados dos dados. 
    </def>
</deflist>

```kotlin
import kotlin.random.Random

fun main() {
    val firstResult = Random.nextInt(6)
    val secondResult = Random.nextInt(6)
    // Write your code here
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/ControlFlowConditionalExercise1Test.kt" validate="false" id="kotlin-tour-control-flow-conditional-exercise-1"}

```kotlin
import kotlin.random.Random

fun main() {
    val firstResult = Random.nextInt(6)
    val secondResult = Random.nextInt(6)
    if (firstResult == secondResult)
        println("You win :)")
    else
        println("You lose :(")
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/ControlFlowConditionalExercise1Test.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-control-flow-conditional-solution-1"}

</def>
<def title="Imprima a ação de um botão de console de videogame" id="conditional-expressions-exercise-2">

Usando uma expressão `when`, atualize o programa a seguir para que ele imprima a ação correspondente a qualquer botão de
console de videogame da tabela. O valor inicial de `button` é `"A"`, mas você pode mudá-lo para testar outros botões.

| **Botão** | **Ação**                |
|-----------|-------------------------|
| A         | Sim                     |
| B         | Não                     |
| X         | Menu                    |
| Y         | Nada                    |
| Outro     | Não existe esse botão   |

```kotlin
var button = "A"

fun main() {
    println(
        // Write your code here
    )
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/ControlFlowConditionalExercise2Test.kt" validate="false" id="kotlin-tour-control-flow-conditional-exercise-2"}

```kotlin
var button = "A"

fun main() {
    println(
        when (button) {
            "A" -> "Yes"
            "B" -> "No"
            "X" -> "Menu"
            "Y" -> "Nothing"
            else -> "There is no such button"
        }
    )
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/ControlFlowConditionalExercise2Test.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-control-flow-conditional-solution-2"}

</def>
</deflist>

## Intervalos {id="ranges"}

Antes de falar sobre laços de repetição, é útil saber como construir intervalos sobre os quais os laços vão iterar.

A forma mais comum de criar um intervalo no Kotlin é usar o operador `..`. Por exemplo, `1..4` é equivalente a `1, 2, 3, 4`.

Para declarar um intervalo que não inclui o valor final, use o operador `..<`. Por exemplo, `1..<4` é equivalente a `1, 2, 3`.

Para declarar um intervalo em ordem decrescente, use [`downTo`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/down-to.html). Por exemplo, `4 downTo 1` é equivalente a `4, 3, 2, 1`.

Para declarar um intervalo que incrementa em um passo diferente de 1, use [`step`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/step.html) e o valor de incremento desejado.
Por exemplo, `1..5 step 2` é equivalente a `1, 3, 5`.

Você também pode fazer o mesmo com intervalos de `Char`:

* `'a'..'d'` é equivalente a `'a', 'b', 'c', 'd'`
* `'z' downTo 's' step 2` é equivalente a `'z', 'x', 'v', 't'`

## Laços de repetição {id="loops"}

As duas estruturas de laço mais comuns na programação são `for` e `while`. Use `for` para percorrer um intervalo de
valores e executar uma ação. Use `while` para continuar uma ação até que uma condição específica seja satisfeita.

### For

Usando o que você acabou de aprender sobre intervalos, você pode criar um laço `for` que percorre os números de 1 a 5 e imprime
o número a cada iteração.

Coloque o iterador e o intervalo entre parênteses `()`, com a palavra-chave `in`. Adicione a ação que você quer executar entre
chaves `{}`:

```kotlin
fun main() {
//sampleStart
    for (number in 1..5) { 
        // number is the iterator and 1..5 is the range
        print(number)
    }
    // 12345
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-for-loop"}

Coleções também podem ser percorridas por laços:

```kotlin
fun main() { 
//sampleStart
    val cakes = listOf("carrot", "cheese", "chocolate")

    for (cake in cakes) {
        println("Yummy, it's a $cake cake!")
    }
    // Yummy, it's a carrot cake!
    // Yummy, it's a cheese cake!
    // Yummy, it's a chocolate cake!
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-for-collection-loop"}

### While

`while` pode ser usado de duas formas:

  * Para executar um bloco de código enquanto uma expressão condicional for verdadeira. (`while`)
  * Para executar o bloco de código primeiro e só depois verificar a expressão condicional. (`do-while`)

No primeiro caso de uso (`while`):

* Declare a expressão condicional para o laço while continuar, entre parênteses `()`. 
* Adicione a ação que você quer executar entre chaves `{}`.

> Os exemplos a seguir usam o [operador de incremento](operator-overloading.md#increments-and-decrements) `++` para
> incrementar o valor da variável `cakesEaten`.
>
{style="tip"}

```kotlin
fun main() {
//sampleStart
    var cakesEaten = 0
    while (cakesEaten < 3) {
        println("Eat a cake")
        cakesEaten++
    }
    // Eat a cake
    // Eat a cake
    // Eat a cake
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-while-loop"}

No segundo caso de uso (`do-while`):

* Declare a expressão condicional para o laço while continuar, entre parênteses `()`.
* Defina a ação que você quer executar entre chaves `{}`, com a palavra-chave `do`.

```kotlin
fun main() {
//sampleStart
    var cakesEaten = 0
    var cakesBaked = 0
    while (cakesEaten < 3) {
        println("Eat a cake")
        cakesEaten++
    }
    do {
        println("Bake a cake")
        cakesBaked++
    } while (cakesBaked < cakesEaten)
    // Eat a cake
    // Eat a cake
    // Eat a cake
    // Bake a cake
    // Bake a cake
    // Bake a cake
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-while-do-loop"}

Para mais informações e exemplos de expressões condicionais e laços, veja [Condições e laços](control-flow.md).

Agora que você conhece os fundamentos do controle de fluxo no Kotlin, é hora de aprender a escrever suas próprias [funções](kotlin-tour-functions.md).

## Prática: laços de repetição {id="practice-loops" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Conte fatias de pizza com laços while e do-while" id="loops-exercise-1">

Você tem um programa que conta fatias de pizza até haver uma pizza inteira, com 8 fatias. Refatore esse programa de duas formas:

* Use um laço `while`.
* Use um laço `do-while`.

```kotlin
fun main() {
    var pizzaSlices = 0
    // Start refactoring here
    pizzaSlices++
    println("There's only $pizzaSlices slice/s of pizza :(")
    pizzaSlices++
    println("There's only $pizzaSlices slice/s of pizza :(")
    pizzaSlices++
    println("There's only $pizzaSlices slice/s of pizza :(")
    pizzaSlices++
    println("There's only $pizzaSlices slice/s of pizza :(")
    pizzaSlices++
    println("There's only $pizzaSlices slice/s of pizza :(")
    pizzaSlices++
    println("There's only $pizzaSlices slice/s of pizza :(")
    pizzaSlices++
    println("There's only $pizzaSlices slice/s of pizza :(")
    pizzaSlices++
    // End refactoring here
    println("There are $pizzaSlices slices of pizza. Hooray! We have a whole pizza! :D")
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/ControlFlowLoopsExercise1Test.kt" validate="false" id="kotlin-tour-control-flow-loops-exercise-1"}

```kotlin
fun main() {
    var pizzaSlices = 0
    while ( pizzaSlices < 7 ) {
        pizzaSlices++
        println("There's only $pizzaSlices slice/s of pizza :(")
    }
    pizzaSlices++
    println("There are $pizzaSlices slices of pizza. Hooray! We have a whole pizza! :D")
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/ControlFlowLoopsExercise1Test.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo 1" id="kotlin-tour-control-flow-loops-exercise-1-solution-1"}

```kotlin
fun main() {
    var pizzaSlices = 0
    pizzaSlices++
    do {
        println("There's only $pizzaSlices slice/s of pizza :(")
        pizzaSlices++
    } while ( pizzaSlices < 8 )
    println("There are $pizzaSlices slices of pizza. Hooray! We have a whole pizza! :D")
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/ControlFlowLoopsExercise1Test.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo 2" id="kotlin-tour-control-flow-loops-exercise-1-solution-2"}

</def>
<def title="Jogue Fizz buzz" id="loops-exercise-2">

Escreva um programa que simule o jogo [Fizz buzz](https://en.wikipedia.org/wiki/Fizz_buzz). Sua tarefa é imprimir os
números de 1 a 100 em ordem crescente, substituindo qualquer número divisível por três pela palavra "fizz" e qualquer número
divisível por cinco pela palavra "buzz". Qualquer número divisível por 3 e por 5 deve ser substituído pela palavra "fizzbuzz".

<deflist collapsible="true">
    <def title="Dica 1">
        Use um laço <code>for</code> para contar os números e uma expressão <code>when</code> para decidir o que imprimir em cada
        passo. 
    </def>
</deflist>

<deflist collapsible="true">
    <def title="Dica 2">
        Use o operador de módulo (<code>%</code>) para retornar o resto da divisão de um número. Use o <a href="operator-overloading.md#equality-and-inequality-operators">operador de igualdade</a> 
        (<code>==</code>) para verificar se o resto é igual a zero.
    </def>
</deflist>

```kotlin
fun main() {
    // Write your code here
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/ControlFlowLoopsExercise2Test.kt" validate="false" id="kotlin-tour-control-flow-loops-exercise-2"}

```kotlin
fun main() {
    for (number in 1..100) {
        println(
            when {
                number % 15 == 0 -> "fizzbuzz"
                number % 3 == 0 -> "fizz"
                number % 5 == 0 -> "buzz"
                else -> "$number"
            }
        )
    }
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/ControlFlowLoopsExercise2Test.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-control-flow-loops-solution-2"}

</def>
<def title="Imprima as palavras que começam com uma letra" id="loops-exercise-3">

Você tem uma lista de palavras. Use `for` e `if` para imprimir apenas as palavras que começam com a letra `l`.

<deflist collapsible="true">
    <def title="Dica">
        Use a função <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/starts-with.html"> <code>.startsWith()</code>
        </a> do tipo <code>String</code>. 
    </def>
</deflist>

```kotlin
fun main() {
    val words = listOf("dinosaur", "limousine", "magazine", "language")
    // Write your code here
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/ControlFlowLoopsExercise3Test.kt" validate="false" id="kotlin-tour-control-flow-loops-exercise-3"}

```kotlin
fun main() {
    val words = listOf("dinosaur", "limousine", "magazine", "language")
    for (w in words) {
        if (w.startsWith("l"))
            println(w)
    }
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/ControlFlowLoopsExercise3Test.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-control-flow-loops-solution-3"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-collections.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-functions.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->
