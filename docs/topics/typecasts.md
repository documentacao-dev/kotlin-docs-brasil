[//]: # (title: Verificações de tipo e conversões)

No Kotlin, você pode fazer duas coisas com tipos em tempo de execução: verificar se um objeto é de um tipo específico ou convertê-lo para outro tipo.
As **verificações** de tipo ajudam a confirmar o tipo de objeto com que você está lidando, enquanto as **conversões** de tipo tentam converter o objeto para outro tipo.

> Para aprender especificamente sobre verificações e conversões de **generics**, por exemplo `List<T>`, `Map<K,V>`, veja [Verificações e conversões de generics](generics.md#generics-type-checks-and-casts).
>
{style="tip"}

## Verificações com os operadores `is` e `!is` {id="is-and-is-operators"}

Use o operador `is` (ou `!is` para negá-lo) para verificar, em tempo de execução, se um objeto corresponde a um tipo:

```kotlin
fun main() {
    val input: Any = "Hello, Kotlin"

    if (input is String) {
        println("Message length: ${input.length}")
        // Message length: 13
    }

    if (input !is String) { // Same as !(input is String)
        println("Input is not a valid message")
    } else {
        println("Processing message: ${input.length} characters")
        // Processing message: 13 characters
    }
}
```
{kotlin-runnable="true" id="kotlin-typecasts-is-operator"}

Você também pode usar os operadores `is` e `!is` para verificar se um objeto corresponde a um subtipo:

```kotlin
interface Animal {
    val name: String
    fun speak()
}

class Dog(override val name: String) : Animal {
    override fun speak() = println("$name says: Woof!")
}

class Cat(override val name: String) : Animal {
    override fun speak() = println("$name says: Meow!")
}
//sampleStart
fun handleAnimal(animal: Animal) {
    println("Handling animal: ${animal.name}")
    animal.speak()
    
    // Use is operator to check for subtypes
    if (animal is Dog) {
        println("Special care instructions: This is a dog.")
    } else if (animal is Cat) {
        println("Special care instructions: This is a cat.")
    }
}
//sampleEnd
fun main() {
    val pets: List<Animal> = listOf(
        Dog("Buddy"),
        Cat("Whiskers"),
        Dog("Rex")
    )

    for (pet in pets) {
        handleAnimal(pet)
        println("---")
    }
    // Handling animal: Buddy
    // Buddy says: Woof!
    // Special care instructions: This is a dog.
    // ---
    // Handling animal: Whiskers
    // Whiskers says: Meow!
    // Special care instructions: This is a cat.
    // ---
    // Handling animal: Rex
    // Rex says: Woof!
    // Special care instructions: This is a dog.
    // ---
}
```
{kotlin-runnable="true" id="kotlin-typecasts-is-operator-subtype"}

Este exemplo usa o operador `is` para verificar se a instância da classe `Animal` é um subtipo `Dog` ou `Cat`, para imprimir as instruções de cuidado correspondentes.

Você pode verificar se um objeto é um supertipo do seu tipo declarado, mas não vale a pena, porque a resposta é sempre verdadeira.
Toda instância de classe já é uma instância dos seus supertipos.

> Para identificar o tipo de um objeto em tempo de execução, veja [Reflexão](reflection.md).
> 
{type="tip"}

## Conversões de tipo {id="type-casts"}

Converter o tipo de um objeto no Kotlin para outro tipo é chamado de **casting**.

Em alguns casos, o compilador converte objetos automaticamente para você. Isso é chamado de smart-casting.

Se você precisar converter explicitamente um tipo, use os [operadores de conversão](#unsafe-cast-operator) `as?` ou `as`. 

## Smart casts

O compilador acompanha as verificações de tipo e as [conversões explícitas](#unsafe-cast-operator) para valores imutáveis e insere conversões implícitas (seguras) automaticamente:

```kotlin
fun logMessage(data: Any) {
    // data is automatically cast to String
    if (data is String) {
        println("Received text: ${data.length} characters")
    }
}

fun main() {
    logMessage("Server started")
    // Received text: 14 characters
    logMessage(404)
}
```
{kotlin-runnable="true" id="kotlin-typecasts-smartcast"}

O compilador é inteligente o suficiente para saber que uma conversão é segura se uma verificação negativa leva a um `return`:

```kotlin
fun logMessage(data: Any) {
    // data is automatically cast to String
    if (data !is String) return

    println("Received text: ${data.length} characters")
}

fun main() {
    logMessage("User signed in")
    // Received text: 14 characters
    logMessage(true)
}
```
{kotlin-runnable="true" id="kotlin-typecasts-smartcast-negative"}

### Controle de fluxo {id="control-flow"}

Smart casts funcionam não só para expressões condicionais `if`, mas também para [expressões `when`](control-flow.md#when-expressions-and-statements):

```kotlin
fun processInput(data: Any) {
    when (data) {
        // data is automatically cast to Int
        is Int -> println("Log: Assigned new ID ${data + 1}")
        // data is automatically cast to String
        is String -> println("Log: Received message \"$data\"")
        // data is automatically cast to IntArray
        is IntArray -> println("Log: Processed scores, total = ${data.sum()}")
    }
}

fun main() {
    processInput(1001)
    // Log: Assigned new ID 1002
    processInput("System rebooted")
    // Log: Received message "System rebooted"
    processInput(intArrayOf(10, 20, 30))
    // Log: Processed scores, total = 60
}
```
{kotlin-runnable="true" id="kotlin-typecasts-smartcast-when"}

E para [laços `while`](control-flow.md#while-loops):

```kotlin
sealed interface Status
data class Ok(val currentRoom: String) : Status
data object Error : Status

class RobotVacuum(val rooms: List<String>) {
    var index = 0

    fun status(): Status =
        if (index < rooms.size) Ok(rooms[index])
        else Error

    fun clean(): Status {
        println("Finished cleaning ${rooms[index]}")
        index++
        return status()
    }
}

fun main() {
    //sampleStart
    val robo = RobotVacuum(listOf("Living Room", "Kitchen", "Hallway"))

    var status: Status = robo.status()
    while (status is Ok) {
        // The compiler smart casts status to OK type, so the currentRoom
        // property is accessible.
        println("Cleaning ${status.currentRoom}...")
        status = robo.clean()
    }
    // Cleaning Living Room...
    // Finished cleaning Living Room
    // Cleaning Kitchen...
    // Finished cleaning Kitchen
    // Cleaning Hallway...
    // Finished cleaning Hallway
    //sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-typecasts-smartcast-while"}

Neste exemplo, a sealed interface `Status` tem duas implementações: a data class `Ok` e o data object `Error`.
Somente a data class `Ok` tem a propriedade `currentRoom`. Quando a condição do laço `while` é avaliada como verdadeira, o
compilador faz o smart cast da variável `status` para o tipo `Ok`, tornando a propriedade `currentRoom` acessível dentro do corpo do laço.

Se você declarar uma variável do tipo `Boolean` antes de usá-la na condição `if`, `when` ou `while`, qualquer informação que o
compilador coletou sobre a variável fica acessível no bloco correspondente para o smart-casting.

Isso pode ser útil quando você quer, por exemplo, extrair condições booleanas para variáveis. Assim, você pode dar à variável
um nome significativo, o que melhora a legibilidade do código e permite reutilizar a variável depois no código. Por exemplo:

```kotlin
class Cat {
    fun purr() {
        println("Purr purr")
    }
}
//sampleStart
fun petAnimal(animal: Any) {
    val isCat = animal is Cat
    if (isCat) {
        // The compiler can access information about
        // isCat, so it knows that animal was smart-cast
        // to the type Cat.
        // Therefore, the purr() function can be called.
        animal.purr()
    }
}

fun main(){
    val kitty = Cat()
    petAnimal(kitty)
    // Purr purr
}
//sampleEnd
```
{kotlin-runnable="true" kotlin-min-compiler-version="2.0" id="kotlin-smart-casts-local-variables" validate="false"}

### Operadores lógicos {id="logical-operators"}

O compilador pode fazer smart casts no lado direito dos operadores `&&` ou `||` se houver uma verificação de tipo (normal ou negativa) no lado esquerdo:

```kotlin
// x is automatically cast to String on the right-hand side of `||`
if (x !is String || x.length == 0) return

// x is automatically cast to String on the right-hand side of `&&`
if (x is String && x.length > 0) {
    print(x.length) // x is automatically cast to String
}
```

Se você combinar verificações de tipo para objetos com o operador `and` (`&&`), o compilador faz o smart cast do objeto
para todos os tipos verificados simultaneamente. Saiba mais em [Tipos de interseção](#intersection-types).

Se você combinar verificações de tipo para objetos com o operador `or` (`||`), é feito um smart cast para o supertipo comum mais próximo:

```kotlin
interface Status {
    fun signal() {}
}

interface Ok : Status
interface Postponed : Status
interface Declined : Status

fun signalCheck(signalStatus: Any) {
    if (signalStatus is Postponed || signalStatus is Declined) {
        // signalStatus is smart-cast to a common supertype Status
        signalStatus.signal()
    }
}
```

> O supertipo comum é uma **aproximação** de um [tipo união](https://en.wikipedia.org/wiki/Union_type). Tipos união
> não são [atualmente aceitos no Kotlin](https://youtrack.jetbrains.com/issue/KT-13108/Denotable-union-and-intersection-types).
>
{style="note"}

### Tipos de interseção {id="intersection-types"}

Quando o compilador faz smart cast de um objeto por meio de várias verificações com `&&`, ele infere um [*tipo de interseção*](https://kotlinlang.org/spec/type-system.html#intersection-types).
Trata-se de um tipo interno que satisfaz simultaneamente todas as restrições verificadas:

```kotlin
interface Bird {
    fun fly()
}

interface Fish {
    fun swim()
}

fun describe(animal: Any) {
    // Infers the Bird and Fish types
    if (animal is Bird && animal is Fish) {
        // Accesses fly() and swim() without additional checks or casts
        animal.fly()
        animal.swim()
    }
}
```

Tipos de interseção não são denotáveis. Eles existem apenas no sistema de tipos interno do compilador, para preservar informações de tipo
durante a verificação de tipos. Você não pode escrevê-los diretamente no código Kotlin. Você pode encontrar tipos de interseção em
mensagens de erro do compilador e em dicas de ferramentas da IDE, normalmente exibidos como `A & B`.
A única exceção é `T & Any`, que declara um [tipo definitivamente não nulo](generics.md#definitely-non-nullable-types).
Essa sintaxe é reservada especificamente para combinar um parâmetro de tipo com `Any`.

```kotlin
fun  <T> T.assertNotNull(): T & Any = this ?: throw IllegalStateException("null value")
```

### Funções inline {id="inline-functions"}

O compilador pode fazer smart cast de variáveis capturadas dentro de funções lambda passadas para [funções inline](inline-functions.md).

Funções inline são tratadas como tendo um contrato implícito [`callsInPlace`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.contracts/-contract-builder/calls-in-place.html).
Isso significa que quaisquer funções lambda passadas para uma função inline são chamadas no próprio local. Como as funções lambda são chamadas no local, o compilador sabe que uma função lambda não pode vazar referências para variáveis contidas no corpo dessa função.

O compilador usa esse conhecimento, junto com outras análises, para decidir se é seguro fazer smart cast de qualquer uma das
variáveis capturadas. Por exemplo:

```kotlin
interface Processor {
    fun process()
}

inline fun inlineAction(f: () -> Unit) = f()

fun nextProcessor(): Processor? = null

fun runProcessor(): Processor? {
    var processor: Processor? = null
    inlineAction {
        // The compiler knows that processor is a local variable and inlineAction()
        // is an inline function, so references to processor can't be leaked.
        // Therefore, it's safe to smart-cast processor.
      
        // If processor isn't null, processor is smart-cast
        if (processor != null) {
            // The compiler knows that processor isn't null, so no safe call 
            // is needed
            processor.process()
        }

        processor = nextProcessor()
    }

    return processor
}
```

### Tratamento de exceções {id="exception-handling"}

As informações de smart cast são repassadas aos blocos `catch` e `finally`. Isso torna seu código mais seguro,
pois o compilador acompanha se o objeto tem um tipo anulável. Por exemplo:

```kotlin
//sampleStart
fun testString() {
    var stringInput: String? = null
    // stringInput is smart-cast to String type
    stringInput = ""
    try {
        // The compiler knows that stringInput isn't null
        println(stringInput.length)
        // 0

        // The compiler rejects previous smart cast information for 
        // stringInput. Now stringInput has the String? type.
        stringInput = null

        // Trigger an exception
        if (2 > 1) throw Exception()
        stringInput = ""
    } catch (exception: Exception) {
        // The compiler knows stringInput can be null
        // so stringInput stays nullable.
        println(stringInput?.length)
        // null
    }
}
//sampleEnd
fun main() {
    testString()
}
```
{kotlin-runnable="true" kotlin-min-compiler-version="2.0" id="kotlin-smart-casts-exception-handling"}

### Pré-requisitos do smart cast {id="smart-cast-prerequisites"}

Smart casts funcionam somente quando o compilador pode garantir que a variável não muda entre a verificação e seu uso.
Eles podem ser usados nas seguintes condições:

<table style="none">
    <tr>
        <td>
            Variáveis locais <code>val</code>
        </td>
        <td>
            Sempre, exceto <a href="delegated-properties.md">propriedades delegadas locais</a>.
        </td>
    </tr>
    <tr>
        <td>
            Propriedades <code>val</code>
        </td>
        <td>
            Se a propriedade for <code>private</code> ou <code>internal</code>, ou se a verificação for feita no mesmo <a href="visibility-modifiers.md#modules">módulo</a> onde a propriedade é declarada. Smart casts não podem ser usados em propriedades <code>open</code> nem em propriedades com getter personalizado.
        </td>
    </tr>
    <tr>
        <td>
            Variáveis locais <code>var</code>
        </td>
        <td>
            Se a variável não for modificada entre a verificação e seu uso, não for capturada por uma lambda que a modifica e não for uma propriedade delegada local.
        </td>
    </tr>
    <tr>
        <td>
            Propriedades <code>var</code>
        </td>
        <td>
            Nunca, porque a variável pode ser modificada a qualquer momento por outro código.
        </td>
    </tr>
</table>

## Operadores de conversão `as` e `as?` {id="unsafe-cast-operator"}

O Kotlin tem dois operadores de conversão: `as` e `as?`. Você pode usar ambos para converter, mas eles têm comportamentos diferentes.

Se uma conversão falhar com o operador `as`, uma `ClassCastException` é lançada em tempo de execução. Por isso ele também é chamado de operador **inseguro**.
Você pode usar `as` ao converter para um tipo não nulo:

```kotlin
fun main() {
    val rawInput: Any = "user-1234"

    // Casts to String successfully
    val userId = rawInput as String
    println("Logging in user with ID: $userId")
    // Logging in user with ID: user-1234

    // Triggers ClassCastException
    val wrongCast = rawInput as Int
    println("wrongCast contains: $wrongCast")
    // Exception in thread "main" java.lang.ClassCastException
}
```
{kotlin-runnable="true" kotlin-min-compiler-version="2.0" id="kotlin-unsafe-cast-operator" validate="false"}

Se você usar o operador `as?`, e a conversão falhar, o operador retorna `null`. Por isso ele também é chamado de operador **seguro**:

```kotlin
fun main() {
    val rawInput: Any = "user-1234"

    // Casts to String successfully
    val userId = rawInput as? String
    println("Logging in user with ID: $userId")
    // Logging in user with ID: user-1234

    // Assigns a null value to wrongCast
    val wrongCast = rawInput as? Int
    println("wrongCast contains: $wrongCast")
    // wrongCast contains: null
}
```
{kotlin-runnable="true" kotlin-min-compiler-version="2.0" id="kotlin-safe-cast-operator"}

Para converter um tipo anulável com segurança, use o operador `as?` para evitar uma `ClassCastException` se a conversão falhar.

Você _pode_ usar `as` com um tipo anulável. Isso permite que o resultado seja `null`, mas ainda assim lança uma `ClassCastException` 
se a conversão não tiver sucesso. Por esse motivo, `as?` é a opção mais segura:

```kotlin
fun main() {
    val config: Map<String, Any?> = mapOf(
        "username" to "kodee",
        "alias" to null,
        "loginAttempts" to 3
    )

    // Unsafely casts to a nullable String
    val username: String? = config["username"] as String?
    println("Username: $username")
    // Username: kodee

    // Unsafely casts a null value to a nullable String
    val alias: String? = config["alias"] as String?
    println("Alias: $alias")
    // Alias: null

    // Fails to cast to nullable String and throws ClassCastException
    // val unsafeAttempts: String? = config["loginAttempts"] as String?
    // println("Login attempts (unsafe): $unsafeAttempts")
    // Exception in thread "main" java.lang.ClassCastException

    // Fails to cast to nullable String and returns null
    val safeAttempts: String? = config["loginAttempts"] as? String
    println("Login attempts (safe): $safeAttempts")
    // Login attempts (safe): null
}
```
{kotlin-runnable="true" kotlin-min-compiler-version="2.0" id="kotlin-cast-nullable-types"}

### Upcasting e downcasting {id="up-and-downcasting"}

No Kotlin, você pode converter objetos para supertipos e subtipos. 

Converter um objeto para uma instância da sua superclasse é chamado de **upcasting**. O upcasting não precisa de nenhuma sintaxe especial nem de operadores de conversão. Por exemplo:

```kotlin
interface Animal {
    fun makeSound()
}

class Dog : Animal {
    // Implements behavior for makeSound()
    override fun makeSound() {
        println("Dog says woof!")
    }
}

fun printAnimalInfo(animal: Animal) {
    animal.makeSound()
}

fun main() {
    val dog = Dog()
    // Upcasts Dog instance to Animal
    printAnimalInfo(dog)  
    // Dog says woof!
}
```
{kotlin-runnable="true" kotlin-min-compiler-version="2.0" id="kotlin-upcast"}

Neste exemplo, quando a função `printAnimalInfo()` é chamada com uma instância de `Dog`, o compilador faz o upcasting
para `Animal`, porque esse é o tipo de parâmetro esperado. Como o objeto real continua sendo uma instância de `Dog`, o compilador
resolve dinamicamente a função `makeSound()` da classe `Dog`, imprimindo `"Dog says woof!"`.

Você vai ver upcasting explícito com frequência nas APIs do Kotlin em que o comportamento depende de um tipo abstrato. Ele também é comum no Jetpack Compose
e em toolkits de UI, que normalmente tratam todos os elementos de UI como supertipos e depois operam sobre subclasses específicas:

```kotlin
    val textView = TextView(this)
    textView.text = "Hello, View!"

    // Upcasts from TextView to View
    val view: View = textView  

    // Use View functions
    view.setPadding(20, 20, 20, 20)
    // Activity expects a View type
    setContentView(view)
```

Converter um objeto para uma instância de uma subclasse é chamado de **downcasting**. Como o downcasting pode ser inseguro, você precisa usar operadores de conversão explícitos. Para evitar exceções em conversões que falham, recomendamos o operador de conversão seguro `as?`, que retorna `null` se a conversão falhar:

```kotlin
interface Animal {
    fun makeSound()
}

class Dog : Animal {
    override fun makeSound() {
        println("Dog says woof!")
    }

    fun bark() {
        println("BARK!")
    }
}

fun main() {
    // Creates animal as a Dog instance with Animal
    // type
    val animal: Animal = Dog()
    
    // Safely downcasts animal to Dog type
    val dog: Dog? = animal as? Dog

    // Uses a safe call to call bark() if dog isn't null
    dog?.bark()
    // "BARK!"
}
```
{kotlin-runnable="true" kotlin-min-compiler-version="2.0" id="kotlin-downcast"}

Neste exemplo, `animal` é declarado com o tipo `Animal`, mas guarda uma instância de `Dog`. O código converte `animal` com segurança para o tipo 
`Dog` e usa uma [chamada segura](null-safety.md#safe-call-operator) (`?.`) para acessar a função `bark()`.

Você vai usar downcasting em serialização ao desserializar uma classe base para um subtipo específico. Também é comum ao trabalhar 
com bibliotecas Java que retornam objetos de supertipo, que talvez seja necessário converter para um subtipo (downcasting) no Kotlin.

<!-- ia-translate: true -->