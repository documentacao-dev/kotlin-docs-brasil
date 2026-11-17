[//]: # (title: Classes abertas e especiais)

<no-index/>


Neste capítulo, você vai aprender sobre classes abertas, como elas funcionam com interfaces e outros tipos especiais
de classes disponíveis em Kotlin.

## Classes abertas {id="open-classes"}

Se você não puder usar interfaces ou classes abstratas, pode tornar uma classe explicitamente herdável declarando-a
como **open**. Para isso, use a palavra-chave `open` antes da declaração da classe:

```kotlin
open class Vehicle(val make: String, val model: String)
```

Para criar uma classe que herda de outra, adicione dois-pontos depois do cabeçalho da classe, seguidos de uma chamada
ao construtor da classe pai da qual você quer herdar. Neste exemplo, a classe `Car` herda da classe `Vehicle`:

```kotlin
open class Vehicle(val make: String, val model: String)

class Car(make: String, model: String, val numberOfDoors: Int) : Vehicle(make, model)

fun main() {
    // Creates an instance of the Car class
    val car = Car("Toyota", "Corolla", 4)

    // Prints the details of the car
    println("Car Info: Make - ${car.make}, Model - ${car.model}, Number of doors - ${car.numberOfDoors}")
    // Car Info: Make - Toyota, Model - Corolla, Number of doors - 4
}
```
{kotlin-runnable="true" id="kotlin-tour-classes-open-class"}

Assim como ao criar uma instância de uma classe normal, se sua classe herda de uma classe pai, ela precisa inicializar
todos os parâmetros declarados no cabeçalho da classe pai. Então, no exemplo, a instância `car` da classe `Car` inicializa
os parâmetros da classe pai: `make` e `model`.

### Sobrescrever comportamentos herdados {id="overriding-inherited-behavior"}

Se você quer herdar de uma classe, mas mudar parte do comportamento, pode sobrescrever o comportamento herdado.

Por padrão, não é possível sobrescrever uma função ou propriedade membro da classe pai. Assim como nas classes abstratas,
você precisa adicionar palavras-chave especiais.

#### Funções membro {id="member-functions"}

Para permitir que uma função da classe pai seja sobrescrita, use a palavra-chave `open` antes da declaração dela na
classe pai:

```kotlin
open fun displayInfo() {}
```
{validate="false"}

Para sobrescrever uma função membro herdada, use a palavra-chave `override` antes da declaração da função na classe
filha:

```kotlin
override fun displayInfo() {}
```
{validate="false"}

Por exemplo:

```kotlin
open class Vehicle(val make: String, val model: String) {
    open fun displayInfo() {
        println("Vehicle Info: Make - $make, Model - $model")
    }
}

class Car(make: String, model: String, val numberOfDoors: Int) : Vehicle(make, model) {
    override fun displayInfo() {
        println("Car Info: Make - $make, Model - $model, Number of Doors - $numberOfDoors")
    }
}

fun main() {
    val car1 = Car("Toyota", "Corolla", 4)
    val car2 = Car("Honda", "Civic", 2)

    // Uses the overridden displayInfo() function
    car1.displayInfo()
    // Car Info: Make - Toyota, Model - Corolla, Number of Doors - 4
    car2.displayInfo()
    // Car Info: Make - Honda, Model - Civic, Number of Doors - 2
}
```
{kotlin-runnable="true" id="kotlin-tour-class-override-function"}

Este exemplo:

* Cria duas instâncias da classe `Car`, que herda da classe `Vehicle`: `car1` e `car2`.
* Sobrescreve a função `displayInfo()` na classe `Car` para também imprimir o número de portas.
* Chama a função `displayInfo()` sobrescrita nas instâncias `car1` e `car2`.

#### Propriedades {id="properties"}

Em Kotlin, não é prática comum tornar uma propriedade herdável usando a palavra-chave `open` e sobrescrevê-la depois.
Na maioria das vezes, você usa uma classe abstrata ou uma interface, em que as propriedades são herdáveis por padrão.

As propriedades dentro de classes abertas são acessíveis pela classe filha. Em geral, é melhor acessá-las diretamente
do que sobrescrevê-las com uma nova propriedade.

Por exemplo, suponha que você tenha uma propriedade chamada `transmissionType` que quer sobrescrever depois. A sintaxe
para sobrescrever propriedades é exatamente a mesma usada para funções membro. Você pode fazer assim:

```kotlin
open class Vehicle(val make: String, val model: String) {
    open val transmissionType: String = "Manual"
}

class Car(make: String, model: String, val numberOfDoors: Int) : Vehicle(make, model) {
    override val transmissionType: String = "Automatic"
}
```

No entanto, essa não é uma boa prática. Em vez disso, você pode adicionar a propriedade ao construtor da classe
herdável e declarar o valor dela ao criar a classe filha `Car`:

```kotlin
open class Vehicle(val make: String, val model: String, val transmissionType: String = "Manual")

class Car(make: String, model: String, val numberOfDoors: Int) : Vehicle(make, model, "Automatic")
```

Acessar propriedades diretamente, em vez de sobrescrevê-las, deixa o código mais simples e legível. Ao declarar as
propriedades uma vez na classe pai e passar os valores pelo construtor, você elimina a necessidade de sobrescritas
desnecessárias nas classes filhas.

Para mais informações sobre herança de classes e sobrescrita de comportamento, consulte [Herança](inheritance.md).

### Classes abertas e interfaces {id="open-classes-and-interfaces"}

Você pode criar uma classe que herda de uma classe **e** implementa várias interfaces. Nesse caso, você precisa declarar
a classe pai primeiro, depois dos dois-pontos, antes de listar as interfaces:

```kotlin
// Define interfaces
interface EcoFriendly {
    val emissionLevel: String
}

interface ElectricVehicle {
    val batteryCapacity: Double
}

// Parent class
open class Vehicle(val make: String, val model: String)

// Child class
open class Car(make: String, model: String, val numberOfDoors: Int) : Vehicle(make, model)

// New class that inherits from Car and implements two interfaces
class ElectricCar(
    make: String,
    model: String,
    numberOfDoors: Int,
    val capacity: Double,
    val emission: String
) : Car(make, model, numberOfDoors), EcoFriendly, ElectricVehicle {
    override val batteryCapacity: Double = capacity
    override val emissionLevel: String = emission
}
```

## Classes especiais {id="special-classes"}

Além de classes abstratas, abertas e de dados, Kotlin tem tipos especiais de classes projetados para diversas finalidades,
como restringir comportamentos específicos ou reduzir o impacto no desempenho ao criar objetos pequenos.

### Sealed classes

Às vezes, você quer restringir a herança. Isso pode ser feito com sealed classes. Sealed classes são um tipo especial de
[classe abstrata](kotlin-tour-intermediate-classes-interfaces.md#abstract-classes). Depois de declarar que uma classe é
sealed, você só pode criar classes filhas dela dentro do mesmo pacote. Não é possível herdar da sealed class fora desse escopo.

> Um pacote é uma coleção de código com classes e funções relacionadas, normalmente dentro de um diretório. Para saber
> mais sobre pacotes em Kotlin, consulte [Pacotes e importações](packages.md).
> 
{style="tip"}

Para criar uma sealed class, use a palavra-chave `sealed`:

```kotlin
sealed class Mammal
```

Sealed classes são especialmente úteis combinadas com uma expressão `when`. Usando uma expressão `when`, você pode
definir o comportamento para todas as classes filhas possíveis. Por exemplo:

```kotlin
sealed class Mammal(val name: String)

class Cat(val catName: String) : Mammal(catName)
class Human(val humanName: String, val job: String) : Mammal(humanName)

fun greetMammal(mammal: Mammal): String {
    when (mammal) {
        is Human -> return "Hello ${mammal.name}; You're working as a ${mammal.job}"
        is Cat -> return "Hello ${mammal.name}"   
    }
}

fun main() {
    println(greetMammal(Cat("Snowy")))
    // Hello Snowy
}
```
{kotlin-runnable="true" id="kotlin-tour-sealed-classes"}

No exemplo:

* Há uma sealed class chamada `Mammal` que tem o parâmetro `name` no construtor.
* A classe `Cat` herda da sealed class `Mammal` e usa o parâmetro `catName` do próprio construtor como o parâmetro `name` da classe `Mammal`.
* A classe `Human` herda da sealed class `Mammal` e usa o parâmetro `humanName` do próprio construtor como o parâmetro `name` da classe `Mammal`. Ela também tem o parâmetro `job` no construtor.
* A função `greetMammal()` aceita um argumento do tipo `Mammal` e retorna uma string.
* Dentro do corpo da função `greetMammal()`, há uma expressão `when` que usa o [operador `is`](typecasts.md#is-and-is-operators) para verificar o tipo de `mammal` e decidir qual ação executar.
* A função `main()` chama a função `greetMammal()` com uma instância da classe `Cat` e o parâmetro `name` com o valor `Snowy`.

> Este tour aborda o operador `is` com mais detalhes no capítulo [Null safety](kotlin-tour-intermediate-null-safety.md).
> 
{style ="tip"}

Para mais informações sobre sealed classes e seus casos de uso recomendados, consulte [Sealed classes e interfaces](sealed-classes.md).

### Enum classes

Enum classes são úteis quando você quer representar um conjunto finito de valores distintos em uma classe. Uma enum class
contém constantes de enum, que são, elas mesmas, instâncias da enum class.

Para criar uma enum class, use a palavra-chave `enum`:

```kotlin
enum class State
```

Imagine que você quer criar uma enum class que contém os diferentes estados de um processo. Cada constante de enum deve
ser separada por vírgula `,`:

```kotlin
enum class State {
    IDLE, RUNNING, FINISHED
}
```

A enum class `State` tem as constantes de enum `IDLE`, `RUNNING` e `FINISHED`. Para acessar uma constante de enum, use o
nome da classe seguido de `.` e o nome da constante:

```kotlin
val state = State.RUNNING
```

Você pode usar essa enum class com uma expressão `when` para definir a ação a tomar de acordo com o valor da constante de enum:

```kotlin
enum class State {
    IDLE, RUNNING, FINISHED
}

fun main() {
    val state = State.RUNNING
    val message = when (state) {
        State.IDLE -> "It's idle"
        State.RUNNING -> "It's running"
        State.FINISHED -> "It's finished"
    }
    println(message)
    // It's running
}
```
{kotlin-runnable="true" id="kotlin-tour-enum-classes"}

Enum classes podem ter propriedades e funções membro, assim como classes normais.

Por exemplo, imagine que você está trabalhando com HTML e quer criar uma enum class com algumas cores. Você quer que cada
cor tenha uma propriedade, vamos chamá-la de `rgb`, que contém o valor RGB dela em hexadecimal. Ao criar as constantes de
enum, você precisa inicializá-las com essa propriedade:

```kotlin
enum class Color(val rgb: Int) {
    RED(0xFF0000),
    GREEN(0x00FF00),
    BLUE(0x0000FF),
    YELLOW(0xFFFF00)
}
```

> O Kotlin armazena valores hexadecimais como inteiros, então a propriedade `rgb` tem o tipo `Int`, e não o tipo `String`.
>
{style="note"}

Para adicionar uma função membro a essa classe, separe-a das constantes de enum com um ponto e vírgula `;`:

```kotlin
enum class Color(val rgb: Int) {
    RED(0xFF0000),
    GREEN(0x00FF00),
    BLUE(0x0000FF),
    YELLOW(0xFFFF00);

    fun containsRed() = (this.rgb and 0xFF0000 != 0)
}

fun main() {
    val red = Color.RED
    
    // Calls containsRed() function on enum constant
    println(red.containsRed())
    // true

    // Calls containsRed() function on enum constants via class names
    println(Color.BLUE.containsRed())
    // false
  
    println(Color.YELLOW.containsRed())
    // true
}
```
{kotlin-runnable="true" id="kotlin-tour-interface-enum-classes-members"}

Neste exemplo, a função membro `containsRed()` acessa o valor da propriedade `rgb` da constante de enum usando a palavra-chave
`this` e verifica se o valor hexadecimal contém `FF` nos primeiros bits, para retornar um valor booleano.

Para mais informações, consulte [Enum classes](enum-classes.md).

### Inline value classes

Às vezes, você talvez queira criar pequenos objetos a partir de classes e usá-los só por um instante. Essa
abordagem pode ter impacto no desempenho. Inline value classes são um tipo especial de classe que evita esse impacto.
No entanto, elas só podem conter valores.

Para criar uma inline value class, use a palavra-chave `value` e a anotação `@JvmInline`:

```kotlin
@JvmInline
value class Email
```

> A anotação `@JvmInline` instrui o Kotlin a otimizar o código quando ele é compilado. Para saber mais,
> consulte [Anotações](annotations.md).
> 
{style="tip"}

Uma inline value class **precisa** ter uma única propriedade inicializada no cabeçalho da classe.

Imagine que você quer criar uma classe que armazena um endereço de e-mail:

```kotlin
// The address property is initialized in the class header.
@JvmInline
value class Email(val address: String)

fun sendEmail(email: Email) {
    println("Sending email to ${email.address}")
}

fun main() {
    val myEmail = Email("example@example.com")
    sendEmail(myEmail)
    // Sending email to example@example.com
}
```
{kotlin-runnable="true" id="kotlin-tour-inline-value-class"}

No exemplo:

* `Email` é uma inline value class que tem uma propriedade no cabeçalho da classe: `address`.
* A função `sendEmail()` aceita objetos do tipo `Email` e imprime uma string na saída padrão.
* A função `main()`:
    * Cria uma instância da classe `Email` chamada `myEmail`.
    * Chama a função `sendEmail()` no objeto `myEmail`.

Ao usar uma inline value class, você torna a classe inline e pode usá-la diretamente no código sem criar um objeto.
Isso pode reduzir significativamente o consumo de memória e melhorar o desempenho do código em tempo de execução.

Para mais informações sobre inline value classes, consulte [Inline value classes](inline-classes.md).

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Modele os status de entrega com uma sealed class" id="special-classes-exercise-1">

Você administra um serviço de entregas e precisa de uma forma de acompanhar o status dos pacotes. Crie uma sealed class
chamada `DeliveryStatus`, que contenha data classes para representar os seguintes status: `Pending`, `InTransit`,
`Delivered` e `Canceled`. Complete a declaração da classe `DeliveryStatus` para que o código da função `main()` rode
com sucesso:

```kotlin
sealed class // Write your code here

fun printDeliveryStatus(status: DeliveryStatus) {
    when (status) {
        is DeliveryStatus.Pending -> {
            println("The package is pending pickup from ${status.sender}.")
        }
        is DeliveryStatus.InTransit -> {
            println("The package is in transit and expected to arrive by ${status.estimatedDeliveryDate}.")
        }
        is DeliveryStatus.Delivered -> {
            println("The package was delivered to ${status.recipient} on ${status.deliveryDate}.")
        }
        is DeliveryStatus.Canceled -> {
            println("The delivery was canceled due to: ${status.reason}.")
        }
    }
}

fun main() {
    val status1: DeliveryStatus = DeliveryStatus.Pending("Alice")
    val status2: DeliveryStatus = DeliveryStatus.InTransit("2024-11-20")
    val status3: DeliveryStatus = DeliveryStatus.Delivered("2024-11-18", "Bob")
    val status4: DeliveryStatus = DeliveryStatus.Canceled("Address not found")

    printDeliveryStatus(status1)
    // The package is pending pickup from Alice.
    printDeliveryStatus(status2)
    // The package is in transit and expected to arrive by 2024-11-20.
    printDeliveryStatus(status3)
    // The package was delivered to Bob on 2024-11-18.
    printDeliveryStatus(status4)
    // The delivery was canceled due to: Address not found.
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/DeliveryStatusTest.kt" validate="false" id="kotlin-tour-special-classes-exercise-1"}

```kotlin
sealed class DeliveryStatus {
    data class Pending(val sender: String) : DeliveryStatus()
    data class InTransit(val estimatedDeliveryDate: String) : DeliveryStatus()
    data class Delivered(val deliveryDate: String, val recipient: String) : DeliveryStatus()
    data class Canceled(val reason: String) : DeliveryStatus()
}

fun printDeliveryStatus(status: DeliveryStatus) {
    when (status) {
        is DeliveryStatus.Pending -> {
            println("The package is pending pickup from ${status.sender}.")
        }
        is DeliveryStatus.InTransit -> {
            println("The package is in transit and expected to arrive by ${status.estimatedDeliveryDate}.")
        }
        is DeliveryStatus.Delivered -> {
            println("The package was delivered to ${status.recipient} on ${status.deliveryDate}.")
        }
        is DeliveryStatus.Canceled -> {
            println("The delivery was canceled due to: ${status.reason}.")
        }
    }
}

fun main() {
    val status1: DeliveryStatus = DeliveryStatus.Pending("Alice")
    val status2: DeliveryStatus = DeliveryStatus.InTransit("2024-11-20")
    val status3: DeliveryStatus = DeliveryStatus.Delivered("2024-11-18", "Bob")
    val status4: DeliveryStatus = DeliveryStatus.Canceled("Address not found")

    printDeliveryStatus(status1)
    // The package is pending pickup from Alice.
    printDeliveryStatus(status2)
    // The package is in transit and expected to arrive by 2024-11-20.
    printDeliveryStatus(status3)
    // The package was delivered to Bob on 2024-11-18.
    printDeliveryStatus(status4)
    // The delivery was canceled due to: Address not found.
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/DeliveryStatusTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-special-classes-solution-1"}

</def>
<def title="Defina tipos de problema com uma enum class" id="special-classes-exercise-2">

Em um programa, você quer tratar diferentes status e tipos de erro. Você tem uma sealed class para capturar os
diferentes status, que são declarados em data classes ou objects. Complete o código abaixo criando uma enum class chamada
`Problem` que representa os diferentes tipos de problema: `NETWORK`, `TIMEOUT` e `UNKNOWN`.

```kotlin
sealed class Status {
    data object Loading : Status()
    data class Error(val problem: Problem) : Status() {
        // Write your code here
    }

    data class OK(val data: List<String>) : Status()
}

fun handleStatus(status: Status) {
    when (status) {
        is Status.Loading -> println("Loading...")
        is Status.OK -> println("Data received: ${status.data}")
        is Status.Error -> when (status.problem) {
            Status.Error.Problem.NETWORK -> println("Network issue")
            Status.Error.Problem.TIMEOUT -> println("Request timed out")
            Status.Error.Problem.UNKNOWN -> println("Unknown error occurred")
        }
    }
}

fun main() {
    val status1: Status = Status.Error(Status.Error.Problem.NETWORK)
    val status2: Status = Status.OK(listOf("Data1", "Data2"))

    handleStatus(status1)
    // Network issue
    handleStatus(status2)
    // Data received: [Data1, Data2]
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/StatusProblemTest.kt" validate="false" id="kotlin-tour-special-classes-exercise-2"}

```kotlin
sealed class Status {
    data object Loading : Status()
    data class Error(val problem: Problem) : Status() {
        enum class Problem {
            NETWORK,
            TIMEOUT,
            UNKNOWN
        }
    }

    data class OK(val data: List<String>) : Status()
}

fun handleStatus(status: Status) {
    when (status) {
        is Status.Loading -> println("Loading...")
        is Status.OK -> println("Data received: ${status.data}")
        is Status.Error -> when (status.problem) {
            Status.Error.Problem.NETWORK -> println("Network issue")
            Status.Error.Problem.TIMEOUT -> println("Request timed out")
            Status.Error.Problem.UNKNOWN -> println("Unknown error occurred")
        }
    }
}

fun main() {
    val status1: Status = Status.Error(Status.Error.Problem.NETWORK)
    val status2: Status = Status.OK(listOf("Data1", "Data2"))

    handleStatus(status1)
    // Network issue
    handleStatus(status2)
    // Data received: [Data1, Data2]
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/StatusProblemTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-special-classes-solution-2"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-intermediate-objects.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-intermediate-properties.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->
