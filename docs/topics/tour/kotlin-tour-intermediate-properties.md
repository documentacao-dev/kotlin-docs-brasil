[//]: # (title: Propriedades)

<no-index/>


No tour para iniciantes, você aprendeu como as propriedades são usadas para declarar características de instâncias de classes e como acessá-las.
Este capítulo aprofunda como as propriedades funcionam em Kotlin e explora outras maneiras de usá-las no seu código.

## Campos de suporte {id="backing-fields"}

Em Kotlin, as propriedades têm funções `get()` e `set()` padrão, conhecidas como acessores de propriedade, que cuidam de obter e modificar
os seus valores. Embora essas funções padrão não fiquem explicitamente visíveis no código, o compilador as gera automaticamente
para gerenciar o acesso à propriedade nos bastidores. Esses acessores usam um **campo de suporte** para armazenar
o valor real da propriedade.

Campos de suporte existem se uma das duas condições a seguir for verdadeira:

* Você usa as funções padrão `get()` ou `set()` da propriedade.
* Você tenta acessar o valor da propriedade no código usando a palavra-chave `field`.

> As funções `get()` e `set()` também são chamadas de getters e setters.
>
{style="tip"}

Por exemplo, este código tem a propriedade `category`, que não tem funções `get()` ou `set()` personalizadas e, por isso, usa
as implementações padrão:

```kotlin
class Contact(val id: Int, var email: String) {
    var category: String = ""
}
```

Nos bastidores, isso é equivalente a este pseudocódigo:

```kotlin
class Contact(val id: Int, var email: String) {
    var category: String = ""
        get() = field
        set(value) {
            field = value
        }
}
```
{validate="false"}

Neste exemplo:

* A função `get()` obtém o valor da propriedade a partir do campo: `""`.
* A função `set()` aceita `value` como parâmetro e o atribui ao campo, em que `value` é `""`.

O acesso ao campo de suporte é útil quando você quer adicionar lógica extra nas funções `get()` ou `set()`
sem causar um loop infinito. Por exemplo, você tem uma classe `Person` com a propriedade `name`:


```kotlin
class Person {
    var name: String = ""
}
```

Você quer garantir que a primeira letra da propriedade `name` seja maiúscula, então cria uma função `set()` personalizada
que usa as funções de extensão [`.replaceFirstChar()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/replace-first-char.html)
e [`.uppercase()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/uppercase-char.html).
No entanto, se você se referir à propriedade diretamente na função `set()`, cria um loop infinito e recebe um `StackOverflowError`
em tempo de execução:

```kotlin
class Person {
    var name: String = ""
        set(value) {
            // This causes a runtime error
            name = value.replaceFirstChar { firstChar -> firstChar.uppercase() }
        }
}

fun main() {
    val person = Person()
    person.name = "kodee"
    println(person.name)
    // Exception in thread "main" java.lang.StackOverflowError
}
```
{validate="false" kotlin-runnable="true" id="kotlin-tour-properties-stackoverflow"}

Para corrigir isso, use o campo de suporte na função `set()`, referenciando-o com a palavra-chave `field`:

```kotlin
class Person {
    var name: String = ""
        set(value) {
            field = value.replaceFirstChar { firstChar -> firstChar.uppercase() }
        }
}

fun main() {
    val person = Person()
    person.name = "kodee"
    println(person.name)
    // Kodee
}
```
{kotlin-runnable="true" id="kotlin-tour-properties-backingfield"}

Campos de suporte também são úteis quando você quer adicionar logging, enviar notificações quando o valor de uma propriedade muda,
ou usar lógica adicional que compara os valores antigo e novo da propriedade.

Para mais informações, veja [Campos de suporte](properties.md#backing-fields).

## Propriedades de extensão {id="extension-properties"}

Assim como as funções de extensão, também existem propriedades de extensão. Elas permitem adicionar novas propriedades
a classes existentes sem modificar o código-fonte delas. No entanto, propriedades de extensão em Kotlin **não** têm campos de suporte.
Isso significa que você precisa escrever as funções `get()` e `set()` por conta própria. Além disso, a ausência de campo de suporte
faz com que elas não possam armazenar nenhum estado.

Para declarar uma propriedade de extensão, escreva o nome da classe que você quer estender, seguido de `.` e do nome da
sua propriedade. Assim como nas propriedades comuns de classe, você precisa declarar um tipo para a sua propriedade.
Por exemplo:

```kotlin
val String.lastChar: Char
```
{validate="false"}

Propriedades de extensão são mais úteis quando você quer que uma propriedade contenha um valor calculado sem usar herança.
Você pode pensar nas propriedades de extensão como uma função com apenas um parâmetro: o receiver.

Por exemplo, suponha que você tenha uma data class chamada `Person` com duas propriedades: `firstName` e `lastName`.

```kotlin
data class Person(val firstName: String, val lastName: String)
```

Você quer poder acessar o nome completo da pessoa sem modificar a data class `Person` nem herdar dela.
Você pode fazer isso criando uma propriedade de extensão com uma função `get()` personalizada:

```kotlin
data class Person(val firstName: String, val lastName: String)

// Extension property to get the full name
val Person.fullName: String
    get() = "$firstName $lastName"

fun main() {
    val person = Person(firstName = "John", lastName = "Doe")

    // Use the extension property
    println(person.fullName)
    // John Doe
}
```
{kotlin-runnable="true" id="kotlin-tour-properties-extension"}

> Propriedades de extensão não podem sobrescrever propriedades existentes de uma classe.
>
{style="note"}

Assim como acontece com as funções de extensão, a biblioteca padrão do Kotlin usa propriedades de extensão amplamente. Por exemplo,
veja a [propriedade `lastIndex`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/last-index.html) de um `CharSequence`.

## Propriedades delegadas {id="delegated-properties"}

Você já aprendeu sobre delegação no capítulo [Classes e interfaces](kotlin-tour-intermediate-classes-interfaces.md#delegation). Você também
pode usar delegação com propriedades para delegar os acessores de propriedade a outro objeto. Isso é útil
quando você tem requisitos mais complexos para armazenar propriedades que um simples campo de suporte não consegue tratar, como guardar
valores em uma tabela de banco de dados, em uma sessão do navegador ou em um map. Usar propriedades delegadas também reduz código repetitivo, porque a
lógica de obter e definir as propriedades fica contida somente no objeto para o qual você delega.

A sintaxe é parecida com a de delegação em classes, mas atua em outro nível. Declare sua propriedade, seguida da
palavra-chave `by` e do objeto para o qual você quer delegar. Por exemplo:

```kotlin
val displayName: String by Delegate
```

Aqui, a propriedade delegada `displayName` se refere ao objeto `Delegate` para os seus acessores de propriedade.

Todo objeto para o qual você delega **deve** ter uma função de operador `getValue()`, que o Kotlin usa para obter o valor
da propriedade delegada. Se a propriedade for mutável, ele também deve ter uma função de operador `setValue()` para que o Kotlin possa definir o seu valor.

Por padrão, as funções `getValue()` e `setValue()` têm a seguinte construção:

```kotlin
operator fun getValue(thisRef: Any?, property: KProperty<*>): String {}

operator fun setValue(thisRef: Any?, property: KProperty<*>, value: String) {}
```
{validate="false"}

Nessas funções:

* A palavra-chave `operator` marca essas funções como funções de operador, permitindo que elas sobrecarreguem as funções `get()` e `set()`.
* O parâmetro `thisRef` se refere ao objeto **que contém** a propriedade delegada. Por padrão, o tipo é definido como `Any?`, mas você pode precisar declarar um tipo mais específico.
* O parâmetro `property` se refere à propriedade cujo valor é acessado ou alterado. Você pode usar esse parâmetro para acessar informações
como o nome ou o tipo da propriedade. Por padrão, o tipo é definido como `KProperty<*>`, mas você também pode usar `Any?`. Você não precisa se preocupar em alterar isso no código.

A função `getValue()` tem o tipo de retorno `String` por padrão, mas você pode ajustar isso se quiser.

A função `setValue()` tem um parâmetro adicional `value`, que guarda o novo valor atribuído à
propriedade.

Então, como isso fica na prática? Suponha que você queira ter uma propriedade calculada, como o nome de exibição de um usuário, que é calculada
apenas uma vez porque a operação é cara e o seu app é sensível a desempenho. Você pode usar uma propriedade delegada
para guardar em cache o nome de exibição, de modo que ele seja calculado apenas uma vez, mas possa ser acessado a qualquer momento sem impacto no desempenho.

Primeiro, você precisa criar o objeto para o qual vai delegar. Neste caso, o objeto será uma instância da classe `CachedStringDelegate`:

```kotlin
class CachedStringDelegate {
    var cachedValue: String? = null
}
```

A propriedade `cachedValue` contém o valor em cache. Dentro da classe `CachedStringDelegate`, adicione à função de operador `getValue()`
o comportamento que você quer da função `get()` da propriedade delegada:

```kotlin
class CachedStringDelegate {
    var cachedValue: String? = null

    operator fun getValue(thisRef: Any?, property: Any?): String {
        if (cachedValue == null) {
            cachedValue = "Default Value"
            println("Computed and cached: $cachedValue")
        } else {
            println("Accessed from cache: $cachedValue")
        }
        return cachedValue ?: "Unknown"
    }
}
```

A função `getValue()` verifica se a propriedade `cachedValue` é `null`. Se for, a função atribui
`"Default value"` e imprime uma string para fins de log. Se a propriedade `cachedValue` já foi calculada, ela
não é `null`. Nesse caso, outra string é impressa para fins de log. Por fim, a função usa o operador Elvis
para retornar o valor em cache ou `"Unknown"` se o valor for `null`.

Agora você pode delegar a propriedade que quer guardar em cache (`val displayName`) para uma instância da classe `CachedStringDelegate`:

```kotlin
class CachedStringDelegate {
    var cachedValue: String? = null

    operator fun getValue(thisRef: User, property: Any?): String {
        if (cachedValue == null) {
            cachedValue = "${thisRef.firstName} ${thisRef.lastName}"
            println("Computed and cached: $cachedValue")
        } else {
            println("Accessed from cache: $cachedValue")
        }
        return cachedValue ?: "Unknown"
    }
}

class User(val firstName: String, val lastName: String) {
    val displayName: String by CachedStringDelegate()
}

fun main() {
    val user = User("John", "Doe")

    // First access computes and caches the value
    println(user.displayName)
    // Computed and cached: John Doe
    // John Doe

    // Subsequent accesses retrieve the value from cache
    println(user.displayName)
    // Accessed from cache: John Doe
    // John Doe
}
```
{kotlin-runnable="true" id="kotlin-tour-properties-delegated"}

Este exemplo:

* Cria uma classe `User` que tem duas propriedades no cabeçalho, `firstName` e `lastName`, e uma propriedade no corpo da classe, `displayName`.
* Delega a propriedade `displayName` para uma instância da classe `CachedStringDelegate`.
* Cria uma instância da classe `User` chamada `user`.
* Imprime o resultado de acessar a propriedade `displayName` na instância `user`.

Observe que, na função `getValue()`, o tipo do parâmetro `thisRef` é restringido de `Any?` para o tipo do objeto:
`User`. Isso é para que o compilador consiga acessar as propriedades `firstName` e `lastName` da classe `User`.

### Delegates padrão {id="standard-delegates"}

A biblioteca padrão do Kotlin oferece alguns delegates úteis para que você nem sempre precise criar os seus do zero.
Se você usar um desses delegates, não precisa definir as funções `getValue()` e `setValue()`, porque a biblioteca padrão
as fornece automaticamente.

#### Propriedades lazy {id="lazy-properties"}

Para inicializar uma propriedade somente quando ela é acessada pela primeira vez, use uma propriedade lazy. A biblioteca padrão oferece a
interface `Lazy` para delegação.

Para criar uma instância da interface `Lazy`, use a função `lazy()`, fornecendo a ela
uma expressão lambda a ser executada quando a função `get()` for chamada pela primeira vez. Chamadas seguintes da função `get()`
retornam o mesmo resultado fornecido na primeira chamada. Propriedades lazy usam a sintaxe de [lambda final](kotlin-tour-functions.md#trailing-lambdas)
para passar a expressão lambda.

Por exemplo:

```kotlin
class Database {
    fun connect() {
        println("Connecting to the database...")
    }

    fun query(sql: String): List<String> {
        return listOf("Data1", "Data2", "Data3")
    }
}

val databaseConnection: Database by lazy {
    val db = Database()
    db.connect()
    db
}

fun fetchData() {
    val data = databaseConnection.query("SELECT * FROM data")
    println("Data: $data")
}

fun main() {
    // First time accessing databaseConnection
    fetchData()
    // Connecting to the database...
    // Data: [Data1, Data2, Data3]

    // Subsequent access uses the existing connection
    fetchData()
    // Data: [Data1, Data2, Data3]
}
```
{kotlin-runnable="true" id="kotlin-tour-properties-lazy"}

Neste exemplo:

* Há uma classe `Database` com as funções membro `connect()` e `query()`.
* A função `connect()` imprime uma string no console, e a função `query()` aceita uma consulta SQL e retorna uma lista.
* Há uma propriedade `databaseConnection`, que é uma propriedade lazy.
* A expressão lambda fornecida à função `lazy()`:
  * Cria uma instância da classe `Database`.
  * Chama a função membro `connect()` nessa instância (`db`).
  * Retorna a instância.
* Há uma função `fetchData()` que:
  * Cria uma consulta SQL chamando a função `query()` na propriedade `databaseConnection`.
  * Atribui a consulta SQL à variável `data`.
  * Imprime a variável `data` no console.
* A função `main()` chama a função `fetchData()`. Na primeira vez que ela é chamada, a propriedade lazy é inicializada.
Na segunda vez, é retornado o mesmo resultado da primeira chamada.

Propriedades lazy são úteis não só quando a inicialização consome muitos recursos, mas também quando uma propriedade pode não ser usada
no seu código. Além disso, propriedades lazy são thread-safe por padrão, o que é especialmente útil se você estiver trabalhando
em um ambiente concorrente.

Para mais informações, veja [Propriedades lazy](delegated-properties.md#lazy-properties).

#### Propriedades observáveis {id="observable-properties"}

Para monitorar se o valor de uma propriedade muda, use uma propriedade observável. Uma propriedade observável é útil quando
você quer detectar uma mudança no valor da propriedade e usar essa informação para disparar uma reação. A biblioteca padrão oferece
o objeto `Delegates` para delegação.

Para criar uma propriedade observável, primeiro você precisa importar `kotlin.properties.Delegates.observable`. Depois, use a função `observable()`
e forneça a ela uma expressão lambda a ser executada sempre que a propriedade mudar. Assim como nas propriedades lazy,
propriedades observáveis usam a sintaxe de [lambda final](kotlin-tour-functions.md#trailing-lambdas) para passar a expressão lambda.

Por exemplo:

```kotlin
import kotlin.properties.Delegates.observable

class Thermostat {
    var temperature: Double by observable(20.0) { _, old, new ->
        if (new > 25) {
            println("Warning: Temperature is too high! ($old°C -> $new°C)")
        } else {
            println("Temperature updated: $old°C -> $new°C")
        }
    }
}

fun main() {
    val thermostat = Thermostat()
    thermostat.temperature = 22.5
    // Temperature updated: 20.0°C -> 22.5°C

    thermostat.temperature = 27.0
    // Warning: Temperature is too high! (22.5°C -> 27.0°C)
}
```
{kotlin-runnable="true" id="kotlin-tour-properties-observable"}

Neste exemplo:

* Há uma classe `Thermostat` que contém uma propriedade observável: `temperature`.
* A função `observable()` aceita `20.0` como parâmetro e o usa para inicializar a propriedade.
* A expressão lambda fornecida à função `observable()`:
  * Tem três parâmetros:
    * `_`, que se refere à própria propriedade.
    * `old`, que é o valor antigo da propriedade.
    * `new`, que é o valor novo da propriedade.
  * Verifica se o parâmetro `new` é maior que `25` e, dependendo do resultado, imprime uma string no console.
* A função `main()`:
  * Cria uma instância da classe `Thermostat` chamada `thermostat`.
  * Atualiza o valor da propriedade `temperature` da instância para `22.5`, o que dispara um print com a atualização da temperatura.
  * Atualiza o valor da propriedade `temperature` da instância para `27.0`, o que dispara um print com um aviso.

Propriedades observáveis são úteis não só para fins de logging e depuração. Você também pode usá-las em casos como
atualizar uma interface gráfica ou fazer verificações adicionais, como validar a consistência dos dados.

Para mais informações, veja [Propriedades observáveis](delegated-properties.md#observable-properties).

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Encontre livros esgotados" id="properties-exercise-1">

Você gerencia um sistema de estoque de uma livraria. O estoque é armazenado em uma lista em que cada item representa a quantidade
de um livro específico. Por exemplo, `listOf(3, 0, 7, 12)` significa que a loja tem 3 exemplares do primeiro livro, 0 do segundo,
7 do terceiro e 12 do quarto.

Escreva uma função chamada `findOutOfStockBooks()` que retorna uma lista com os índices de todos os livros que estão esgotados.

<deflist collapsible="true">
    <def title="Dica 1">
        Use a propriedade de extensão <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/indices.html"><code>indices</code></a> da biblioteca padrão.
    </def>
</deflist>

<deflist collapsible="true">
    <def title="Dica 2">
        Você pode usar a função <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/build-list.html"><code>buildList()</code></a> para criar e gerenciar uma lista em vez de criar e retornar manualmente uma lista mutável. A função <code>buildList()</code> usa uma lambda com receiver, que você aprendeu nos capítulos anteriores.
    </def>
</deflist>

```kotlin
fun findOutOfStockBooks(inventory: List<Int>): List<Int> {
    // Write your code here
}

fun main() {
    val inventory = listOf(3, 0, 7, 0, 5)
    println(findOutOfStockBooks(inventory))
    // [1, 3]
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/FindOutOfStockBooksTest.kt" validate="false" id="kotlin-tour-properties-exercise-1"}

```kotlin
fun findOutOfStockBooks(inventory: List<Int>): List<Int> {
    val outOfStockIndices = mutableListOf<Int>()
    for (index in inventory.indices) {
        if (inventory[index] == 0) {
            outOfStockIndices.add(index)
        }
    }
    return outOfStockIndices
}

fun main() {
    val inventory = listOf(3, 0, 7, 0, 5)
    println(findOutOfStockBooks(inventory))
    // [1, 3]
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/FindOutOfStockBooksTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução 1" id="kotlin-tour-properties-solution-1-1"}

```kotlin
fun findOutOfStockBooks(inventory: List<Int>): List<Int> = buildList {
    for (index in inventory.indices) {
        if (inventory[index] == 0) {
            add(index)
        }
    }
}

fun main() {
    val inventory = listOf(3, 0, 7, 0, 5)
    println(findOutOfStockBooks(inventory))
    // [1, 3]
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/FindOutOfStockBooksTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução 2" id="kotlin-tour-properties-solution-1-2"}

</def>
<def title="Converta quilômetros em milhas" id="properties-exercise-2">

Você tem um app de viagens que precisa exibir distâncias em quilômetros e em milhas. Crie uma propriedade de extensão para o tipo
`Double` chamada `asMiles` para converter uma distância em quilômetros para milhas:

> A fórmula para converter quilômetros em milhas é `miles = kilometers * 0.621371`.
>
{style="note"}

<deflist collapsible="true">
    <def title="Dica">
        Lembre-se de que propriedades de extensão precisam de uma função <code>get()</code> personalizada.
    </def>
</deflist>

```kotlin
val // Write your code here

fun main() {
    val distanceKm = 5.0
    println("$distanceKm km is ${distanceKm.asMiles} miles")
    // 5.0 km is 3.106855 miles

    val marathonDistance = 42.195
    println("$marathonDistance km is ${marathonDistance.asMiles} miles")
    // 42.195 km is 26.218749345 miles
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/AsMilesTest.kt" validate="false" id="kotlin-tour-properties-exercise-2"}

```kotlin
val Double.asMiles: Double
    get() = this * 0.621371

fun main() {
    val distanceKm = 5.0
    println("$distanceKm km is ${distanceKm.asMiles} miles")
    // 5.0 km is 3.106855 miles

    val marathonDistance = 42.195
    println("$marathonDistance km is ${marathonDistance.asMiles} miles")
    // 42.195 km is 26.218749345 miles
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/AsMilesTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-properties-solution-2"}

</def>
<def title="Inicialize verificações de saúde de forma lazy" id="properties-exercise-3">

Você tem um verificador de saúde de sistema que pode determinar o estado de um sistema em nuvem. No entanto, as duas funções que ele pode executar
para fazer uma verificação de saúde consomem muitos recursos. Use propriedades lazy para inicializar as verificações, de modo que as
funções custosas só sejam executadas quando necessário:

```kotlin
fun checkAppServer(): Boolean {
    println("Performing application server health check...")
    return true
}

fun checkDatabase(): Boolean {
    println("Performing database health check...")
    return false
}

fun main() {
    // Write your code here

    when {
        isAppServerHealthy -> println("Application server is online and healthy")
        isDatabaseHealthy -> println("Database is healthy")
        else -> println("System is offline")
    }
    // Performing application server health check...
    // Application server is online and healthy
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/LazyHealthCheckTest.kt" validate="false" id="kotlin-tour-properties-exercise-3"}

```kotlin
fun checkAppServer(): Boolean {
    println("Performing application server health check...")
    return true
}

fun checkDatabase(): Boolean {
    println("Performing database health check...")
    return false
}

fun main() {
    val isAppServerHealthy by lazy { checkAppServer() }
    val isDatabaseHealthy by lazy { checkDatabase() }

    when {
        isAppServerHealthy -> println("Application server is online and healthy")
        isDatabaseHealthy -> println("Database is healthy")
        else -> println("System is offline")
    }
   // Performing application server health check...
   // Application server is online and healthy
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/LazyHealthCheckTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-properties-solution-3"}

</def>
<def title="Acompanhe mudanças de orçamento" id="properties-exercise-4">

Você está criando um app simples de controle de orçamento. O app precisa observar as mudanças no orçamento restante do usuário e avisá-lo
sempre que ele ficar abaixo de um certo limite. Você tem uma classe `Budget` que é inicializada com a propriedade `totalBudget`,
que contém o valor inicial do orçamento. Dentro da classe, crie uma propriedade observável chamada `remainingBudget` que imprime:

* Um aviso quando o valor for menor que 20% do orçamento inicial.
* Uma mensagem de incentivo quando o orçamento aumentar em relação ao valor anterior.

```kotlin
import kotlin.properties.Delegates.observable

class Budget(val totalBudget: Int) {
    var remainingBudget: Int // Write your code here
}

fun main() {
    val myBudget = Budget(totalBudget = 1000)
    myBudget.remainingBudget = 800
    myBudget.remainingBudget = 150
    // Warning: Your remaining budget (150) is below 20% of your total budget.
    myBudget.remainingBudget = 50
    // Warning: Your remaining budget (50) is below 20% of your total budget.
    myBudget.remainingBudget = 300
    // Good news: Your remaining budget increased to 300.
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/BudgetTest.kt" validate="false" id="kotlin-tour-properties-exercise-4"}

```kotlin
import kotlin.properties.Delegates.observable

class Budget(val totalBudget: Int) {
    var remainingBudget: Int by observable(totalBudget) { _, oldValue, newValue ->
        if (newValue < totalBudget * 0.2) {
            println("Warning: Your remaining budget ($newValue) is below 20% of your total budget.")
        } else if (newValue > oldValue) {
            println("Good news: Your remaining budget increased to $newValue.")
        }
    }
}

fun main() {
    val myBudget = Budget(totalBudget = 1000)
    myBudget.remainingBudget = 800
    myBudget.remainingBudget = 150
    // Warning: Your remaining budget (150) is below 20% of your total budget.
    myBudget.remainingBudget = 50
    // Warning: Your remaining budget (50) is below 20% of your total budget.
    myBudget.remainingBudget = 300
    // Good news: Your remaining budget increased to 300.
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/intermediate/BudgetTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-properties-solution-4"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-intermediate-open-special-classes.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-intermediate-null-safety.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->
