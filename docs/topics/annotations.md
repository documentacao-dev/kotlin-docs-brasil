[//]: # (title: Anotações)

Anotações são tags que você pode usar para anexar metadados a elementos do seu código. Ferramentas e frameworks processam esses
metadados durante a compilação e em tempo de execução, e executam ações diferentes com base neles.

Você pode anotar seu código para simplificar e automatizar tarefas comuns, como gerar código repetitivo (boilerplate), impor padrões de codificação ou escrever documentação.

> Se você quiser desenvolver seus próprios processadores de anotações, pode usar a API [Kotlin Symbol Processing (KSP)](ksp-overview.md).
>
{style="tip"}

## Declaração {id="declaration"}

Anotações são um tipo especial de classe. Para declarar uma anotação, use a palavra-chave `annotation` antes da declaração da classe:

```kotlin
annotation class Fancy
```

Atributos adicionais da anotação podem ser especificados anotando a classe da anotação com meta-anotações:

  * [`@Target`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.annotation/-target/index.html) especifica os tipos possíveis de
    elementos que podem ser anotados com a anotação (como classes, funções, propriedades e expressões);
  * [`@Retention`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.annotation/-retention/index.html) especifica se a
    anotação é armazenada nos arquivos de classe compilados e se ela fica visível por reflexão em tempo de execução
    (por padrão, ambos são verdadeiros);
  * [`@Repeatable`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.annotation/-repeatable/index.html) permite usar a mesma anotação
    em um único elemento várias vezes;
  * [`@MustBeDocumented`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.annotation/-must-be-documented/index.html) especifica que a
    anotação faz parte da API pública e deve ser incluída na assinatura da classe ou do método exibida na
    documentação gerada da API.

```kotlin
@Target(AnnotationTarget.CLASS, AnnotationTarget.FUNCTION,
        AnnotationTarget.TYPE_PARAMETER, AnnotationTarget.VALUE_PARAMETER,
        AnnotationTarget.EXPRESSION)
@Retention(AnnotationRetention.SOURCE)
@MustBeDocumented
annotation class Fancy
```

## Uso {id="usage"}

```kotlin
@Fancy class Foo {
    @Fancy fun baz(@Fancy foo: Int): Int {
        return (@Fancy 1)
    }
}
```

Se você precisar anotar o construtor primário de uma classe, precisa adicionar a palavra-chave `constructor`
na declaração do construtor e colocar as anotações antes dela:

```kotlin
class Foo @Inject constructor(dependency: MyDependency) { ... }
```

Você também pode anotar os acessores de propriedades:

```kotlin
class Foo {
    var x: MyDependency? = null
        @Inject set
}
```

## Construtores {id="constructors"}

Anotações podem ter construtores que recebem parâmetros.

```kotlin
annotation class Special(val why: String)

@Special("example") class Foo {}
```

Os tipos de parâmetro permitidos são:

 * Tipos que correspondem aos tipos primitivos do Java (Int, Long etc.)
 * Strings
 * Classes (`Foo::class`)
 * Enums
 * Outras anotações
 * Arrays dos tipos listados acima

Parâmetros de anotação não podem ter tipos nullable, porque a JVM não oferece suporte a armazenar `null` como valor
de um atributo de anotação.

Se uma anotação for usada como parâmetro de outra anotação, seu nome não recebe o prefixo `@`:

```kotlin
annotation class ReplaceWith(val expression: String)

annotation class Deprecated(
        val message: String,
        val replaceWith: ReplaceWith = ReplaceWith(""))

@Deprecated("This function is deprecated, use === instead", ReplaceWith("this === other"))
```

Se você precisar especificar uma classe como argumento de uma anotação, use uma classe do Kotlin
([KClass](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html)). O compilador do Kotlin
converte automaticamente para uma classe Java, para que o código Java possa acessar as anotações e os argumentos
normalmente.

```kotlin

import kotlin.reflect.KClass

annotation class Ann(val arg1: KClass<*>, val arg2: KClass<out Any>)

@Ann(String::class, Int::class) class MyClass
```

## Instanciação {id="instantiation"}

Em Java, um tipo de anotação é uma forma de interface, então você pode implementá-lo e usar uma instância.
Como alternativa a esse mecanismo, o Kotlin permite chamar um construtor de uma classe de anotação em código arbitrário
e usar a instância resultante da mesma forma.

```kotlin
annotation class InfoMarker(val info: String)

fun processInfo(marker: InfoMarker): Unit = TODO()

fun main(args: Array<String>) {
    if (args.isNotEmpty())
        processInfo(getAnnotationReflective(args))
    else
        processInfo(InfoMarker("default"))
}
```

Saiba mais sobre a instanciação de classes de anotação neste [KEEP](https://github.com/Kotlin/KEEP/blob/master/proposals/annotation-instantiation.md).

## Lambdas

Anotações também podem ser usadas em lambdas. Elas são aplicadas ao método `invoke()` no qual o corpo
da lambda é gerado. Isso é útil para frameworks como o [Quasar](https://docs.paralleluniverse.co/quasar/),
que usa anotações para controle de concorrência.

```kotlin
annotation class Suspendable

val f = @Suspendable { Fiber.sleep(10) }
```

## Alvos de uso da anotação (use-site targets) {id="annotation-use-site-targets"}

Quando você anota uma propriedade ou um parâmetro do construtor primário, há vários elementos Java gerados a partir do
elemento Kotlin correspondente e, portanto, vários locais possíveis para a anotação no
bytecode Java gerado. Para especificar exatamente como a anotação deve ser gerada, use a seguinte sintaxe:

```kotlin
class Example(@field:Ann val foo,    // annotate only the Java field
              @get:Ann val bar,      // annotate only the Java getter
              @param:Ann val quux)   // annotate only the Java constructor parameter
```

A mesma sintaxe pode ser usada para anotar o arquivo inteiro. Para isso, coloque uma anotação com o alvo `file` no
nível superior do arquivo, antes da diretiva package ou antes de todos os imports, se o arquivo estiver no pacote padrão:

```kotlin
@file:JvmName("Foo")

package org.jetbrains.demo
```

Se você tiver várias anotações com o mesmo alvo, pode evitar repetir o alvo adicionando colchetes após o
alvo e colocando todas as anotações dentro dos colchetes (exceto para o meta-alvo `all`):

```kotlin
class Example {
     @set:[Inject VisibleForTesting]
     var collaborator: Collaborator
}
```

A lista completa de alvos de uso suportados é:

  * `file`
  * `field`
  * `property` (anotações com este alvo não são visíveis para o Java)
  * `get` (getter da propriedade)
  * `set` (setter da propriedade)
  * `all` (um meta-alvo para propriedades, veja a seção [meta-alvo `all`](#all-meta-target) para mais informações)
  * `receiver` (parâmetro receiver de uma função ou propriedade de extensão)

    Para anotar o parâmetro receiver de uma função de extensão, use a seguinte sintaxe:

    ```kotlin
    fun @receiver:Fancy String.myExtension() { ... }
    ```

  * `param` (parâmetro do construtor)
  * `setparam` (parâmetro do setter da propriedade)
  * `delegate` (o campo que armazena a instância de delegação de uma propriedade delegada)

### Valores padrão quando nenhum alvo de uso é especificado {id="defaults-when-no-use-site-targets-are-specified"}

Se você não especificar um alvo de uso, o compilador escolhe o alvo de acordo com a anotação `@Target` da anotação
que você está usando. Se houver vários alvos aplicáveis, o compilador escolhe um ou mais deles na seguinte ordem:

* O alvo de parâmetro do construtor (`param`).
* O alvo de propriedade (`property`).
* O alvo de campo (`field`), se ele for aplicável e o alvo de propriedade (`property`) não for.

Se nenhum dos alvos `param`, `property` ou `field` for aplicável, a anotação é inválida, e você precisa especificar um alvo de uso explicitamente.

Vamos usar a [anotação `@Email` do Jakarta Bean Validation](https://jakarta.ee/specifications/bean-validation/3.0/apidocs/jakarta/validation/constraints/email):

```java
@Target(value={METHOD,FIELD,ANNOTATION_TYPE,CONSTRUCTOR,PARAMETER,TYPE_USE})
public @interface Email { }
```

Com essa anotação, considere o seguinte exemplo:

```kotlin
data class User(val username: String,
                // @Email is now equivalent to @param:Email @field:Email
                @Email val email: String) {
    // @Email is still equivalent to @field:Email
    @Email val secondaryEmail: String? = null
}
```

Neste exemplo, a anotação `@Email` se aplica tanto ao alvo de parâmetro do construtor quanto ao alvo de campo da propriedade `email`, porque a propriedade:

* É declarada no construtor primário.
* Não tem getter ou setter personalizado, então o compilador gera um campo de suporte (backing field).

A anotação `@Email` se aplica apenas ao alvo de campo da propriedade `secondaryEmail`, porque a propriedade:

* Não é declarada no construtor primário.
* Não tem getter ou setter personalizado, então o compilador gera um campo de suporte (backing field).

### Meta-alvo `all` {id="all-meta-target"}

O alvo `all` facilita aplicar a mesma anotação não apenas ao parâmetro e à propriedade ou ao campo, mas também ao getter e ao setter correspondentes.

Especificamente, a anotação marcada com `all` é propagada, se aplicável:

* Para o parâmetro do construtor (`param`), se a propriedade for definida no construtor primário.
* Para a própria propriedade (`property`).
* Para o campo de suporte (`field`), se a propriedade tiver um.
* Para o getter (`get`).
* Para o parâmetro do setter (`setparam`), se a propriedade for definida como `var`.
* Para o alvo exclusivo do Java `RECORD_COMPONENT`, se a classe tiver a anotação `@JvmRecord`.

Vamos usar a [anotação `@Email` do Jakarta Bean Validation](https://jakarta.ee/specifications/bean-validation/3.0/apidocs/jakarta/validation/constraints/email),
que é definida assim:

```java
@Target(value={METHOD,FIELD,ANNOTATION_TYPE,CONSTRUCTOR,PARAMETER,TYPE_USE})
public @interface Email { }
```

No exemplo abaixo, essa anotação `@Email` é aplicada a todos os alvos relevantes:

```kotlin
data class User(
    val username: String,
    // Applies @Email to param, field, and get
    @all:Email val email: String,
    // Applies @Email to param, field, get, and setparam
    @all:Email var name: String,
) {
    // Applies @Email to field and getter (not param since it's not in the constructor)
    @all:Email val secondaryEmail: String? = null
}
```

Você pode usar o meta-alvo `all` com qualquer propriedade, tanto dentro quanto fora do construtor primário.

#### Limitações {id="limitations"}

O alvo `all` tem algumas limitações:

* Ele não propaga a anotação para tipos, possíveis receivers de extensão ou receivers e parâmetros de contexto.
* Ele não pode ser usado com várias anotações:
    ```kotlin
    @all:[A B] // forbidden, use @all:A @all:B
    val x: Int = 5
    ```
* Ele não pode ser usado com [propriedades delegadas](delegated-properties.md).

## Anotações Java {id="java-annotations"}

Anotações Java são 100% compatíveis com o Kotlin:

```kotlin
import org.junit.Test
import org.junit.Assert.*
import org.junit.Rule
import org.junit.rules.*

class Tests {
    // apply @Rule annotation to property getter
    @get:Rule val tempFolder = TemporaryFolder()

    @Test fun simple() {
        val f = tempFolder.newFile()
        assertEquals(42, getTheAnswer())
    }
}
```

Como a ordem dos parâmetros de uma anotação escrita em Java não é definida, você não pode usar a sintaxe comum de chamada
de função para passar os argumentos. Em vez disso, use a sintaxe de argumentos nomeados:

``` java
// Java
public @interface Ann {
    int intValue();
    String stringValue();
}
```

```kotlin
// Kotlin
@Ann(intValue = 1, stringValue = "abc") class C
```

Assim como em Java, um caso especial é o parâmetro `value`; o valor dele pode ser especificado sem um nome explícito:

``` java
// Java
public @interface AnnWithValue {
    String value();
}
```

```kotlin
// Kotlin
@AnnWithValue("abc") class C
```

### Arrays como parâmetros de anotação {id="arrays-as-annotation-parameters"}

Se o argumento `value` em Java tiver um tipo array, ele se torna um parâmetro `vararg` no Kotlin:

``` java
// Java
public @interface AnnWithArrayValue {
    String[] value();
}
```

```kotlin
// Kotlin
@AnnWithArrayValue("abc", "foo", "bar") class C
```

Para outros argumentos que têm tipo array, você precisa usar a sintaxe de literal de array ou
`arrayOf(...)`:

``` java
// Java
public @interface AnnWithArrayMethod {
    String[] names();
}
```

```kotlin
@AnnWithArrayMethod(names = ["abc", "foo", "bar"])
class C
```

### Acessar propriedades de uma instância de anotação {id="accessing-properties-of-an-annotation-instance"}

Os valores de uma instância de anotação são expostos como propriedades para o código Kotlin:

``` java
// Java
public @interface Ann {
    int value();
}
```

```kotlin
// Kotlin
fun foo(ann: Ann) {
    val i = ann.value
}
```

### Possibilidade de não gerar alvos de anotação do JVM 1.8+ {id="ability-to-not-generate-jvm-1-8-annotation-targets"}

Se uma anotação Kotlin tiver `TYPE` entre seus alvos Kotlin, a anotação é mapeada para `java.lang.annotation.ElementType.TYPE_USE`
em sua lista de alvos de anotação Java. Isso é igual ao que acontece com o alvo Kotlin `TYPE_PARAMETER`, que é mapeado para
o alvo Java `java.lang.annotation.ElementType.TYPE_PARAMETER`. Isso é um problema para clientes Android com níveis de API
abaixo de 26, que não têm esses alvos na API.

Para evitar a geração dos alvos de anotação `TYPE_USE` e `TYPE_PARAMETER`, use o novo argumento do compilador `-Xno-new-java-annotation-targets`.

## Anotações repetíveis {id="repeatable-annotations"}

Assim como [em Java](https://docs.oracle.com/javase/tutorial/java/annotations/repeating.html), o Kotlin tem anotações repetíveis,
que podem ser aplicadas a um único elemento de código várias vezes. Para tornar sua anotação repetível, marque a declaração dela
com a meta-anotação [`@kotlin.annotation.Repeatable`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.annotation/-repeatable/).
Isso a torna repetível tanto no Kotlin quanto no Java. Anotações repetíveis do Java também têm suporte
do lado do Kotlin.

A principal diferença em relação ao esquema usado em Java é a ausência de uma _anotação contêiner_, que o compilador do Kotlin
gera automaticamente com um nome predefinido. Para a anotação do exemplo abaixo, ele vai gerar a anotação contêiner
`@Tag.Container`:

```kotlin
@Repeatable
annotation class Tag(val name: String)

// The compiler generates the @Tag.Container containing annotation
```

Você pode definir um nome personalizado para a anotação contêiner aplicando a
meta-anotação [`@kotlin.jvm.JvmRepeatable`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-repeatable/)
e passando como argumento uma classe de anotação contêiner declarada explicitamente:

```kotlin
@JvmRepeatable(Tags::class)
annotation class Tag(val name: String)

annotation class Tags(val value: Array<Tag>)
```

Para extrair anotações repetíveis do Kotlin ou do Java via reflexão, use a função [`KAnnotatedElement.findAnnotations()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect.full/find-annotations.html).

Saiba mais sobre anotações repetíveis do Kotlin neste [KEEP](https://github.com/Kotlin/KEEP/blob/master/proposals/repeatable-annotations.md).

<!-- ia-translate: true -->
