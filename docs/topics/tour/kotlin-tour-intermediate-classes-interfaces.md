[//]: # (title: Classes e interfaces)

<no-index/>


Na tour para iniciantes, você aprendeu a usar classes e data classes para armazenar dados e manter um conjunto de características que podem ser compartilhadas no código. Com o tempo, você vai querer criar uma hierarquia para compartilhar código de forma eficiente nos seus projetos. Este capítulo explica as opções que o Kotlin oferece para compartilhar código e como elas podem tornar seu código mais seguro e fácil de manter.

## Herança de classes {id="class-inheritance"}

Em um capítulo anterior, vimos como usar funções de extensão para estender classes sem modificar o código-fonte original. Mas e se você estiver trabalhando em algo complexo em que compartilhar código **entre** classes seria útil? Nesses casos, você pode usar a herança de classes.

Por padrão, as classes no Kotlin não podem ser herdadas. O Kotlin foi projetado dessa forma para evitar herança não intencional e tornar suas classes mais fáceis de manter.

As classes do Kotlin só dão suporte à **herança simples**, ou seja, só é possível herdar de **uma classe por vez**. Essa classe é chamada de **pai**.

A classe pai também herda de outra classe (a avó), formando uma hierarquia. No topo da hierarquia de classes do Kotlin está a classe pai comum: `Any`. Todas as classes herdam, em última instância, da classe `Any`:

![Exemplo da hierarquia de classes com o tipo Any](any-type-class.png){width="200"}

A classe `Any` fornece automaticamente a função `toString()` como função membro. Por isso, você pode usar essa função herdada em qualquer uma das suas classes. Por exemplo:

```kotlin
class Car(val make: String, val model: String, val numberOfDoors: Int)

fun main() {
    //sampleStart
    val car1 = Car("Toyota", "Corolla", 4)

    // Uses the .toString() function via string templates to print class properties
    println("Car1: make=${car1.make}, model=${car1.model}, numberOfDoors=${car1.numberOfDoors}")
    // Car1: make=Toyota, model=Corolla, numberOfDoors=4
    //sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-any-class"}

Se você quer usar herança para compartilhar código entre classes, primeiro considere usar classes abstratas.

### Classes abstratas {id="abstract-classes"}

Classes abstratas podem ser herdadas por padrão. A finalidade das classes abstratas é fornecer membros que outras classes herdam ou implementam. Por isso, elas têm um construtor, mas você não pode criar instâncias delas. Dentro da classe filha, você define o comportamento das propriedades e funções do pai com a palavra-chave `override`. Dessa forma, pode-se dizer que a classe filha "sobrescreve" os membros da classe pai.

> Quando você define o comportamento de uma função ou propriedade herdada, chamamos isso de **implementação**.
> 
{style="tip"}

Classes abstratas podem conter funções e propriedades **com** implementação, bem como funções e propriedades **sem** implementação, conhecidas como funções e propriedades abstratas.

Para criar uma classe abstrata, use a palavra-chave `abstract`:

```kotlin
abstract class Animal
```

Para declarar uma função ou uma propriedade **sem** implementação, também use a palavra-chave `abstract`:

```kotlin
abstract fun makeSound()
abstract val sound: String
```

Por exemplo, suponha que você queira criar uma classe abstrata chamada `Product` a partir da qual é possível criar classes filhas para definir diferentes categorias de produtos:

```kotlin
abstract class Product(val name: String, var price: Double) {
    // Abstract property for the product category
    abstract val category: String

    // A function that can be shared by all products
    fun productInfo(): String {
        return "Product: $name, Category: $category, Price: $price"
    }
}
```

Na classe abstrata:

* O construtor tem dois parâmetros para o `name` e o `price` do produto.
* Há uma propriedade abstrata que contém a categoria do produto como string.
* Há uma função que exibe informações sobre o produto.

Vamos criar uma classe filha para eletrônicos. Antes de definir uma implementação para a propriedade `category` na classe filha, você deve usar a palavra-chave `override`:

```kotlin
class Electronic(name: String, price: Double, val warranty: Int) : Product(name, price) {
    override val category = "Electronic"
}
```

A classe `Electronic`:

* Herda da classe abstrata `Product`.
* Tem um parâmetro adicional no construtor: `warranty`, específico para eletrônicos.
* Sobrescreve a propriedade `category` para conter a string `"Electronic"`.

Agora, você pode usar essas classes assim:

```kotlin
abstract class Product(val name: String, var price: Double) {
    // Abstract property for the product category
    abstract val category: String

    // A function that can be shared by all products
    fun productInfo(): String {
        return "Product: $name, Category: $category, Price: $price"
    }
}

class Electronic(name: String, price: Double, val warranty: Int) : Product(name, price) {
    override val category = "Electronic"
}

//sampleStart
fun main() {
    // Creates an instance of the Electronic class
    val laptop = Electronic(name = "Laptop", price = 1000.0, warranty = 2)

    println(laptop.productInfo())
    // Product: Laptop, Category: Electronic, Price: 1000.0
}
//sampleEnd
```
{kotlin-runnable="true" id="kotlin-tour-abstract-class"}

Embora as classes abstratas sejam ótimas para compartilhar código dessa forma, elas são restritas porque as classes no Kotlin só dão suporte à herança simples. Se você precisar herdar de várias fontes, considere usar interfaces.

## Interfaces

Interfaces são parecidas com classes, mas têm algumas diferenças:

* Você não pode criar uma instância de uma interface. Elas não têm construtor nem cabeçalho.
* Suas funções e propriedades são implicitamente herdáveis por padrão. No Kotlin, dizemos que elas são "abertas".
* Você não precisa marcar suas funções com `abstract` se não der uma implementação a elas.

Assim como as classes abstratas, você usa interfaces para definir um conjunto de funções e propriedades que classes podem herdar e implementar depois. Essa abordagem ajuda você a focar na abstração descrita pela interface, em vez dos detalhes específicos de implementação. Usar interfaces torna seu código:

* Mais modular, pois isola partes diferentes, permitindo que evoluam de forma independente.
* Mais fácil de entender, por agrupar funções relacionadas em um conjunto coeso.
* Mais fácil de testar, pois você pode trocar rapidamente uma implementação por um mock nos testes.

Para declarar uma interface, use a palavra-chave `interface`:

```kotlin
interface PaymentMethod
```

### Implementação de interfaces {id="interface-implementation"}

Interfaces dão suporte à herança múltipla, então uma classe pode implementar várias interfaces ao mesmo tempo. Primeiro, vamos considerar o cenário em que uma classe implementa **uma** interface.

Para criar uma classe que implementa uma interface, adicione dois-pontos após o cabeçalho da classe, seguidos do nome da interface que você quer implementar. Você não usa parênteses `()` após o nome da interface, porque interfaces não têm construtor:

```kotlin
class CreditCardPayment : PaymentMethod
```

Por exemplo:

```kotlin
interface PaymentMethod {
    // Functions are inheritable by default
    fun initiatePayment(amount: Double): String
}

class CreditCardPayment(val cardNumber: String, val cardHolderName: String, val expiryDate: String) : PaymentMethod {
    override fun initiatePayment(amount: Double): String {
        // Simulate processing payment with credit card
        return "Payment of $$amount initiated using Credit Card ending in ${cardNumber.takeLast(4)}."
    }
}

fun main() {
    val paymentMethod = CreditCardPayment("1234 5678 9012 3456", "John Doe", "12/25")
    println(paymentMethod.initiatePayment(100.0))
    // Payment of $100.0 initiated using Credit Card ending in 3456.
}
```
{kotlin-runnable="true" id="kotlin-tour-interface-inheritance"}

No exemplo:

* `PaymentMethod` é uma interface que tem uma função `initiatePayment()` sem implementação.
* `CreditCardPayment` é uma classe que implementa a interface `PaymentMethod`.
* A classe `CreditCardPayment` sobrescreve a função `initiatePayment()` herdada.
* `paymentMethod` é uma instância da classe `CreditCardPayment`.
* A função `initiatePayment()` sobrescrita é chamada na instância `paymentMethod` com o parâmetro `100.0`.

Para criar uma classe que implementa **várias** interfaces, adicione dois-pontos após o cabeçalho da classe, seguidos dos nomes das interfaces que você quer implementar, separados por vírgula:

```kotlin
class CreditCardPayment : PaymentMethod, PaymentType
```

Por exemplo:

```kotlin
interface PaymentMethod {
    fun initiatePayment(amount: Double): String
}

interface PaymentType {
    val paymentType: String
}

class CreditCardPayment(val cardNumber: String, val cardHolderName: String, val expiryDate: String) : PaymentMethod,
    PaymentType {
    override fun initiatePayment(amount: Double): String {
        // Simulate processing payment with credit card
        return "Payment of $$amount initiated using Credit Card ending in ${cardNumber.takeLast(4)}."
    }

    override val paymentType: String = "Credit Card"
}

fun main() {
    val paymentMethod = CreditCardPayment("1234 5678 9012 3456", "John Doe", "12/25")
    println(paymentMethod.initiatePayment(100.0))
    // Payment of $100.0 initiated using Credit Card ending in 3456.

    println("Payment is by ${paymentMethod.paymentType}")
    // Payment is by Credit Card
}
```
{kotlin-runnable="true" id="kotlin-tour-interface-multiple-inheritance"}

No exemplo:

* `PaymentMethod` é uma interface que tem a função `initiatePayment()` sem implementação.
* `PaymentType` é uma interface que tem a propriedade `paymentType`, que não é inicializada.
* `CreditCardPayment` é uma classe que implementa as interfaces `PaymentMethod` e `PaymentType`.
* A classe `CreditCardPayment` sobrescreve a função `initiatePayment()` herdada e a propriedade `paymentType`.
* `paymentMethod` é uma instância da classe `CreditCardPayment`.
* A função `initiatePayment()` sobrescrita é chamada na instância `paymentMethod` com o parâmetro `100.0`.
* A propriedade `paymentType` sobrescrita é acessada na instância `paymentMethod`.

Para mais informações sobre interfaces e herança de interfaces, veja [Interfaces](interfaces.md).

## Delegação {id="delegation"}

Interfaces são úteis, mas, se sua interface contém muitas funções, as classes filhas podem acabar com muito código boilerplate. Se você quer sobrescrever apenas uma pequena parte do comportamento de uma classe, precisa repetir muito código.

> Código boilerplate é um trecho de código reutilizado, com pouca ou nenhuma alteração, em várias partes de um projeto de software.
> 
{style="tip"}

Por exemplo, suponha que você tenha uma interface chamada `DrawingTool` que contém várias funções e uma propriedade chamada `color`:

```kotlin
interface DrawingTool {
    val color: String
    fun draw(shape: String)
    fun erase(area: String)
    fun getToolInfo(): String
}
```

Você cria uma classe chamada `PenTool`, que implementa a interface `DrawingTool` e fornece implementações para todos os seus membros:

```kotlin
class PenTool : DrawingTool {
    override val color: String = "black"

    override fun draw(shape: String) {
        println("Drawing $shape using a pen in $color")
    }

    override fun erase(area: String) {
        println("Erasing $area with pen tool")
    }

    override fun getToolInfo(): String {
        return "PenTool(color=$color)"
    }
}
```

Você quer criar uma classe como `PenTool` com o mesmo comportamento, mas um valor de `color` diferente. Uma abordagem é criar uma nova classe que recebe como parâmetro um objeto que implementa a interface `DrawingTool`, como uma instância da classe `PenTool`. Depois, dentro da classe, você pode sobrescrever a propriedade `color`.

Mas, nesse cenário, você precisa adicionar implementações para cada membro da interface `DrawingTool`:

```kotlin
interface DrawingTool {
    val color: String
    fun draw(shape: String)
    fun erase(area: String)
    fun getToolInfo(): String
}

class PenTool : DrawingTool {
    override val color: String = "black"

    override fun draw(shape: String) {
        println("Drawing $shape using a pen in $color")
    }

    override fun erase(area: String) {
        println("Erasing $area with pen tool")
    }

    override fun getToolInfo(): String {
        return "PenTool(color=$color)"
    }
}
//sampleStart
class CanvasSession(val tool: DrawingTool) : DrawingTool {
    override val color: String = "blue"

    override fun draw(shape: String) {
        tool.draw(shape)
    }

    override fun erase(area: String) {
        tool.erase(area)
    }

    override fun getToolInfo(): String {
        return tool.getToolInfo()
    }
}
//sampleEnd
fun main() {
    val pen = PenTool()
    val session = CanvasSession(pen)

    println("Pen color: ${pen.color}")
    // Pen color: black

    println("Session color: ${session.color}")
    // Session color: blue

    session.draw("circle")
    // Drawing circle with pen in black

    session.erase("top-left corner")
    // Erasing top-left corner with pen tool

    println(session.getToolInfo())
    // PenTool(color=black)
}
```
{kotlin-runnable="true" id="kotlin-tour-interface-non-delegation"}

Você pode ver que, se a interface `DrawingTool` tiver um grande número de funções membro, a quantidade de código boilerplate na classe `CanvasSession` pode ser grande. No entanto, existe uma alternativa.

No Kotlin, você pode delegar a implementação da interface para uma instância de classe usando a palavra-chave `by`. Por exemplo:

```kotlin
class CanvasSession(val tool: DrawingTool) : DrawingTool by tool
```

Aqui, `tool` é o nome da instância da classe `PenTool` para a qual as implementações das funções membro são delegadas.

Agora você não precisa adicionar implementações para as funções membro na classe `CanvasSession`. O compilador faz isso automaticamente para você, a partir da classe `PenTool`. Isso poupa você de escrever muito código boilerplate. Em vez disso, você adiciona código apenas para o comportamento que quer alterar na classe filha.

Por exemplo, se você quiser alterar o valor da propriedade `color`:

```kotlin
interface DrawingTool {
    val color: String
    fun draw(shape: String)
    fun erase(area: String)
    fun getToolInfo(): String
}

class PenTool : DrawingTool {
    override val color: String = "black"

    override fun draw(shape: String) {
        println("Drawing $shape using a pen in $color")
    }

    override fun erase(area: String) {
        println("Erasing $area with pen tool")
    }

    override fun getToolInfo(): String {
        return "PenTool(color=$color)"
    }
}

//sampleStart
class CanvasSession(val tool: DrawingTool) : DrawingTool by tool {
    // No boilerplate code!
    override val color: String = "blue"
}
//sampleEnd
fun main() {
    val pen = PenTool()
    val session = CanvasSession(pen)

    println("Pen color: ${pen.color}")
    // Pen color: black

    println("Session color: ${session.color}")
    // Session color: blue

    session.draw("circle")
    // Drawing circle with pen in black

    session.erase("top-left corner")
    // Erasing top-left corner with pen tool

    println(session.getToolInfo())
    // PenTool(color=black)
}
```
{kotlin-runnable="true" id="kotlin-tour-interface-delegation"}

Se quiser, você também pode sobrescrever o comportamento de uma função membro herdada na classe `CanvasSession`, mas agora não precisa adicionar novas linhas de código para cada função membro herdada.

Para mais informações, veja [Delegação](delegation.md).

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Implementar dispositivos inteligentes com uma classe abstrata" id="classes-interfaces-exercise-1">

Imagine que você está trabalhando em um sistema de casa inteligente. Uma casa inteligente normalmente tem diferentes tipos de dispositivos que têm alguns recursos básicos, mas também comportamentos únicos. No código de exemplo abaixo, complete a classe `abstract` chamada `SmartDevice` para que a classe filha `SmartLight` possa compilar com sucesso.

Em seguida, crie outra classe filha chamada `SmartThermostat` que herda da classe `SmartDevice` e implementa as funções `turnOn()` e `turnOff()`, que retornam instruções de impressão descrevendo se o termostato está aquecendo ou desligado. Por fim, adicione outra função chamada `adjustTemperature()` que aceita uma medição de temperatura como entrada e imprime:
`$name thermostat set to $temperature°C.`

<deflist collapsible="true">
    <def title="Dica">
        Na classe <code>SmartDevice</code>, adicione as funções <code>turnOn()</code> e <code>turnOff()</code> para que você possa sobrescrever o comportamento delas depois, na classe <code>SmartThermostat</code>.
    </def>
</deflist>

```kotlin
abstract class // Write your code here

class SmartLight(name: String) : SmartDevice(name) {
    override fun turnOn() {
        println("$name is now ON.")
    }

    override fun turnOff() {
        println("$name is now OFF.")
    }

   fun adjustBrightness(level: Int) {
        println("Adjusting $name brightness to $level%.")
    }
}

class SmartThermostat // Write your code here

fun main() {
    val livingRoomLight = SmartLight("Living Room Light")
    val bedroomThermostat = SmartThermostat("Bedroom Thermostat")
    
    livingRoomLight.turnOn()
    // Living Room Light is now ON.
    livingRoomLight.adjustBrightness(10)
    // Adjusting Living Room Light brightness to 10%.
    livingRoomLight.turnOff()
    // Living Room Light is now OFF.

    bedroomThermostat.turnOn()
    // Bedroom Thermostat thermostat is now heating.
    bedroomThermostat.adjustTemperature(5)
    // Bedroom Thermostat thermostat set to 5°C.
    bedroomThermostat.turnOff()
    // Bedroom Thermostat thermostat is now off.
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/SmartDeviceTest.kt" validate="false" id="kotlin-tour-classes-interfaces-exercise-1"}

```kotlin
abstract class SmartDevice(val name: String) {
    abstract fun turnOn()
    abstract fun turnOff()
}

class SmartLight(name: String) : SmartDevice(name) {
    override fun turnOn() {
        println("$name is now ON.")
    }

    override fun turnOff() {
        println("$name is now OFF.")
    }

   fun adjustBrightness(level: Int) {
        println("Adjusting $name brightness to $level%.")
    }
}

class SmartThermostat(name: String) : SmartDevice(name) {
    override fun turnOn() {
        println("$name thermostat is now heating.")
    }

    override fun turnOff() {
        println("$name thermostat is now off.")
    }

   fun adjustTemperature(temperature: Int) {
        println("$name thermostat set to $temperature°C.")
    }
}


fun main() {
    val livingRoomLight = SmartLight("Living Room Light")
    val bedroomThermostat = SmartThermostat("Bedroom Thermostat")
    
    livingRoomLight.turnOn()
    // Living Room Light is now ON.
    livingRoomLight.adjustBrightness(10)
    // Adjusting Living Room Light brightness to 10%.
    livingRoomLight.turnOff()
    // Living Room Light is now OFF.

    bedroomThermostat.turnOn()
    // Bedroom Thermostat thermostat is now heating.
    bedroomThermostat.adjustTemperature(5)
    // Bedroom Thermostat thermostat set to 5°C.
    bedroomThermostat.turnOff()
    // Bedroom Thermostat thermostat is now off.
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/SmartDeviceTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-classes-interfaces-solution-1"}

</def>
<def title="Implementar uma interface de mídia" id="classes-interfaces-exercise-2">

Crie uma interface chamada `Media` que você possa usar para implementar classes de mídia específicas, como `Audio`, `Video` ou `Podcast`. Sua interface deve incluir:

* Uma propriedade chamada `title` para representar o título da mídia.
* Uma função chamada `play()` para reproduzir a mídia.

Em seguida, crie uma classe chamada `Audio` que implementa a interface `Media`. A classe `Audio` deve usar a propriedade `title` no seu construtor e ter uma propriedade adicional chamada `composer`, do tipo `String`. Na classe, implemente a função `play()` para imprimir o seguinte: `"Playing audio: $title, composed by $composer"`.

<deflist collapsible="true">
    <def title="Dica">
        Você pode usar a palavra-chave <code>override</code> nos cabeçalhos de classe para implementar uma propriedade de uma interface no construtor.
    </def>
</deflist>

```kotlin
interface // Write your code here

class // Write your code here

fun main() {
    val audio = Audio("Symphony No. 5", "Beethoven")
    audio.play()
   // Playing audio: Symphony No. 5, composed by Beethoven
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/AudioTest.kt" validate="false" id="kotlin-tour-classes-interfaces-exercise-2"}

```kotlin
interface Media {
    val title: String
    fun play()
}

class Audio(override val title: String, val composer: String) : Media {
    override fun play() {
        println("Playing audio: $title, composed by $composer")
    }
}

fun main() {
    val audio = Audio("Symphony No. 5", "Beethoven")
    audio.play()
   // Playing audio: Symphony No. 5, composed by Beethoven
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/AudioTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-classes-interfaces-solution-2"}

</def>
<def title="Combinar uma interface e uma classe abstrata" id="classes-interfaces-exercise-3">

Você está criando um sistema de processamento de pagamentos para um app de e-commerce. Cada método de pagamento precisa conseguir autorizar um pagamento e processar uma transação. Alguns pagamentos também precisam conseguir processar reembolsos.

1. Na interface `Refundable`, adicione uma função chamada `refund()` para processar reembolsos.

2. Na classe abstrata `PaymentMethod`:
   * Adicione uma função chamada `authorize()` que recebe um valor e imprime uma mensagem contendo o valor.
   * Adicione uma função abstrata chamada `processPayment()` que também recebe um valor.

3. Crie uma classe chamada `CreditCard` que implementa a interface `Refundable` e a classe abstrata `PaymentMethod`. Nessa classe, adicione implementações para as funções `refund()` e `processPayment()` para que elas imprimam as seguintes instruções:
   * `"Refunding $amount to the credit card."`
   * `"Processing credit card payment of $amount."`

```kotlin
interface Refundable {
    // Write your code here
}

abstract class PaymentMethod(val name: String) {
    // Write your code here
}

class CreditCard // Write your code here

fun main() {
    val visa = CreditCard("Visa")
    
    visa.authorize(100.0)
    // Authorizing payment of $100.0.
    visa.processPayment(100.0)
    // Processing credit card payment of $100.0.
    visa.refund(50.0)
    // Refunding $50.0 to the credit card.
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/CreditCardTest.kt" validate="false" id="kotlin-tour-classes-interfaces-exercise-3"}

```kotlin
interface Refundable {
    fun refund(amount: Double)
}

abstract class PaymentMethod(val name: String) {
    fun authorize(amount: Double) {
        println("Authorizing payment of $$amount.")
    }

    abstract fun processPayment(amount: Double)
}

class CreditCard(name: String) : PaymentMethod(name), Refundable {
    override fun processPayment(amount: Double) {
        println("Processing credit card payment of $$amount.")
    }

    override fun refund(amount: Double) {
        println("Refunding $$amount to the credit card.")
    }
}

fun main() {
    val visa = CreditCard("Visa")
    
    visa.authorize(100.0)
    // Authorizing payment of $100.0.
    visa.processPayment(100.0)
    // Processing credit card payment of $100.0.
    visa.refund(50.0)
    // Refunding $50.0 to the credit card.
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/CreditCardTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-classes-interfaces-solution-3"}

</def>
<def title="Personalizar o comportamento com delegação de interface" id="classes-interfaces-exercise-4">

Você tem um app de mensagens simples que tem algumas funcionalidades básicas, mas quer adicionar funcionalidades para mensagens _inteligentes_ sem duplicar muito o código.

No código abaixo, defina uma classe chamada `SmartMessenger` que herda da interface `Messenger`, mas delega a implementação para uma instância da classe `BasicMessenger`.

Na classe `SmartMessenger`, sobrescreva a função `sendMessage()` para enviar mensagens inteligentes. A função deve aceitar uma `message` como entrada e retornar uma instrução impressa: `"Sending a smart message: $message"`. Além disso, chame a função `sendMessage()` da classe `BasicMessenger` e preceda a mensagem com `[smart]`.

> Você não precisa reescrever a função `receiveMessage()` na classe `SmartMessenger`.
> 
{style="note"}

```kotlin
interface Messenger {
    fun sendMessage(message: String)
    fun receiveMessage(): String
}

class BasicMessenger : Messenger {
    override fun sendMessage(message: String) {
        println("Sending message: $message")
    }

    override fun receiveMessage(): String {
        return "You've got a new message!"
    }
}

class SmartMessenger // Write your code here

fun main() {
    val basicMessenger = BasicMessenger()
    val smartMessenger = SmartMessenger(basicMessenger)
    
    basicMessenger.sendMessage("Hello!")
    // Sending message: Hello!
    println(smartMessenger.receiveMessage())
    // You've got a new message!
    smartMessenger.sendMessage("Hello from SmartMessenger!")
    // Sending a smart message: Hello from SmartMessenger!
    // Sending message: [smart] Hello from SmartMessenger!
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/SmartMessengerTest.kt" validate="false" id="kotlin-tour-classes-interfaces-exercise-4"}

```kotlin
interface Messenger {
    fun sendMessage(message: String)
    fun receiveMessage(): String
}

class BasicMessenger : Messenger {
    override fun sendMessage(message: String) {
        println("Sending message: $message")
    }

    override fun receiveMessage(): String {
        return "You've got a new message!"
    }
}

class SmartMessenger(val basicMessenger: BasicMessenger) : Messenger by basicMessenger {
    override fun sendMessage(message: String) {
        println("Sending a smart message: $message")
        basicMessenger.sendMessage("[smart] $message")
    }
}

fun main() {
    val basicMessenger = BasicMessenger()
    val smartMessenger = SmartMessenger(basicMessenger)
    
    basicMessenger.sendMessage("Hello!")
    // Sending message: Hello!
    println(smartMessenger.receiveMessage())
    // You've got a new message!
    smartMessenger.sendMessage("Hello from SmartMessenger!")
    // Sending a smart message: Hello from SmartMessenger!
    // Sending message: [smart] Hello from SmartMessenger!
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/SmartMessengerTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-classes-interfaces-solution-4"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-intermediate-lambdas-receiver.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-intermediate-objects.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->
