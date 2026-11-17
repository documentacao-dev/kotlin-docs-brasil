[//]: # (title: Classes)

<no-index/>


O Kotlin permite programação orientada a objetos com classes e objetos. Objetos são úteis para armazenar dados no
programa. Classes permitem declarar um conjunto de características para um objeto. Quando você cria objetos a partir de
uma classe, economiza tempo e esforço, porque não precisa declarar essas características toda vez.

Para declarar uma classe, use a palavra-chave `class`: 

```kotlin
class Customer
```

## Propriedades {id="properties"}

As características de um objeto de uma classe podem ser declaradas em propriedades. Você pode declarar propriedades para
uma classe:

* Dentro dos parênteses `()` depois do nome da classe.
```kotlin
class Contact(val id: Int, var email: String)
```

* Dentro do corpo da classe, definido por chaves `{}`.
```kotlin
class Contact(val id: Int, var email: String) {
    val category: String = ""
}
```

Recomendamos declarar propriedades como somente leitura (`val`), a menos que elas precisem ser alteradas depois que uma
instância da classe é criada.

Você pode declarar propriedades sem `val` ou `var` dentro dos parênteses, mas essas propriedades não ficam acessíveis
depois que uma instância é criada.

> * O conteúdo entre parênteses `()` é chamado de **cabeçalho da classe**.
> * Você pode usar uma [vírgula final](coding-conventions.md#trailing-commas) ao declarar propriedades da classe.
>
{style="note"}

Assim como nos parâmetros de função, as propriedades de uma classe podem ter valores padrão:
```kotlin
class Contact(val id: Int, var email: String = "example@gmail.com") {
    val category: String = "work"
}
```

## Criar instância {id="create-instance"}

Para criar um objeto a partir de uma classe, você declara uma **instância** da classe usando um **construtor**.

Por padrão, o Kotlin cria automaticamente um construtor com os parâmetros declarados no cabeçalho da classe.

Por exemplo:
```kotlin
class Contact(val id: Int, var email: String)

fun main() {
    val contact = Contact(1, "mary@gmail.com")
}
```
{kotlin-runnable="true" id="kotlin-tour-class-create-instance"}

No exemplo:

* `Contact` é uma classe.
* `contact` é uma instância da classe `Contact`.
* `id` e `email` são propriedades.
* `id` e `email` são usados com o construtor padrão para criar `contact`.

Classes em Kotlin podem ter vários construtores, incluindo os que você mesmo define. Para saber mais sobre como declarar
vários construtores, veja [Construtores](classes.md#constructors-and-initializer-blocks).

## Acessar propriedades {id="access-properties"}

Para acessar uma propriedade de uma instância, escreva o nome da propriedade depois do nome da instância, seguido de
um ponto `.`:

```kotlin
class Contact(val id: Int, var email: String)

fun main() {
    val contact = Contact(1, "mary@gmail.com")
    
    // Prints the value of the property: email
    println(contact.email)           
    // mary@gmail.com

    // Updates the value of the property: email
    contact.email = "jane@gmail.com"
    
    // Prints the new value of the property: email
    println(contact.email)           
    // jane@gmail.com
}
```
{kotlin-runnable="true" id="kotlin-tour-access-property"}

> Para concatenar o valor de uma propriedade como parte de uma string, você pode usar templates de string (`$`).
> Por exemplo:
> ```kotlin
> println("Their email address is: ${contact.email}")
> ```
>
{style="tip"}

## Funções membro {id="member-functions"}

Além de declarar propriedades como parte das características de um objeto, você também pode definir o comportamento de um
objeto com funções membro.

No Kotlin, funções membro devem ser declaradas dentro do corpo da classe. Para chamar uma função membro em uma instância,
escreva o nome da função depois do nome da instância, seguido de um ponto `.`. Por exemplo:

```kotlin
class Contact(val id: Int, var email: String) {
    fun printId() {
        println(id)
    }
}

fun main() {
    val contact = Contact(1, "mary@gmail.com")
    // Calls member function printId()
    contact.printId()           
    // 1
}
```
{kotlin-runnable="true" id="kotlin-tour-member-function"}

## Data classes

O Kotlin tem **data classes**, particularmente úteis para armazenar dados. Data classes têm a mesma funcionalidade das
classes comuns, mas vêm automaticamente com funções membro adicionais. Essas funções permitem imprimir a instância em uma
saída legível, comparar instâncias de uma classe, copiar instâncias e muito mais. Como essas funções estão disponíveis
automaticamente, você não precisa gastar tempo escrevendo o mesmo código repetitivo para cada classe.

Para declarar uma data class, use a palavra-chave `data`:

```kotlin
data class User(val name: String, val id: Int)
```

O compilador do Kotlin usa apenas as propriedades definidas dentro do [construtor primário](classes.md#primary-constructor)
ao gerar funções membro. Se você declarar propriedades no corpo da data class, elas não são incluídas na saída das
funções geradas.

As funções membro predefinidas mais úteis das data classes são:

| **Função**         | **Descrição**                                                                                   |
|--------------------|-------------------------------------------------------------------------------------------------|
| `toString()`       | Imprime uma string legível da instância da classe e de suas propriedades.                       |
| `equals()` ou `==` | Compara instâncias de uma classe.                                                               |
| `copy()`           | Cria uma instância da classe copiando outra, possivelmente com algumas propriedades diferentes. |

Veja as seções a seguir para exemplos de como usar cada função:

* [Imprimir como string](#print-as-string)
* [Comparar instâncias](#compare-instances)
* [Copiar instância](#copy-instance)

### Imprimir como string {id="print-as-string"}

Para imprimir uma string legível de uma instância de classe, você pode chamar explicitamente a função `toString()`, ou
usar funções de impressão (`println()` e `print()`), que chamam `toString()` automaticamente para você:

```kotlin
data class User(val name: String, val id: Int)

fun main() {
    //sampleStart
    val user = User("Alex", 1)
    
    // Automatically uses toString() function so that output is easy to read
    println(user)            
    // User(name=Alex, id=1)
    //sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-data-classes-print-string"}

Isso é especialmente útil na depuração ou na criação de logs.

### Comparar instâncias {id="compare-instances"}

Para comparar instâncias de data class, use o operador de igualdade `==`:

```kotlin
data class User(val name: String, val id: Int)

fun main() {
    //sampleStart
    val user = User("Alex", 1)
    val secondUser = User("Alex", 1)
    val thirdUser = User("Max", 2)

    // Compares user to second user
    println("user == secondUser: ${user == secondUser}") 
    // user == secondUser: true
    
    // Compares user to third user
    println("user == thirdUser: ${user == thirdUser}")   
    // user == thirdUser: false
    //sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-data-classes-compare-instances"}

### Copiar instância {id="copy-instance"}

Para criar uma cópia exata de uma instância de data class, chame a função `copy()` na instância.

Para criar uma cópia de uma instância de data class **e** alterar algumas propriedades, chame a função `copy()` na
instância **e** adicione valores de substituição para as propriedades como parâmetros da função.

Por exemplo:

```kotlin
data class User(val name: String, val id: Int)

fun main() {
    //sampleStart
    val user = User("Alex", 1)

    // Creates an exact copy of user
    println(user.copy())       
    // User(name=Alex, id=1)

    // Creates a copy of user with name: "Max"
    println(user.copy("Max"))  
    // User(name=Max, id=1)

    // Creates a copy of user with id: 3
    println(user.copy(id = 3)) 
    // User(name=Alex, id=3)
    //sampleEnd
}
```
{kotlin-runnable="true" id="kotlin-tour-data-classes-copy-instance"}

Criar uma cópia de uma instância é mais seguro do que modificar a instância original, porque qualquer código que dependa
da instância original não é afetado pela cópia nem pelo que você fizer com ela.

Para mais informações sobre data classes, veja [Data classes](data-classes.md).

O último capítulo deste tour trata da [null safety](kotlin-tour-null-safety.md) do Kotlin.

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true" numbered="true">
<def title="Declarar uma data class" id="classes-exercise-1">

Defina uma data class `Employee` com duas propriedades: uma para o nome e outra para o salário. Garanta que a propriedade
do salário seja mutável, senão você não vai receber um aumento no fim do ano! A função main demonstra como você pode usar
essa data class.

```kotlin
// Write your code here

fun main() {
    val emp = Employee("Mary", 20)
    println(emp)
    emp.salary += 10
    println(emp)
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/EmployeeTest.kt" validate="false" id="kotlin-tour-classes-exercise-1"}

```kotlin
data class Employee(val name: String, var salary: Int)

fun main() {
    val emp = Employee("Mary", 20)
    println(emp)
    emp.salary += 10
    println(emp)
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/EmployeeTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-classes-solution-1"}

</def>
<def title="Declarar data classes aninhadas" id="classes-exercise-2">

Declare as data classes adicionais que são necessárias para que este código compile.

```kotlin
data class Person(val name: Name, val address: Address, val ownsAPet: Boolean = true)
// Write your code here
// data class Name(...)

fun main() {
    val person = Person(
        Name("John", "Smith"),
        Address("123 Fake Street", City("Springfield", "US")),
        ownsAPet = false
    )
    println(person)
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/PersonTest.kt" validate="false" id="kotlin-tour-classes-exercise-2"}

```kotlin
data class Person(val name: Name, val address: Address, val ownsAPet: Boolean = true)
data class Name(val first: String, val last: String)
data class Address(val street: String, val city: City)
data class City(val name: String, val countryCode: String)

fun main() {
    val person = Person(
        Name("John", "Smith"),
        Address("123 Fake Street", City("Springfield", "US")),
        ownsAPet = false
    )
    println(person)
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/PersonTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-classes-solution-2"}

</def>
<def title="Gerar funcionários aleatórios com uma classe" id="classes-exercise-3">

Para testar seu código, você precisa de um gerador que crie funcionários aleatórios. Defina uma classe
`RandomEmployeeGenerator` com uma lista fixa de nomes possíveis (dentro do corpo da classe). Configure a classe com um
salário mínimo e um máximo (dentro do cabeçalho da classe). No corpo da classe, defina a função `generateEmployee()`.
Mais uma vez, a função main demonstra como você pode usar essa classe.

> Neste exercício, você importa um pacote para poder usar a função [`Random.nextInt()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.random/-random/next-int.html).
> Para mais informações sobre importação de pacotes, veja [Pacotes e importações](packages.md).
>
{style="tip"}

<deflist collapsible="true" id="kotlin-tour-classes-exercise-3-hint-1">
    <def title="Dica 1">
        Listas têm uma extension function chamada <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/random.html"><code>.random()</code></a>
        que retorna um item aleatório dentro de uma lista.
    </def>
</deflist>

<deflist collapsible="true" id="kotlin-tour-classes-exercise-3-hint-2">
    <def title="Dica 2">
        <code>Random.nextInt(from = ..., until = ...)</code> fornece um número <code>Int</code> aleatório dentro dos limites especificados.
    </def>
</deflist>

```kotlin
import kotlin.random.Random

data class Employee(val name: String, var salary: Int)

// Write your code here

fun main() {
    val empGen = RandomEmployeeGenerator(10, 30)
    println(empGen.generateEmployee())
    println(empGen.generateEmployee())
    println(empGen.generateEmployee())
    empGen.minSalary = 50
    empGen.maxSalary = 100
    println(empGen.generateEmployee())
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/RandomEmployeeGeneratorTest.kt" validate="false" id="kotlin-tour-classes-exercise-3"}

```kotlin
import kotlin.random.Random

data class Employee(val name: String, var salary: Int)

class RandomEmployeeGenerator(var minSalary: Int, var maxSalary: Int) {
    val names = listOf("John", "Mary", "Ann", "Paul", "Jack", "Elizabeth")
    fun generateEmployee() =
        Employee(names.random(),
            Random.nextInt(from = minSalary, until = maxSalary))
}

fun main() {
    val empGen = RandomEmployeeGenerator(10, 30)
    println(empGen.generateEmployee())
    println(empGen.generateEmployee())
    println(empGen.generateEmployee())
    empGen.minSalary = 50
    empGen.maxSalary = 100
    println(empGen.generateEmployee())
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/RandomEmployeeGeneratorTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Exemplo de solução" id="kotlin-tour-classes-solution-3"}

</def>
</deflist>

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-functions.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-null-safety.md" mode="classic" icon="arrow-right" icon-position="right">Próximo passo</a>
  </li>
</list>

<!-- ia-translate: true -->