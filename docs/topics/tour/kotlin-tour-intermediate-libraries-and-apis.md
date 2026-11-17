[//]: # (title: Bibliotecas e APIs)

<no-index/>


Para aproveitar ao máximo o Kotlin, use bibliotecas e APIs existentes para que você passe mais tempo programando e menos tempo reinventando a roda.

As bibliotecas distribuem código reutilizável que simplifica tarefas comuns. Dentro das bibliotecas, há pacotes e objetos que agrupam classes, funções e utilitários relacionados. As bibliotecas expõem APIs (Application Programming Interfaces) como um conjunto de funções, classes ou propriedades que os desenvolvedores podem usar no código deles.

![Bibliotecas e APIs do Kotlin](kotlin-library-diagram.svg){width=600}

Vamos explorar o que é possível com o Kotlin.

## A biblioteca padrão {id="the-standard-library"}

O Kotlin tem uma biblioteca padrão que fornece tipos, funções, coleções e utilitários essenciais para tornar seu código conciso e expressivo. Grande parte da biblioteca padrão (tudo que está no [pacote `kotlin`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/)) está disponível em qualquer arquivo Kotlin sem a necessidade de importação explícita:

```kotlin
fun main() {
    val text = "emosewa si niltoK"
    
   // Use the reversed() function from the standard library
    val reversedText = text.reversed()

    // Use the print() function from the standard library
    print(reversedText)
    // Kotlin is awesome
}
```
{kotlin-runnable="true" id="kotlin-tour-libraries-stdlib"}

No entanto, algumas partes da biblioteca padrão exigem uma importação antes de você poder usá-las no seu código.
Por exemplo, se você quiser usar os recursos de medição de tempo da biblioteca padrão, precisa importar o [pacote `kotlin.time`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/).

No início do seu arquivo, adicione a palavra-chave `import` seguida do pacote de que você precisa:

```kotlin
import kotlin.time.*
```

O asterisco `*` é uma importação curinga que diz ao Kotlin para importar tudo dentro do pacote. Você não pode usar o asterisco `*` com companion objects.
Em vez disso, você precisa declarar explicitamente os membros de um companion object que quer usar.

Por exemplo:

```kotlin
import kotlin.time.Duration
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.minutes

fun main() {
    val thirtyMinutes: Duration = 30.minutes
    val halfHour: Duration = 0.5.hours
    println(thirtyMinutes == halfHour)
    // true
}
```
{kotlin-runnable="true" id="kotlin-tour-libraries-time"}

Este exemplo:

* Importa a classe `Duration` e as propriedades de extensão `hours` e `minutes` do seu companion object.
* Usa a propriedade `minutes` para converter `30` em uma `Duration` de 30 minutos.
* Usa a propriedade `hours` para converter `0.5` em uma `Duration` de 30 minutos.
* Verifica se as duas durações são iguais e imprime o resultado.

### Pesquise antes de criar {id="search-before-you-build"}

Antes de decidir escrever seu próprio código, verifique se o que você procura já existe na biblioteca padrão.
Veja a seguir uma lista de áreas em que a biblioteca padrão já oferece várias classes, funções e propriedades para você:

* [Coleções](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/)
* [Sequências](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/)
* [Manipulação de strings](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/)
* [Gerenciamento de tempo](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/)

Para saber mais sobre o que mais há na biblioteca padrão, explore a [referência da API](https://kotlinlang.org/api/core/kotlin-stdlib/).

## Bibliotecas do Kotlin {id="kotlin-libraries"}

A biblioteca padrão cobre muitos casos de uso comuns, mas há alguns que ela não aborda. Felizmente, a equipe do Kotlin e o restante da comunidade desenvolveram uma ampla variedade de bibliotecas para complementar a biblioteca padrão. Por exemplo, a [`kotlinx-datetime`](https://kotlinlang.org/api/kotlinx-datetime/) ajuda você a gerenciar o tempo em diferentes plataformas.

Você pode encontrar bibliotecas úteis na nossa [plataforma de busca](https://klibs.io/). Para usá-las, você precisa seguir passos extras, como adicionar uma dependência ou plugin. Cada biblioteca tem um repositório no GitHub com instruções sobre como incluí-la nos seus projetos Kotlin.

Depois de adicionar a biblioteca, você pode importar qualquer pacote dela. Veja um exemplo de como importar o pacote `kotlinx-datetime` para descobrir a hora atual em Nova York:

```kotlin
import kotlinx.datetime.*

fun main() {
    val now = Clock.System.now() // Get current instant
    println("Current instant: $now")

    val zone = TimeZone.of("America/New_York")
    val localDateTime = now.toLocalDateTime(zone)
    println("Local date-time in NY: $localDateTime")
}
```
{kotlin-runnable="true" id="kotlin-tour-libraries-datetime"}

Este exemplo:

* Importa o pacote `kotlinx.datetime`.
* Usa a função `Clock.System.now()` para criar uma instância da classe `Instant`, que contém a hora atual, e atribui o resultado à variável `now`.
* Imprime a hora atual.
* Usa a função `TimeZone.of()` para encontrar o fuso horário de Nova York e atribui o resultado à variável `zone`.
* Chama a função `.toLocalDateTime()` na instância que contém a hora atual, com o fuso horário de Nova York como argumento.
* Atribui o resultado à variável `localDateTime`.
* Imprime a hora ajustada para o fuso horário de Nova York.

> Para explorar em mais detalhes as funções e classes usadas neste exemplo, consulte a [referência da API](https://kotlinlang.org/api/kotlinx-datetime/kotlinx-datetime/kotlinx.datetime/).
>
{style="tip"}

## Faça opt-in em APIs {id="opt-in-to-apis"}

Autores de bibliotecas podem marcar certas APIs como exigindo opt-in antes que você possa usá-las no seu código. Normalmente, eles fazem isso quando uma
API ainda está em desenvolvimento e pode mudar no futuro. Se você não fizer opt-in, verá avisos ou erros como este:

```text
This declaration needs opt-in. Its usage should be marked with '@...' or '@OptIn(...)'
```

Para fazer opt-in, escreva `@OptIn` seguido de parênteses contendo o nome da classe que categoriza a API, acrescido de dois-pontos duplos `::` e `class`.

Por exemplo, a função `uintArrayOf()` da biblioteca padrão pertence a `@ExperimentalUnsignedTypes`, como mostrado
[na referência da API](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-u-int-array.html):

```kotlin
@ExperimentalUnsignedTypes
inline fun uintArrayOf(vararg elements: UInt): UIntArray
```

No código, o opt-in fica assim:

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
```

Aqui está um exemplo que faz opt-in para usar a função `uintArrayOf()` a fim de criar um array de inteiros sem sinal e modificar um dos seus elementos:

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    // Create an unsigned integer array
    val unsignedArray: UIntArray = uintArrayOf(1u, 2u, 3u, 4u, 5u)

    // Modify an element
    unsignedArray[2] = 42u
    println("Updated array: ${unsignedArray.joinToString()}")
    // Updated array: 1, 2, 42, 4, 5
}
```
{kotlin-runnable="true" id="kotlin-tour-libraries-apis"}

Esta é a forma mais fácil de fazer opt-in, mas existem outras. Para saber mais, consulte [Requisitos de opt-in](opt-in-requirements.md).

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Calcule os juros compostos" id="libraries-exercise-1">

Você está desenvolvendo um app financeiro que ajuda os usuários a calcular o valor futuro de seus investimentos. A fórmula
para calcular juros compostos é:

<math>A = P \times (1 + \displaystyle\frac{r}{n})^{nt}</math>

Onde:

* `A` é o montante acumulado após os juros (principal + juros).
* `P` é o valor principal (o investimento inicial).
* `r` é a taxa de juros anual (decimal).
* `n` é o número de vezes que os juros são capitalizados por ano.
* `t` é o tempo, em anos, pelo qual o dinheiro é investido.

Atualize o código para:

1. Importar as funções necessárias do [pacote `kotlin.math`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/).
2. Adicionar um corpo à função `calculateCompoundInterest()` que calcula o montante final após aplicar os juros compostos.

```kotlin
// Write your code here

fun calculateCompoundInterest(P: Double, r: Double, n: Int, t: Int): Double {
    // Write your code here
}

fun main() {
    val principal = 1000.0
    val rate = 0.05
    val timesCompounded = 4
    val years = 5
    val amount = calculateCompoundInterest(principal, rate, timesCompounded, years)
    println("The accumulated amount is: $amount")
    // The accumulated amount is: 1282.0372317085844
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/CalculateCompoundInterestTest.kt" validate="false" id="kotlin-tour-libraries-exercise-1"}

```kotlin
import kotlin.math.*

fun calculateCompoundInterest(P: Double, r: Double, n: Int, t: Int): Double {
    return P * (1 + r / n).pow(n * t)
}

fun main() {
    val principal = 1000.0
    val rate = 0.05
    val timesCompounded = 4
    val years = 5
    val amount = calculateCompoundInterest(principal, rate, timesCompounded, years)
    println("The accumulated amount is: $amount")
    // The accumulated amount is: 1282.0372317085844
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/CalculateCompoundInterestTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-libraries-solution-1"}

</def>
<def title="Meça o tempo gasto no processamento de dados" id="libraries-exercise-2">

Você quer medir o tempo que leva para executar várias tarefas de processamento de dados no seu programa. Atualize o código
para adicionar as instruções de importação corretas e as funções do pacote [`kotlin.time`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/):

```kotlin
// Write your code here

fun main() {
    val timeTaken = /* Write your code here */ {
        // Simulate some data processing
        val data = List(1000) { it * 2 }
        val filteredData = data.filter { it % 3 == 0 }

        // Simulate processing the filtered data
        val processedData = filteredData.map { it / 2 }
        println("Processed data")
    }

    println("Time taken: $timeTaken") // e.g. 16 ms
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/MeasureTimeTest.kt" validate="false" id="kotlin-tour-libraries-exercise-2"}

```kotlin
import kotlin.time.measureTime

fun main() {
    val timeTaken = measureTime {
        // Simulate some data processing
        val data = List(1000) { it * 2 }
        val filteredData = data.filter { it % 3 == 0 }

        // Simulate processing the filtered data
        val processedData = filteredData.map { it / 2 }
        println("Processed data")
    }

    println("Time taken: $timeTaken") // e.g. 16 ms
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/MeasureTimeTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-libraries-solution-2"}

</def>
<def title="Faça opt-in em uma API experimental" id="libraries-exercise-3">

Há um novo recurso na biblioteca padrão disponível na versão mais recente do Kotlin. Você quer testá-lo, mas ele exige opt-in.
O recurso pertence a [`@ExperimentalStdlibApi`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-experimental-stdlib-api/).
Como deve ser o opt-in no seu código?

```kotlin
@OptIn(ExperimentalStdlibApi::class)
```
{initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-libraries-solution-3"}

</def>
</deflist>

## Próximos passos {id="what-s-next"}

Parabéns! Você concluiu o tour intermediário! Gostaria de [compartilhar seu feedback](https://surveys.hotjar.com/bf4ce865-99ce-4fc1-b107-e9b16bc31592) sobre sua experiência?

Como próximo passo, confira nossos tutoriais de apps populares em Kotlin:

<p></p> <!-- workaround for MRK057: Paragraph can only contain inline elements -->
<panels columns="2" id="kotlin-tour-whats-next">
    <panel>
        <title>Kotlin para backend</title>
        <p>Crie um app de backend com Spring Boot e Kotlin.</p>
        <a href="jvm-create-project-with-spring-boot.md" as="button" icon="arrow-right" icon-position="right" id="kotlin-tour-backend-tutorial">Começar</a>
    </panel>
    <panel>
        <title>Kotlin Multiplatform</title>
        <p>Crie um app multiplataforma do zero e compartilhe a lógica de negócio e a UI.</p>
        <a href="https://kotlinlang.org/docs/multiplatform/compose-multiplatform-new-project.html" as="button" icon="arrow-right" icon-position="right" id="kotlin-tour-cmp-tutorial">Começar</a>
    </panel>
</panels>

<seealso></seealso>

<list id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-intermediate-null-safety.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
</list>

<!-- ia-translate: true -->
