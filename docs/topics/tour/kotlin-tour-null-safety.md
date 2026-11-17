[//]: # (title: Null safety)

<no-index/>


Em Kotlin, é possível ter um valor `null`. O Kotlin usa valores `null` quando algo está ausente ou ainda não foi definido.
Você já viu o Kotlin retornar um valor `null` no capítulo [Coleções](kotlin-tour-collections.md#kotlin-tour-map-no-key), quando tentou acessar um par chave-valor com uma chave que não existe no mapa. Embora seja útil usar valores `null` dessa forma, você pode ter problemas se seu código não estiver preparado para lidar com eles.

Para ajudar a evitar problemas com valores `null` nos seus programas, o Kotlin tem null safety. A null safety detecta possíveis problemas com valores `null` em tempo de compilação, e não em tempo de execução.

Null safety é uma combinação de recursos que permitem:

* Declarar explicitamente quando valores `null` são permitidos no seu programa.
* Verificar a presença de valores `null`.
* Usar chamadas seguras em propriedades ou funções que podem conter valores `null`.
* Declarar ações a serem tomadas se valores `null` forem detectados.

## Tipos nuláveis {id="nullable-types"}

O Kotlin oferece suporte a tipos nuláveis, que permitem que o tipo declarado tenha valores `null`. Por padrão, um tipo **não** pode aceitar valores `null`. Tipos nuláveis são declarados adicionando explicitamente `?` após a declaração do tipo.

Por exemplo:

```kotlin
fun main() {
    // neverNull has String type
    var neverNull: String = "This can't be null"

    // Throws a compiler error
    neverNull = null

    // nullable has nullable String type
    var nullable: String? = "You can keep a null here"

    // This is OK
    nullable = null

    // By default, null values aren't accepted
    var inferredNonNull = "The compiler assumes non-nullable"

    // Throws a compiler error
    inferredNonNull = null

    // notNull doesn't accept null values
    fun strLength(notNull: String): Int {                 
        return notNull.length
    }

    println(strLength(neverNull)) // 18
    println(strLength(nullable))  // Throws a compiler error
}
```
{kotlin-runnable="true" validate="false" id="kotlin-tour-nullable-type"}

> `length` é uma propriedade da classe [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/) que
> contém o número de caracteres de uma string.
>
{style="tip"}

## Verifique valores null {id="check-for-null-values"}

Você pode verificar a presença de valores `null` dentro de expressões condicionais. No exemplo a seguir, a função `describeString()`
tem uma instrução `if` que verifica se `maybeString` **não** é `null` e se o `length` dela é maior que zero:

```kotlin
fun describeString(maybeString: String?): String {
    if (maybeString != null && maybeString.length > 0) {
        return "String of length ${maybeString.length}"
    } else {
        return "Empty or null string"
    }
}

fun main() {
    val nullString: String? = null
    println(describeString(nullString))
    // Empty or null string
}
```
{kotlin-runnable="true" id="kotlin-tour-check-nulls"}

## Use chamadas seguras {id="use-safe-calls"}

Para acessar com segurança propriedades de um objeto que pode conter um valor `null`, use o operador de chamada segura `?.`. O operador de chamada segura
retorna `null` se o objeto ou uma das propriedades acessadas for `null`. Isso é útil se você quiser evitar que a presença de valores `null`
cause erros no seu código.

No exemplo a seguir, a função `lengthString()` usa uma chamada segura para retornar o comprimento da string ou `null`:

```kotlin
fun lengthString(maybeString: String?): Int? = maybeString?.length

fun main() { 
    val nullString: String? = null
    println(lengthString(nullString))
    // null
}
```
{kotlin-runnable="true" id="kotlin-tour-safe-call-property"}

> Chamadas seguras podem ser encadeadas, de modo que, se alguma propriedade de um objeto contiver um valor `null`, a chamada retorna `null` sem
> lançar um erro. Por exemplo:
> 
> ```kotlin
>   person.company?.address?.country
> ```
>
{style="tip"}

O operador de chamada segura também pode ser usado para chamar com segurança uma extension function ou uma função membro. Nesse caso, uma verificação de null é
realizada antes de a função ser chamada. Se a verificação detectar um valor `null`, a chamada é ignorada e `null` é retornado.

No exemplo a seguir, `nullString` é `null`, então a invocação de [`.uppercase()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/uppercase.html)
é ignorada e `null` é retornado:

```kotlin
fun main() {
    val nullString: String? = null
    println(nullString?.uppercase())
    // null
}
```
{kotlin-runnable="true" id="kotlin-tour-safe-call-function"}

## Use o operador Elvis {id="use-elvis-operator"}

Você pode fornecer um valor padrão para retornar caso um valor `null` seja detectado, usando o **operador Elvis** `?:`.

Escreva à esquerda do operador Elvis o que deve ser verificado quanto a um valor `null`.
Escreva à direita do operador Elvis o que deve ser retornado se um valor `null` for detectado.

No exemplo a seguir, `nullString` é `null`, então a chamada segura para acessar a propriedade `length` retorna um valor `null`.
Como resultado, o operador Elvis retorna `0`:

```kotlin
fun main() {
    val nullString: String? = null
    println(nullString?.length ?: 0)
    // 0
}
```
{kotlin-runnable="true" id="kotlin-tour-elvis-operator"}

Para mais informações sobre null safety em Kotlin, consulte [Null safety](null-safety.md).

## Prática {id="practice" completion-point="true"}

<deflist appearance="clear" collapsible="true">
<def title="Calcule o salário de um funcionário" id="null-safety-basics-exercise-1">

Você tem a função `employeeById`, que dá acesso a um banco de dados de funcionários de uma empresa. Infelizmente, essa função retorna um valor do tipo `Employee?`, então o resultado pode ser `null`.
Seu objetivo é escrever uma função que retorne o salário de um funcionário quando o `id` dele for informado, ou `0` se o funcionário não estiver no banco de dados.

```kotlin
data class Employee (val name: String, var salary: Int)

fun employeeById(id: Int) = when(id) {
    1 -> Employee("Mary", 20)
    2 -> null
    3 -> Employee("John", 21)
    4 -> Employee("Ann", 23)
    else -> null
}

fun salaryById(id: Int): Int = TODO() // Write your code here

fun main() {
    println((1..5).sumOf { id -> salaryById(id) })
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/SalaryByIdTest.kt" validate="false" id="kotlin-tour-null-safety-exercise"}

```kotlin
data class Employee (val name: String, var salary: Int)

fun employeeById(id: Int) = when(id) {
    1 -> Employee("Mary", 20)
    2 -> null
    3 -> Employee("John", 21)
    4 -> Employee("Ann", 23)
    else -> null
}

fun salaryById(id: Int): Int = employeeById(id)?.salary ?: 0

fun main() {
    println((1..5).sumOf { id -> salaryById(id) })
}
```
{kotlin-runnable="true" kotlin-target-platform="exercise" kotlin-hidden-files="ExerciseUtils.kt,tour/basics/SalaryByIdTest.kt" initial-collapse-state="collapsed" collapsible="true" collapsed-title="Solução de exemplo" id="kotlin-tour-null-safety-solution"}

</def>
</deflist>

## Próximos passos {id="what-s-next"}

Parabéns! Agora que você concluiu o tour para iniciantes, leve seu conhecimento de Kotlin para o próximo nível com
nosso tour intermediário:

<seealso></seealso>

<list columns="2" id="tour-nav">
  <li>
    <a as="button" href="kotlin-tour-classes.md" mode="outline" icon="arrow-left" icon-position="left">Passo anterior</a>
  </li>
  <li>
    <a as="button" href="kotlin-tour-intermediate-extension-functions.md" mode="classic" icon="arrow-right" icon-position="right">Começar o tour intermediário de Kotlin</a>
  </li>
</list>

<!-- ia-translate: true -->
