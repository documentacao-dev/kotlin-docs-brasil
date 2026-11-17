[//]: # (title: Olá, mundo)

<no-index/>


Aqui está um programa simples que imprime "Hello, world!":

```kotlin
fun main() {
    println("Hello, world!")
    // Hello, world!
}
```
{kotlin-runnable="true" id="hello-world-kotlin"}

Em Kotlin:

* `fun` é usado para declarar uma função
* A função `main()` é onde o programa começa
* O corpo de uma função é escrito entre chaves `{}`
* As funções [`println()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.io/println.html) e [`print()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.io/print.html) imprimem seus argumentos na saída padrão

Uma função é um conjunto de instruções que executa uma tarefa específica. Depois de criar uma função, você pode usá-la sempre que precisar executar essa tarefa, sem precisar escrever as instruções de novo. Falaremos mais sobre funções daqui a alguns capítulos. Até lá, todos os exemplos usam a função `main()`.

## Variáveis {id="variables"}

Todos os programas precisam armazenar dados, e as variáveis ajudam você a fazer exatamente isso. Em Kotlin, você pode declarar:

* Variáveis somente leitura com `val`
* Variáveis mutáveis com `var`

> Você não pode alterar uma variável somente leitura depois de atribuir um valor a ela.
>
{style="note"}

Para atribuir um valor, use o operador de atribuição `=`.

Por exemplo:

```kotlin
fun main() { 
//sampleStart
    val popcorn = 5    // There are 5 boxes of popcorn
    val hotdog = 7     // There are 7 hotdogs
    var customers = 10 // There are 10 customers in the queue
    
    // Some customers leave the queue
    customers = 8
    println(customers)
    // 8
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-variables"}

> As variáveis podem ser declaradas fora da função `main()`, no início do programa. Variáveis declaradas assim ficam no **nível superior** (top level).
> 
{style="tip"}

Como `customers` é uma variável mutável, dá para reatribuir o valor dela depois da declaração.

> Recomendamos declarar todas as variáveis como somente leitura (`val`) por padrão. Use variáveis mutáveis (`var`) apenas quando realmente precisar. Assim, é menos provável que você altere sem querer algo que não deveria mudar.
> 
{style="note"}

## Templates de string {id="string-templates"}

É útil saber como imprimir o conteúdo de variáveis na saída padrão. Você pode fazer isso com **templates de string**.
Você pode usar expressões de template para acessar dados armazenados em variáveis e outros objetos e convertê-los em strings.
Um valor string é uma sequência de caracteres entre aspas duplas `"`. Expressões de template sempre começam com um cifrão `$`.

Para avaliar um trecho de código em uma expressão de template, coloque o código entre chaves `{}` depois do cifrão `$`.

Por exemplo:

```kotlin
fun main() { 
//sampleStart
    val customers = 10
    println("There are $customers customers")
    // There are 10 customers
    
    println("There are ${customers + 1} customers")
    // There are 11 customers
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-string-templates"}

Para mais informações, consulte [Templates de string](strings.md#string-templates).

Você vai notar que não há tipos declarados para as variáveis. O próprio Kotlin inferiu o tipo: `Int`. Este tour explica os diferentes tipos básicos do Kotlin e como declará-los no [próximo capítulo](kotlin-tour-basic-types.md).

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true">
<def title="Imprima uma frase usando templates de string" id="hello-world-exercise-1">

Complete o código para que o programa imprima `"Mary is 20 years old"` na saída padrão:

```kotlin
fun main() {
    val name = "Mary"
    val age = 20
    // Write your code here
}
```
{validate="false" kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/HelloWorldTest.kt" id="kotlin-tour-hello-world-exercise"}

```kotlin
fun main() {
    val name = "Mary"
    val age = 20
    println("$name is $age years old")
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/HelloWorldTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-hello-world-solution"}

</def>
</deflist>

<seealso></seealso>

<list id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-basic-types.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->
