[//]: # (title: Null safety)

<no-index/>


Na tour para iniciantes, você aprendeu a lidar com valores `null` no seu código. Este capítulo aborda casos de uso comuns dos recursos de null safety e como aproveitá-los ao máximo.

## Smart casts e safe casts {id="smart-casts-and-safe-casts"}

O Kotlin às vezes consegue inferir o tipo sem declaração explícita. Quando você diz ao Kotlin para tratar uma variável ou objeto como se pertencesse a um tipo específico, esse processo se chama **casting**. Quando um tipo é convertido automaticamente, como quando é inferido, ele se chama **smart casting**.

### Operadores is e !is {id="is-and-is-operators"}

Antes de explorar como o casting funciona, vamos ver como verificar se um objeto tem determinado tipo. Para isso, você pode usar os operadores `is` e `!is` com as expressões condicionais `when` ou `if`:

* `is` verifica se o objeto tem o tipo e retorna um valor booleano.
* `!is` verifica se o objeto **não** tem o tipo e retorna um valor booleano.

Por exemplo:

```kotlin
fun printObjectType(obj: Any) {
    when (obj) {
        is Int -> println("It's an Integer with value $obj")
        !is Double -> println("It's NOT a Double")
        else -> println("Unknown type")
    }
}

fun main() {
    val myInt = 42
    val myDouble = 3.14
    val myList = listOf(1, 2, 3)
  
    // The type is Int
    printObjectType(myInt)
    // It's an Integer with value 42

    // The type is List, so it's NOT a Double.
    printObjectType(myList)
    // It's NOT a Double

    // The type is Double, so the else branch is triggered.
    printObjectType(myDouble)
    // Unknown type
}
```
{kotlin-runnable="true" id="kotlin-tour-null-safety-casts"}

> Você já viu um exemplo de como usar uma expressão condicional `when` com os operadores `is` e `!is` no capítulo [Classes abertas e outras classes especiais](kotlin-tour-intermediate-open-special-classes.md#sealed-classes).
> 
{style="tip"}

### Operadores as e as? {id="as-and-as-operators"}

Para fazer um _cast_ explícito de um objeto para qualquer outro tipo, use o operador `as`. Isso inclui converter de um tipo nulável para o equivalente não nulável. Se o cast não for possível, o programa falha **em tempo de execução**. Por isso, ele é chamado de operador de cast **inseguro**.

```kotlin
fun main() {
//sampleStart
    val a: String? = null
    val b = a as String

    // Triggers an error at runtime
    print(b)
//sampleEnd
}
```
{kotlin-runnable="true" validate="false" id="kotlin-tour-null-safety-as-operator"}

Para fazer um cast explícito para um tipo não nulável, mas retornar `null` em vez de lançar um erro se o cast falhar, use o operador `as?`. Como o operador `as?` não gera erro em caso de falha, ele é chamado de operador **seguro**.

```kotlin
fun main() {
//sampleStart
    val a: String? = null
    val b = a as? String

    // Returns null value
    print(b)
    // null
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-null-safety-safe-operator"}

Você pode combinar o operador `as?` com o operador Elvis `?:` para reduzir várias linhas de código a uma só. Por exemplo, a função `calculateTotalStringLength()` a seguir calcula o comprimento total de todas as strings de uma lista mista:

```kotlin
fun calculateTotalStringLength(items: List<Any>): Int {
    var totalLength = 0

    for (item in items) {
        totalLength += if (item is String) {
            item.length
        } else {
            0  // Add 0 for non-String items
        }
    }

    return totalLength
}
```

O exemplo:

* Usa a variável `totalLength` como contador.
* Usa um laço `for` para percorrer cada item da lista.
* Usa um `if` e o operador `is` para verificar se o item atual é uma string:
  * Se for, o comprimento da string é somado ao contador.
  * Se não for, o contador não é incrementado.
* Retorna o valor final da variável `totalLength`.

Esse código pode ser reduzido a:

```kotlin
fun calculateTotalStringLength(items: List<Any>): Int {
    return items.sumOf { (it as? String)?.length ?: 0 }
}
```

O exemplo usa a função de extensão [`.sumOf()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sum-of.html) e fornece uma expressão lambda que:

* Para cada item da lista, faz um cast seguro para `String` usando `as?`.
* Usa uma chamada segura `?.` para acessar a propriedade `length` se a chamada não retornar um valor `null`.
* Usa o operador Elvis `?:` para retornar `0` se a chamada segura retornar `null`.

## Valores null e coleções {id="null-values-and-collections"}

No Kotlin, trabalhar com coleções muitas vezes envolve lidar com valores `null` e filtrar elementos desnecessários. O Kotlin tem funções úteis para escrever código limpo, eficiente e seguro contra null ao trabalhar com listas, conjuntos, mapas e outros tipos de coleções.

Para filtrar valores `null` de uma lista, use a função [`filterNotNull()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter-not-null.html):

```kotlin
fun main() {
//sampleStart
    val emails: List<String?> = listOf("alice@example.com", null, "bob@example.com", null, "carol@example.com")

    val validEmails = emails.filterNotNull()

    println(validEmails)
    // [alice@example.com, bob@example.com, carol@example.com]
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-null-safety-filternotnull"}

Se você quiser filtrar valores `null` diretamente ao criar uma lista, use a função [`listOfNotNull()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/list-of-not-null.html):

```kotlin
fun main() {
//sampleStart
    val serverConfig = mapOf(
        "appConfig.json" to "App Configuration",
        "dbConfig.json" to "Database Configuration"
    )

    val requestedFile = "appConfig.json"
    val configFiles = listOfNotNull(serverConfig[requestedFile])

    println(configFiles)
    // [App Configuration]
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-null-safety-listofnotnull"}

Nos dois exemplos, se todos os itens forem valores `null`, uma lista vazia é retornada.

O Kotlin também oferece funções para encontrar valores em coleções. Se um valor não for encontrado, elas retornam valores `null` em vez de gerar um erro:

* [`maxOrNull()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/max-or-null.html) encontra o maior valor. Se ele não existir, retorna um valor `null`.
* [`minOrNull()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/min-or-null.html) encontra o menor valor. Se ele não existir, retorna um valor `null`.

Por exemplo:

```kotlin
fun main() {
//sampleStart
    // Temperatures recorded over a week
    val temperatures = listOf(15, 18, 21, 21, 19, 17, 16)
  
    // Find the highest temperature of the week
    val maxTemperature = temperatures.maxOrNull()
    println("Highest temperature recorded: ${maxTemperature ?: "No data"}")
    // Highest temperature recorded: 21

    // Find the lowest temperature of the week
    val minTemperature = temperatures.minOrNull()
    println("Lowest temperature recorded: ${minTemperature ?: "No data"}")
    // Lowest temperature recorded: 15
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-null-safety-collections"}

Este exemplo usa o operador Elvis `?:` para exibir uma mensagem caso as funções retornem um valor `null`.

> As funções `maxOrNull()` e `minOrNull()` foram projetadas para uso com coleções que **não**
> contêm valores `null`. Caso contrário, não é possível saber se a função não encontrou o valor desejado ou se encontrou um valor `null`.
>
{style="note"}

Você pode usar a função [`singleOrNull()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/single-or-null.html) com uma expressão lambda para encontrar um único item que corresponda a uma condição.
Se ele não existir ou se houver vários itens que correspondam, a função retorna um valor `null`:

```kotlin
fun main() {
//sampleStart
    // Temperatures recorded over a week
    val temperatures = listOf(15, 18, 21, 21, 19, 17, 16)

    // Check if there was exactly one day with 30 degrees
    val singleHotDay = temperatures.singleOrNull{ it == 30 }
    println("Single hot day with 30 degrees: ${singleHotDay ?: "None"}")
    // Single hot day with 30 degrees: None
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-null-safety-singleornull"}

> A função `singleOrNull()` foi projetada para uso com coleções que **não** contêm valores `null`.
>
{style="note"}

Algumas funções usam uma expressão lambda para transformar uma coleção e retornam valores `null` se não conseguirem cumprir seu propósito.

Para transformar uma coleção com uma expressão lambda e retornar o primeiro valor que não seja `null`, use a função [`firstNotNullOfOrNull()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/first-not-null-of-or-null.html). Se nenhum valor assim existir, a função retorna um valor `null`:

```kotlin
fun main() {
//sampleStart
    data class User(val name: String?, val age: Int?)

    val users = listOf(
        User(null, 25),
        User("Alice", null),
        User("Bob", 30)
    )

    val firstNonNullName = users.firstNotNullOfOrNull { it.name }
    println(firstNonNullName)
    // Alice
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-null-safety-firstnotnullofornull"}

Para usar uma expressão lambda que processa cada item da coleção sequencialmente e cria um valor acumulado (ou retorna um valor `null` se a coleção estiver vazia), use a função [`reduceOrNull()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/reduce-or-null.html):

```kotlin
fun main() {
//sampleStart
    // Prices of items in a shopping cart
    val itemPrices = listOf(20, 35, 15, 40, 10)

    // Calculate the total price using the reduceOrNull() function
    val totalPrice = itemPrices.reduceOrNull { runningTotal, price -> runningTotal + price }
    println("Total price of items in the cart: ${totalPrice ?: "No items"}")
    // Total price of items in the cart: 120

    val emptyCart = listOf<Int>()
    val emptyTotalPrice = emptyCart.reduceOrNull { runningTotal, price -> runningTotal + price }
    println("Total price of items in the empty cart: ${emptyTotalPrice ?: "No items"}")
    // Total price of items in the empty cart: No items
//sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-null-safety-reduceornull"}

Este exemplo também usa o operador Elvis `?:` para exibir uma mensagem caso a função retorne um valor `null`.

> A função `reduceOrNull()` foi projetada para uso com coleções que **não** contêm valores `null`.
>
{style="note"}

Explore a [biblioteca padrão](https://kotlinlang.org/api/core/kotlin-stdlib/) do Kotlin para encontrar mais funções que ajudam a tornar seu código mais seguro.

## Retornos antecipados e o operador Elvis {id="early-returns-and-the-elvis-operator"}

Na tour para iniciantes, você aprendeu a usar [retornos antecipados](kotlin-tour-functions.md#early-returns-in-functions) para interromper o processamento de uma função a partir de determinado ponto. Você pode usar o operador Elvis `?:` com um retorno antecipado para verificar pré-condições em uma função. Essa abordagem é uma ótima forma de manter o código conciso, porque você não precisa de verificações aninhadas. A complexidade reduzida também facilita a manutenção. Por exemplo:

```kotlin
data class User(
    val id: Int,
    val name: String,
    // List of friend user IDs
    val friends: List<Int>
)

// Function to get the number of friends for a user
fun getNumberOfFriends(users: Map<Int, User>, userId: Int): Int {
    // Retrieves the user or return -1 if not found
    val user = users[userId] ?: return -1
    // Returns the number of friends
    return user.friends.size
}

fun main() {
    // Creates some sample users
    val user1 = User(1, "Alice", listOf(2, 3))
    val user2 = User(2, "Bob", listOf(1))
    val user3 = User(3, "Charlie", listOf(1))

    // Creates a map of users
    val users = mapOf(1 to user1, 2 to user2, 3 to user3)

    println(getNumberOfFriends(users, 1))
    // 2
    println(getNumberOfFriends(users, 2))
    // 1
    println(getNumberOfFriends(users, 4))
    // -1
}
```
{kotlin-runnable="true" id="kotlin-tour-null-safety-early-return"}

Neste exemplo:

* Há uma data class `User` com propriedades para o `id`, o `name` e a lista de amigos do usuário.
* A função `getNumberOfFriends()`:
  * Recebe um mapa de instâncias de `User` e um ID de usuário como inteiro.
  * Acessa o valor do mapa de instâncias de `User` com o ID de usuário fornecido.
  * Usa um operador Elvis para retornar a função antecipadamente com o valor `-1` se o valor do mapa for `null`.
  * Atribui o valor encontrado no mapa à variável `user`.
  * Retorna o número de amigos da lista de amigos do usuário usando a propriedade `size`.
* A função `main()`:
  * Cria três instâncias de `User`.
  * Cria um mapa dessas instâncias de `User` e o atribui à variável `users`.
  * Chama `getNumberOfFriends()` com `users` e os valores `1` e `2`, que retornam dois amigos para `"Alice"` e um amigo para `"Bob"`.
  * Chama `getNumberOfFriends()` com `users` e o valor `4`, o que dispara um retorno antecipado com o valor `-1`.

Você pode notar que o código poderia ser mais conciso sem o retorno antecipado. No entanto, essa abordagem exige várias chamadas seguras, porque `users[userId]` pode retornar `null`, o que deixa o código um pouco mais difícil de ler:

```kotlin
fun getNumberOfFriends(users: Map<Int, User>, userId: Int): Int {
    // Retrieve the user or return -1 if not found
    return users[userId]?.friends?.size ?: -1
}
```
{validate="false"}

Embora este exemplo verifique apenas uma condição com o operador Elvis, você pode adicionar várias verificações para cobrir qualquer caminho de erro crítico. Retornos antecipados com o operador Elvis evitam que o programa faça trabalho desnecessário e tornam o código mais seguro, pois param assim que um valor `null` ou um caso inválido é detectado.

Para mais informações sobre como usar `return` no seu código, veja [Retornos e saltos](returns.md).

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Validar dados do usuário com safe casts e o operador Elvis" id="null-safety-exercise-1">

Você está desenvolvendo um sistema de notificações para um app em que os usuários podem ativar ou desativar diferentes tipos de notificação. Complete a função `getNotificationPreferences()` para que:

1. A variável `validUser` use o operador `as?` para verificar se `user` é uma instância da classe `User`. Se não for, retorne uma lista vazia.
2. A variável `userName` use o operador Elvis `?:` para garantir que o nome do usuário seja `"Guest"` caso ele seja `null`.
3. A instrução de retorno final use a função `.takeIf()` para incluir as preferências de notificação por e-mail e por SMS somente se estiverem ativadas.
4. A função `main()` seja executada com sucesso e imprima a saída esperada.

> A [função `takeIf()`](scope-functions.md#takeif-and-takeunless) retorna o valor original se a condição dada for verdadeira, caso contrário retorna `null`. Por exemplo:
>
> ```kotlin
> fun main() {
>     // The user is logged in
>     val userIsLoggedIn = true
>     // The user has an active session
>     val hasSession = true
> 
>     // Gives access to the dashboard if the user is logged in
>     // and has an active session
>     val canAccessDashboard = userIsLoggedIn.takeIf { hasSession }
> 
>     println(canAccessDashboard ?: "Access denied")
>     // true
> }
> ```
>
{style = "tip"}

```kotlin
data class User(val name: String?)

fun getNotificationPreferences(user: Any, emailEnabled: Boolean, smsEnabled: Boolean): List<String> {
    val validUser = // Write your code here
    val userName = // Write your code here

    return listOfNotNull( /* Write your code here */)
}

fun main() {
    val user1 = User("Alice")
    val user2 = User(null)
    val invalidUser = "NotAUser"

    println(getNotificationPreferences(user1, emailEnabled = true, smsEnabled = false))
    // [Email Notifications enabled for Alice]
    println(getNotificationPreferences(user2, emailEnabled = false, smsEnabled = true))
    // [SMS Notifications enabled for Guest]
    println(getNotificationPreferences(invalidUser, emailEnabled = true, smsEnabled = true))
    // []
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/GetNotificationPreferencesTest.kt" validate="false" id="kotlin-tour-null-safety-exercise-1"}

```kotlin
data class User(val name: String?)

fun getNotificationPreferences(user: Any, emailEnabled: Boolean, smsEnabled: Boolean): List<String> {
    val validUser = user as? User ?: return emptyList()
    val userName = validUser.name ?: "Guest"

    return listOfNotNull(
        "Email Notifications enabled for $userName".takeIf { emailEnabled },
        "SMS Notifications enabled for $userName".takeIf { smsEnabled }
    )
}

fun main() {
    val user1 = User("Alice")
    val user2 = User(null)
    val invalidUser = "NotAUser"

    println(getNotificationPreferences(user1, emailEnabled = true, smsEnabled = false))
    // [Email Notifications enabled for Alice]
    println(getNotificationPreferences(user2, emailEnabled = false, smsEnabled = true))
    // [SMS Notifications enabled for Guest]
    println(getNotificationPreferences(invalidUser, emailEnabled = true, smsEnabled = true))
    // []
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/GetNotificationPreferencesTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-null-safety-solution-1"}

</def>
<def title="Encontrar uma única assinatura ativa com singleOrNull()" id="null-safety-exercise-2">

Você está trabalhando em um serviço de streaming por assinatura, em que os usuários podem ter várias assinaturas, mas **apenas uma pode estar ativa por vez**. Complete a função `getActiveSubscription()` para que ela use a função `singleOrNull()` com um predicado e retorne um valor `null` se houver mais de uma assinatura ativa:

```kotlin
data class Subscription(val name: String, val isActive: Boolean)

fun getActiveSubscription(subscriptions: List<Subscription>): Subscription? = TODO("Replace the TODO() function")

fun main() {
    val userWithPremiumPlan = listOf(
        Subscription("Basic Plan", false),
        Subscription("Premium Plan", true)
    )

    val userWithConflictingPlans = listOf(
        Subscription("Basic Plan", true),
        Subscription("Premium Plan", true)
    )

    println(getActiveSubscription(userWithPremiumPlan))
    // Subscription(name=Premium Plan, isActive=true)

    println(getActiveSubscription(userWithConflictingPlans))
    // null
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/GetActiveSubscriptionTest.kt" validate="false" id="kotlin-tour-null-safety-exercise-2"}

```kotlin
data class Subscription(val name: String, val isActive: Boolean)

fun getActiveSubscription(subscriptions: List<Subscription>): Subscription? {
    return subscriptions.singleOrNull { subscription -> subscription.isActive }
}

fun main() {
    val userWithPremiumPlan = listOf(
        Subscription("Basic Plan", false),
        Subscription("Premium Plan", true)
    )

    val userWithConflictingPlans = listOf(
        Subscription("Basic Plan", true),
        Subscription("Premium Plan", true)
    )

    println(getActiveSubscription(userWithPremiumPlan))
    // Subscription(name=Premium Plan, isActive=true)

    println(getActiveSubscription(userWithConflictingPlans))
    // null
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/GetActiveSubscriptionTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo 1" id="kotlin-tour-null-safety-solution-2-1"}

```kotlin
data class Subscription(val name: String, val isActive: Boolean)

fun getActiveSubscription(subscriptions: List<Subscription>): Subscription? =
    subscriptions.singleOrNull { it.isActive }

fun main() {
    val userWithPremiumPlan = listOf(
        Subscription("Basic Plan", false),
        Subscription("Premium Plan", true)
    )

    val userWithConflictingPlans = listOf(
        Subscription("Basic Plan", true),
        Subscription("Premium Plan", true)
    )

    println(getActiveSubscription(userWithPremiumPlan))
    // Subscription(name=Premium Plan, isActive=true)

    println(getActiveSubscription(userWithConflictingPlans))
    // null
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/GetActiveSubscriptionTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo 2" id="kotlin-tour-null-safety-solution-2-2"}

</def>
<def title="Filtrar nomes de usuário ativos com mapNotNull()" id="null-safety-exercise-3">

Você está trabalhando em uma plataforma de redes sociais em que os usuários têm nomes de usuário e status de conta. Você quer ver a lista de nomes de usuário atualmente ativos. Complete a função `getActiveUsernames()` para que a [função `mapNotNull()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-not-null.html) tenha um predicado que retorne o nome de usuário se ele estiver ativo ou um valor `null` se não estiver:

```kotlin
data class User(val username: String, val isActive: Boolean)

fun getActiveUsernames(users: List<User>): List<String> {
    return users.mapNotNull { /* Write your code here */ }
}

fun main() {
    val allUsers = listOf(
        User("alice123", true),
        User("bob_the_builder", false),
        User("charlie99", true)
    )

    println(getActiveUsernames(allUsers))
    // [alice123, charlie99]
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/GetActiveUsernamesTest.kt" validate="false" id="kotlin-tour-null-safety-exercise-3"}

> Assim como no Exercício 1, você pode usar a [função `takeIf()`](scope-functions.md#takeif-and-takeunless) para verificar se o usuário está ativo.
>
{ style = "tip" }

```kotlin
data class User(val username: String, val isActive: Boolean)

fun getActiveUsernames(users: List<User>): List<String> {
    return users.mapNotNull { user ->
        if (user.isActive) user.username else null
    }
}

fun main() {
    val allUsers = listOf(
        User("alice123", true),
        User("bob_the_builder", false),
        User("charlie99", true)
    )

    println(getActiveUsernames(allUsers))
    // [alice123, charlie99]
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/GetActiveUsernamesTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo 1" id="kotlin-tour-null-safety-solution-3-1"}

```kotlin
data class User(val username: String, val isActive: Boolean)

fun getActiveUsernames(users: List<User>): List<String> =
    users.mapNotNull { user -> user.username.takeIf { user.isActive } }

fun main() {
    val allUsers = listOf(
        User("alice123", true),
        User("bob_the_builder", false),
        User("charlie99", true)
    )

    println(getActiveUsernames(allUsers))
    // [alice123, charlie99]
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/GetActiveUsernamesTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo 2" id="kotlin-tour-null-safety-solution-3-2"}

</def>
<def title="Validar o estoque com retornos antecipados e o operador Elvis" id="null-safety-exercise-4">

Você está trabalhando em um sistema de gestão de estoque para uma plataforma de e-commerce. Antes de processar uma venda, precisa verificar se a quantidade solicitada de um produto é válida com base no estoque disponível.

Complete a função `validateStock()` para que ela use retornos antecipados e o operador Elvis (quando aplicável) para verificar se:

* A variável `requested` é `null`.
* A variável `available` é `null`.
* A variável `requested` é um valor negativo.
* A quantidade na variável `requested` é maior que a quantidade na variável `available`.

Em todos os casos acima, a função deve retornar antecipadamente com o valor `-1`.

```kotlin
fun validateStock(requested: Int?, available: Int?): Int {
    // Write your code here
}

fun main() {
    println(validateStock(5,10))
    // 5
    println(validateStock(null,10))
    // -1
    println(validateStock(-2,10))
    // -1
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/ValidateStockTest.kt" validate="false" id="kotlin-tour-null-safety-exercise-4"}

```kotlin
fun validateStock(requested: Int?, available: Int?): Int {
    val validRequested = requested ?: return -1
    val validAvailable = available ?: return -1

    if (validRequested < 0) return -1
    if (validRequested > validAvailable) return -1

    return validRequested
}

fun main() {
    println(validateStock(5,10))
    // 5
    println(validateStock(null,10))
    // -1
    println(validateStock(-2,10))
    // -1
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/ValidateStockTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-null-safety-solution-4"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-intermediate-properties.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-intermediate-libraries-and-apis.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->
