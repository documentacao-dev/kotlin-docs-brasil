[//]: # (title: Convenções de código)

Convenções de código comumente conhecidas e fáceis de seguir são essenciais para qualquer linguagem de programação.
Aqui oferecemos diretrizes sobre o estilo de código e a organização de código para projetos que usam Kotlin.

## Configurar o estilo na IDE {id="configure-style-in-ide"}

As duas IDEs mais populares para Kotlin, [IntelliJ IDEA](https://www.jetbrains.com/idea/) e [Android Studio](https://developer.android.com/studio/),
oferecem recursos poderosos para formatação de código. Você pode configurá-las para formatar seu código automaticamente de acordo com o
estilo de código definido.
 
### Aplicar o guia de estilo {id="apply-the-style-guide"}

1. Acesse **Settings/Preferences | Editor | Code Style | Kotlin**.
2. Clique em **Set from...**.
3. Selecione **Kotlin style guide** .

### Verificar se o código segue o guia de estilo {id="verify-that-your-code-follows-the-style-guide"}

1. Acesse **Settings/Preferences | Editor | Inspections | General**.
2. Ative a inspeção **Incorrect formatting**.
Inspeções adicionais que verificam outros problemas descritos no guia de estilo (como convenções de nomenclatura) já vêm ativadas por padrão.

<!-- Replace with an external link when the guide is moved -->

Para mais informações, veja o guia [Migre para o estilo de código do Kotlin com o IntelliJ IDEA](code-style-migration-guide.md).

## Organização do código-fonte {id="source-code-organization"}

### Estrutura de diretórios {id="directory-structure"}

Em projetos Kotlin puros, a estrutura de diretórios recomendada segue a estrutura de pacotes, com o pacote raiz comum omitido. Por exemplo, se todo o código do projeto está no pacote `org.example.kotlin` e em seus subpacotes, os arquivos do pacote `org.example.kotlin` devem ser colocados diretamente sob a raiz de código-fonte, e os arquivos em `org.example.kotlin.network.socket` devem estar no subdiretório `network/socket` da raiz de código-fonte.

>No JVM: em projetos em que Kotlin é usado junto com Java, os arquivos-fonte Kotlin devem ficar na mesma 
>raiz de código-fonte dos arquivos Java e seguir a mesma estrutura de diretórios: cada arquivo deve ser armazenado no 
>diretório correspondente a cada declaração `package`.
>
{style="note"}

### Nomes de arquivos-fonte {id="source-file-names"}

Se um arquivo Kotlin contém uma única classe ou interface (possivelmente com declarações de nível superior relacionadas), seu nome deve ser igual ao nome da classe, com a extensão `.kt` acrescentada.
Isso se aplica a todos os tipos de classes e interfaces.
Se um arquivo contém várias classes, ou apenas declarações de nível superior, escolha um nome que descreva o que o arquivo contém e nomeie o arquivo de acordo.
Use [upper camel case](https://en.wikipedia.org/wiki/Camel_case), em que a primeira letra de cada palavra é maiúscula.
Por exemplo, `ProcessDeclarations.kt`.

O nome do arquivo deve descrever o que o código nele faz. Por isso, evite usar palavras sem significado, como `Util`, nos nomes de arquivos.

#### Projetos multiplataforma {id="multiplatform-projects"}

Em projetos multiplataforma, arquivos com declarações de nível superior em source sets específicas de plataforma devem ter um sufixo associado ao nome do source set. Por exemplo:

* **jvm**Main/kotlin/Platform.**jvm**.kt
* **android**Main/kotlin/Platform.**android**.kt
* **ios**Main/kotlin/Platform.**ios**.kt

Quanto ao source set comum, arquivos com declarações de nível superior não devem ter sufixo. Por exemplo, `commonMain/kotlin/Platform.kt`.

##### Detalhes técnicos {id="technical-details" initial-collapse-state="collapsed" collapsible="true"}

Recomendamos seguir este esquema de nomenclatura de arquivos em projetos multiplataforma por causa de limitações da JVM: ela não permite membros de nível superior (funções, propriedades).

Para contornar isso, o compilador Kotlin para JVM cria classes wrapper (chamadas de "file facades") que contêm as declarações de membros de nível superior. File facades têm um nome interno derivado do nome do arquivo.

Por sua vez, a JVM não permite várias classes com o mesmo nome totalmente qualificado (FQN). Isso pode fazer com que um projeto Kotlin não consiga ser compilado para JVM:

```none
root
|- commonMain/kotlin/myPackage/Platform.kt // contains 'fun count() { }'
|- jvmMain/kotlin/myPackage/Platform.kt // contains 'fun multiply() { }'
```

Aqui, ambos os arquivos `Platform.kt` estão no mesmo pacote, então o compilador Kotlin para JVM produz dois file facades, ambos com o FQN `myPackage.PlatformKt`. Isso gera o erro "Duplicate JVM classes".

A forma mais simples de evitar isso é renomear um dos arquivos de acordo com a diretriz acima. Esse esquema de nomenclatura ajuda a evitar conflitos sem perder a legibilidade do código.

> Há dois cenários em que essas recomendações podem parecer redundantes, mas ainda assim aconselhamos segui-las:
> 
> * Plataformas que não são JVM não têm problemas com file facades duplicados. No entanto, esse esquema de nomenclatura pode ajudar a manter os nomes de arquivos consistentes.
> * Na JVM, se os arquivos-fonte não têm declarações de nível superior, os file facades não são gerados, e você não enfrentará conflitos de nomes.
> 
>   No entanto, esse esquema de nomenclatura pode ajudar a evitar situações em que uma simples refatoração ou uma adição inclua uma função de nível superior e resulte no mesmo erro "Duplicate JVM classes".
> 
{style="tip"}

### Organização dos arquivos-fonte {id="source-file-organization"}

Colocar várias declarações (classes, funções ou propriedades de nível superior) no mesmo arquivo-fonte Kotlin é encorajado, desde que essas declarações estejam semanticamente bem relacionadas entre si e o tamanho do arquivo continue razoável (não ultrapassando algumas centenas de linhas).

Em particular, ao definir funções de extensão para uma classe que são relevantes para todos os clientes dessa classe, coloque-as no mesmo arquivo da própria classe. Ao definir funções de extensão que fazem sentido apenas para um cliente específico, coloque-as junto ao código desse cliente. Evite criar arquivos apenas para conter todas as extensões de alguma classe.

### Layout da classe {id="class-layout"}

O conteúdo de uma classe deve seguir esta ordem:

1. Declarações de propriedades e blocos de inicialização
2. Construtores secundários
3. Declarações de métodos
4. Companion object

Não ordene as declarações de métodos em ordem alfabética ou por visibilidade, e não separe métodos regulares de métodos de extensão. Em vez disso, mantenha itens relacionados juntos, para que quem lê a classe de cima para baixo consiga acompanhar a lógica do que está acontecendo. Escolha uma ordem (primeiro os itens de nível mais alto, ou o contrário) e mantenha-a.

Coloque classes aninhadas junto ao código que as usa. Se as classes forem destinadas a uso externo e não forem referenciadas dentro da classe, coloque-as no final, depois do companion object.

### Layout da implementação de interface {id="interface-implementation-layout"}

Ao implementar uma interface, mantenha os membros implementados na mesma ordem dos membros da interface (se necessário, intercalados com métodos privados adicionais usados na implementação).

### Layout de sobrecargas {id="overload-layout"}

Sempre coloque as sobrecargas umas ao lado das outras em uma classe.

## Regras de nomenclatura {id="naming-rules"}

As regras de nomenclatura de pacotes e classes em Kotlin são bastante simples:

* Nomes de pacotes são sempre em letras minúsculas e não usam sublinhados (`org.example.project`). Usar nomes com várias palavras geralmente não é recomendado, mas, se você precisar usar várias palavras, pode concatená-las ou usar camel case (`org.example.myProject`).

* Nomes de classes e objetos usam upper camel case:

```kotlin
open class DeclarationProcessor { /*...*/ }

object EmptyDeclarationProcessor : DeclarationProcessor() { /*...*/ }
```

### Nomes de funções {id="function-names"}

Nomes de funções, propriedades e variáveis locais começam com letra minúscula e usam camel case sem sublinhados:

```kotlin
fun processDeclarations() { /*...*/ }
var declarationCount = 1
```

### Nomes para funções semelhantes a classes {id="names-for-class-like-functions"}

Há duas exceções em que nomes de funções devem seguir a convenção de nomenclatura de classes. Funções desse tipo geralmente são definidas no nível superior.

* Funções de fábrica que criam instâncias de classes podem ter o mesmo nome do tipo de retorno abstrato:

   ```kotlin
   interface Foo { /*...*/ }

   class FooImpl : Foo { /*...*/ }

   fun Foo(): Foo { return FooImpl() }
   ```

* Funções `@Composable` que retornam `Unit`:

   ```kotlin
   @Composable fun TabHeader { /*...*/ }
   ```

### Nomes para métodos de teste {id="names-for-test-methods"}

Em testes (e **somente** em testes), você pode usar nomes de métodos com espaços entre crases. Observe que esses nomes só funcionam no runtime do Android a partir do API level 30. Sublinhados nos nomes de métodos também são permitidos em código de teste.

```kotlin
class MyTestCase {
    @Test fun `ensure everything works`() { /*...*/ }

    @Test fun ensureEverythingWorks_onAndroid() { /*...*/ }
}
```

### Nomes de propriedades {id="property-names"}

Nomes de constantes (propriedades marcadas com `const`, ou propriedades `val` de nível superior ou de objeto sem função `get` customizada que contenham dados profundamente imutáveis) devem usar apenas letras maiúsculas, com palavras separadas por sublinhado, seguindo a convenção de [screaming snake case](https://en.wikipedia.org/wiki/Snake_case):

```kotlin
const val MAX_COUNT = 8
val USER_NAME_FIELD = "UserName"
```

Nomes de propriedades de nível superior ou de objeto que contenham objetos com comportamento ou dados mutáveis devem usar camel case:

```kotlin
val mutableCollection: MutableSet<String> = HashSet()
```

Nomes de propriedades que referenciam objetos singleton podem usar o mesmo estilo de nomenclatura das declarações `object`:

```kotlin
val PersonComparator: Comparator<Person> = /*...*/
```

Para constantes de enum, é aceitável usar tanto nomes em letras maiúsculas, separados por sublinhado ([screaming snake case](https://en.wikipedia.org/wiki/Snake_case)) (`enum class Color { RED, GREEN }`), quanto nomes em upper camel case, dependendo do uso. 
   
### Nomes para propriedades de apoio {id="names-for-backing-properties"}

Se uma classe tem duas propriedades que são conceitualmente iguais, mas uma faz parte de uma API pública e a outra é um detalhe de implementação, use um sublinhado como prefixo no nome da propriedade privada:

```kotlin
class C {
    private val _elementList = mutableListOf<Element>()

    val elementList: List<Element>
        get() = _elementList
}
```

### Escolha bons nomes {id="choose-good-names"}

O nome de uma classe geralmente é um substantivo ou uma locução substantiva que explica o que a classe _é_: `List`, `PersonReader`.

O nome de um método geralmente é um verbo ou uma locução verbal que diz o que o método _faz_: `close`, `readPersons`.
O nome também deve sugerir se o método modifica o objeto ou retorna um novo. Por exemplo, `sort` ordena uma coleção no próprio lugar, enquanto `sorted` retorna uma cópia ordenada da coleção.

Os nomes devem deixar claro qual é o propósito da entidade, por isso é melhor evitar palavras sem significado (`Manager`, `Wrapper`) nos nomes.

Ao usar uma sigla como parte do nome de uma declaração, siga estas regras:

* Para siglas de duas letras, use maiúsculas nas duas letras. Por exemplo, `IOStream`.
* Para siglas com mais de duas letras, deixe maiúscula apenas a primeira letra. Por exemplo, `XmlFormatter` ou `HttpInputStream`.

## Formatação {id="formatting"}

### Indentação {id="indentation"}

Use quatro espaços para indentação. Não use tabulações.

Para as chaves, coloque a chave de abertura no final da linha em que a construção começa, e a chave de fechamento em uma linha separada, alinhada horizontalmente com a construção de abertura.

```kotlin
if (elements != null) {
    for (element in elements) {
        // ...
    }
}
```

>Em Kotlin, o ponto e vírgula é opcional, e por isso as quebras de linha são significativas. O design da linguagem assume chaves no estilo Java, e você pode encontrar comportamentos inesperados se tentar usar um estilo de formatação diferente.
>
{style="note"}

### Espaços horizontais {id="horizontal-whitespace"}

* Coloque espaços em torno de operadores binários (`a + b`). Exceção: não use espaços em torno do operador "range to" (`0..i`).
* Não use espaços em torno de operadores unários (`a++`).
* Coloque espaços entre as palavras-chave de controle de fluxo (`if`, `when`, `for` e `while`) e o parêntese de abertura correspondente.
* Não coloque espaço antes do parêntese de abertura em uma declaração de construtor primário, em uma declaração de método ou em uma chamada de método.

```kotlin
class A(val x: Int)

fun foo(x: Int) { ... }

fun bar() {
    foo(1)
}
```

* Nunca coloque espaço depois de `(`, `[`, nem antes de `]`, `)`.
* Nunca coloque espaços em torno de `.` ou `?.`: `foo.bar().filter { it > 2 }.joinToString()`, `foo?.bar()`.
* Coloque um espaço depois de `//`: `// This is a comment`.
* Não coloque espaços em torno dos colchetes angulares usados para especificar parâmetros de tipo: `class Map<K, V> { ... }`.
* Não coloque espaços em torno de `::`: `Foo::class`, `String::length`.
* Não coloque espaço antes de `?` usado para marcar um tipo que aceita `null`: `String?`.

Como regra geral, evite alinhamento horizontal de qualquer tipo. Renomear um identificador para um nome com tamanho diferente não deve afetar a formatação da declaração nem a de nenhum dos seus usos.

### Dois-pontos {id="colon"}

Coloque um espaço antes de `:` nos seguintes cenários:

* Quando ele é usado para separar um tipo de um supertipo.
* Ao delegar para o construtor da superclasse ou para outro construtor da mesma classe.
* Depois da palavra-chave `object`.
    
Não coloque espaço antes de `:` quando ele separa uma declaração do seu tipo.
 
Sempre coloque um espaço depois de `:`.

```kotlin
abstract class Foo<out T : Any> : IFoo {
    abstract fun foo(a: Int): T
}

class FooImpl : Foo() {
    constructor(x: String) : this(x) { /*...*/ }

    val x = object : IFoo { /*...*/ } 
}
```

### Cabeçalhos de classe {id="class-headers"}

Classes com poucos parâmetros no construtor primário podem ser escritas em uma única linha:

```kotlin
class Person(id: Int, name: String)
```

Classes com cabeçalhos mais longos devem ser formatadas de modo que cada parâmetro do construtor primário fique em uma linha separada, com indentação.
Além disso, o parêntese de fechamento deve ficar em uma nova linha. Se você usar herança, a chamada do construtor da superclasse ou a lista de interfaces implementadas deve ficar na mesma linha do parêntese:

```kotlin
class Person(
    id: Int,
    name: String,
    surname: String
) : Human(id, name) { /*...*/ }
```

Para múltiplas interfaces, a chamada do construtor da superclasse deve vir primeiro, e cada interface deve ficar em uma linha diferente:

```kotlin
class Person(
    id: Int,
    name: String,
    surname: String
) : Human(id, name),
    KotlinMaker { /*...*/ }
```

Para classes com uma lista longa de supertipos, coloque uma quebra de linha depois dos dois-pontos e alinhe horizontalmente todos os nomes dos supertipos:

```kotlin
class MyFavouriteVeryLongClassHolder :
    MyLongHolder<MyFavouriteVeryLongClass>(),
    SomeOtherInterface,
    AndAnotherOne {

    fun foo() { /*...*/ }
}
```

Para separar claramente o cabeçalho e o corpo da classe quando o cabeçalho é longo, coloque uma linha em branco depois do cabeçalho da classe (como no exemplo acima) ou coloque a chave de abertura em uma linha separada:

```kotlin
class MyFavouriteVeryLongClassHolder :
    MyLongHolder<MyFavouriteVeryLongClass>(),
    SomeOtherInterface,
    AndAnotherOne 
{
    fun foo() { /*...*/ }
}
```

Use a indentação regular (quatro espaços) para os parâmetros do construtor. Isso garante que as propriedades declaradas no construtor primário tenham a mesma indentação das propriedades declaradas no corpo da classe.

### Ordem dos modificadores {id="modifiers-order"}

Se uma declaração tem vários modificadores, sempre os coloque na seguinte ordem:

```kotlin
public / protected / private / internal
expect / actual
final / open / abstract / sealed / const
external
override
lateinit
tailrec
vararg
suspend
inner
enum / annotation / fun // as a modifier in `fun interface` 
companion
inline / value
infix
operator
data
```

Coloque todas as anotações antes dos modificadores:

```kotlin
@Named("Foo")
private val foo: Foo
```

A menos que você esteja trabalhando em uma biblioteca, omita modificadores redundantes (por exemplo, `public`).

### Anotações {id="annotations"}

Coloque as anotações em linhas separadas, antes da declaração à qual estão associadas, e com a mesma indentação:

```kotlin
@Target(AnnotationTarget.PROPERTY)
annotation class JsonExclude
```

Anotações sem argumentos podem ser colocadas na mesma linha:

```kotlin
@JsonExclude @JvmField
var x: String
```

Uma única anotação sem argumentos pode ser colocada na mesma linha da declaração correspondente:

```kotlin
@Test fun foo() { /*...*/ }
```

### Anotações de arquivo {id="file-annotations"}

Anotações de arquivo são colocadas depois do comentário do arquivo (se houver), antes da instrução `package`, e são separadas de `package` por uma linha em branco (para enfatizar que elas se referem ao arquivo, e não ao pacote).

```kotlin
/** License, copyright and whatever */
@file:JvmName("FooBar")

package foo.bar
```

### Funções {id="functions"}

Se a assinatura da função não couber em uma única linha, use a seguinte sintaxe:

```kotlin
fun longMethodName(
    argument: ArgumentType = defaultValue,
    argument2: AnotherArgumentType,
): ReturnType {
    // body
}
```

Use a indentação regular (quatro espaços) para os parâmetros da função. Isso ajuda a manter a consistência com os parâmetros do construtor.

Prefira usar um corpo de expressão em funções cujo corpo consiste em uma única expressão.

```kotlin
fun foo(): Int {     // bad
    return 1 
}

fun foo() = 1        // good
```

### Corpos de expressão {id="expression-bodies"}

Se a função tem um corpo de expressão cuja primeira linha não cabe na mesma linha da declaração, coloque o sinal `=` na primeira linha e indente o corpo da expressão em quatro espaços.

```kotlin
fun f(x: String, y: String, z: String) =
    veryLongFunctionCallWithManyWords(andLongParametersToo(), x, y, z)
```

### Propriedades {id="properties"}

Para propriedades somente leitura bem simples, considere a formatação em uma linha:

```kotlin
val isEmpty: Boolean get() = size == 0
```

Para propriedades mais complexas, sempre coloque as palavras-chave `get` e `set` em linhas separadas:

```kotlin
val foo: String
    get() { /*...*/ }
```

Para propriedades com inicializador, se o inicializador for longo, adicione uma quebra de linha depois do sinal `=` e indente o inicializador em quatro espaços:

```kotlin
private val defaultCharset: Charset? =
    EncodingRegistry.getInstance().getDefaultCharsetForPropertiesFiles(file)
```

### Instruções de controle de fluxo {id="control-flow-statements"}

Se a condição de uma instrução `if` ou `when` ocupa várias linhas, use sempre chaves ao redor do corpo da instrução.
Indente cada linha subsequente da condição em quatro espaços em relação ao início da instrução.
Coloque o parêntese de fechamento da condição junto com a chave de abertura, em uma linha separada:

```kotlin
if (!component.isSyncing &&
    !hasAnyKotlinRuntimeInScope(module)
) {
    return createKotlinNotConfiguredPanel(module)
}
```

Isso ajuda a alinhar a condição e os corpos das instruções. 

Coloque as palavras-chave `else`, `catch` e `finally`, assim como a palavra-chave `while` de um laço `do-while`, na mesma linha da chave anterior:

```kotlin
if (condition) {
    // body
} else {
    // else part
}

try {
    // body
} finally {
    // cleanup
}
```

Em uma instrução `when`, se um ramo ocupa mais de uma linha, considere separá-lo dos blocos de caso adjacentes com uma linha em branco:

```kotlin
private fun parsePropertyValue(propName: String, token: Token) {
    when (token) {
        is Token.ValueToken ->
            callback.visitValue(propName, token.value)

        Token.LBRACE -> { // ...
        }
    }
}
```

Coloque ramos curtos na mesma linha da condição, sem chaves.

```kotlin
when (foo) {
    true -> bar() // good
    false -> { baz() } // bad
}
```

### Chamadas de método {id="method-calls"}

Em listas longas de argumentos, coloque uma quebra de linha depois do parêntese de abertura. Indente os argumentos em quatro espaços.
Agrupe múltiplos argumentos intimamente relacionados na mesma linha.

```kotlin
drawSquare(
    x = 10, y = 10,
    width = 100, height = 100,
    fill = true
)
```

Coloque espaços em torno do sinal `=` que separa o nome do argumento e o valor.

### Quebrar chamadas encadeadas {id="wrap-chained-calls"}

Ao quebrar chamadas encadeadas, coloque o caractere `.` ou o operador `?.` na linha seguinte, com uma única indentação:

```kotlin
val anchor = owner
    ?.firstChild!!
    .siblings(forward = true)
    .dropWhile { it is PsiComment || it is PsiWhiteSpace }
```

A primeira chamada da cadeia geralmente deve ter uma quebra de linha antes dela, mas é aceitável omiti-la se o código fizer mais sentido assim.

### Lambdas

Em expressões lambda, use espaços ao redor das chaves, assim como ao redor da seta que separa os parâmetros do corpo. Se uma chamada recebe um único lambda, passe-o fora dos parênteses sempre que possível.

```kotlin
list.filter { it > 10 }
```

Ao atribuir um rótulo a um lambda, não coloque espaço entre o rótulo e a chave de abertura:

```kotlin
fun foo() {
    ints.forEach lit@{
        // ...
    }
}
```

Ao declarar nomes de parâmetros em um lambda de várias linhas, coloque os nomes na primeira linha, seguidos da seta e da quebra de linha:

```kotlin
appendCommaSeparated(properties) { prop ->
    val propertyValue = prop.get(obj)  // ...
}
```

Se a lista de parâmetros for longa demais para caber em uma linha, coloque a seta em uma linha separada:

```kotlin
foo {
    context: Context,
    environment: Env
    ->
    context.configureEnv(environment)
}
```

### Vírgulas finais {id="trailing-commas"}

Uma vírgula final é o símbolo de vírgula depois do último item em uma série de elementos:

```kotlin
class Person(
    val firstName: String,
    val lastName: String,
    val age: Int, // trailing comma
)
```

Usar vírgulas finais tem vários benefícios:

* Deixa os diffs do controle de versão mais limpos, já que todo o foco fica no valor alterado.
* Facilita adicionar e reordenar elementos: não é preciso adicionar ou remover a vírgula ao manipular os elementos.
* Simplifica a geração de código, por exemplo, para inicializadores de objetos. O último elemento também pode ter uma vírgula.

Vírgulas finais são totalmente opcionais: seu código continua funcionando sem elas. O guia de estilo do Kotlin incentiva o uso de vírgulas finais na declaração e deixa a critério de você usá-las na chamada.

Para ativar vírgulas finais no formatador do IntelliJ IDEA, acesse **Settings/Preferences | Editor | Code Style | Kotlin**, abra a aba **Other** e selecione a opção **Use trailing comma**.

#### Enumerações {id="enumerations" initial-collapse-state="collapsed" collapsible="true"}

```kotlin
enum class Direction {
    NORTH,
    SOUTH,
    WEST,
    EAST, // trailing comma
}
```

#### Argumentos de valor {id="value-arguments" initial-collapse-state="collapsed" collapsible="true"}

```kotlin
fun shift(x: Int, y: Int) { /*...*/ }
shift(
    25,
    20, // trailing comma
)
val colors = listOf(
    "red",
    "green",
    "blue", // trailing comma
)
```

#### Propriedades e parâmetros de classe {id="class-properties-and-parameters" initial-collapse-state="collapsed" collapsible="true"}

```kotlin
class Customer(
    val name: String,
    val lastName: String, // trailing comma
)
class Customer(
    val name: String,
    lastName: String, // trailing comma
)
```

#### Parâmetros de valor de função {id="function-value-parameters" initial-collapse-state="collapsed" collapsible="true"}

```kotlin
fun powerOf(
    number: Int, 
    exponent: Int, // trailing comma
) { /*...*/ }
constructor(
    x: Comparable<Number>,
    y: Iterable<Number>, // trailing comma
) {}
fun print(
    vararg quantity: Int,
    description: String, // trailing comma
) {}
```

#### Parâmetros com tipo opcional (incluindo setters) {id="parameters-with-optional-type-including-setters" initial-collapse-state="collapsed" collapsible="true"}

```kotlin
val sum: (Int, Int, Int) -> Int = fun(
    x,
    y,
    z, // trailing comma
): Int {
    return x + y + x
}
println(sum(8, 8, 8))
```

#### Sufixo de indexação {id="indexing-suffix" initial-collapse-state="collapsed" collapsible="true"}

```kotlin
class Surface {
    operator fun get(x: Int, y: Int) = 2 * x + 4 * y - 10
}
fun getZValue(mySurface: Surface, xValue: Int, yValue: Int) =
    mySurface[
        xValue,
        yValue, // trailing comma
    ]
```

#### Parâmetros em lambdas {id="parameters-in-lambdas" initial-collapse-state="collapsed" collapsible="true"}

```kotlin
fun main() {
    val x = {
            x: Comparable<Number>,
            y: Iterable<Number>, // trailing comma
        ->
        println("1")
    }
    println(x)
}
```

#### Entradas do when {id="when-entry" initial-collapse-state="collapsed" collapsible="true"}

```kotlin
fun isReferenceApplicable(myReference: KClass<*>) = when (myReference) {
    Comparable::class,
    Iterable::class,
    String::class, // trailing comma
        -> true
    else -> false
}
```

#### Literais de coleção (em anotações) {id="collection-literals-in-annotations" initial-collapse-state="collapsed" collapsible="true"}

```kotlin
annotation class ApplicableFor(val services: Array<String>)
@ApplicableFor([
    "serializer",
    "balancer",
    "database",
    "inMemoryCache", // trailing comma
])
fun run() {}
```

#### Argumentos de tipo {id="type-arguments" initial-collapse-state="collapsed" collapsible="true"}

```kotlin
fun <T1, T2> foo() {}
fun main() {
    foo<
            Comparable<Number>,
            Iterable<Number>, // trailing comma
            >()
}
```

#### Parâmetros de tipo {id="type-parameters" initial-collapse-state="collapsed" collapsible="true"}

```kotlin
class MyMap<
        MyKey,
        MyValue, // trailing comma
        > {}
```

#### Declarações de desestruturação {id="destructuring-declarations" initial-collapse-state="collapsed" collapsible="true"}

```kotlin
data class Car(val manufacturer: String, val model: String, val year: Int)
val myCar = Car("Tesla", "Y", 2019)
val (
    manufacturer,
    model,
    year, // trailing comma
) = myCar
val cars = listOf<Car>()
fun printMeanValue() {
    var meanValue: Int = 0
    for ((
        _,
        _,
        year, // trailing comma
    ) in cars) {
        meanValue += year
    }
    println(meanValue/cars.size)
}
printMeanValue()
```

## Comentários de documentação {id="documentation-comments"}

Para comentários de documentação mais longos, coloque o `/**` de abertura em uma linha separada e comece cada linha seguinte com um asterisco:

```kotlin
/**
 * This is a documentation comment
 * on multiple lines.
 */
```

Comentários curtos podem ser colocados em uma única linha:

```kotlin
/** This is a short documentation comment. */
```

De modo geral, evite usar as tags `@param` e `@return`. Em vez disso, incorpore a descrição dos parâmetros e dos valores de retorno diretamente no comentário de documentação, e adicione links para os parâmetros sempre que forem mencionados. Use `@param` e `@return` apenas quando for necessária uma descrição extensa que não caiba no fluxo do texto principal.

```kotlin
// Avoid doing this:

/**
 * Returns the absolute value of the given number.
 * @param number The number to return the absolute value for.
 * @return The absolute value.
 */
fun abs(number: Int): Int { /*...*/ }

// Do this instead:

/**
 * Returns the absolute value of the given [number].
 */
fun abs(number: Int): Int { /*...*/ }
```

## Evite construções redundantes {id="avoid-redundant-constructs"}

De modo geral, se uma certa construção sintática do Kotlin é opcional e destacada pela IDE como redundante, você deve omiti-la no seu código. Não deixe elementos sintáticos desnecessários no código apenas "para deixar mais claro".

### Tipo de retorno Unit {id="unit-return-type"}

Se uma função retorna Unit, o tipo de retorno deve ser omitido:

```kotlin
fun foo() { // ": Unit" is omitted here

}
```

### Ponto e vírgula {id="semicolons"}

Omita pontos e vírgulas sempre que possível.

### Templates de string {id="string-templates"}

Não use chaves ao inserir uma variável simples em um template de string. Use chaves apenas para expressões mais longas:

```kotlin
println("$name has ${children.size} children")
```

Use a [interpolação de strings com múltiplos cifrões](strings.md#multi-dollar-string-interpolation) para tratar o caractere de cifrão `$` como literal de string:

```kotlin
val KClass<*>.jsonSchema : String
    get() = $$"""
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "https://example.com/product.schema.json",
            "$dynamicAnchor": "meta",
            "title": "$${simpleName ?: qualifiedName ?: "unknown"}",
            "type": "object"
        }
        """
```

## Uso idiomático dos recursos da linguagem {id="idiomatic-use-of-language-features"}

### Imutabilidade {id="immutability"}

Prefira dados imutáveis a dados mutáveis. Sempre declare variáveis locais e propriedades como `val`, em vez de `var`, se elas não forem modificadas após a inicialização.

Sempre use as interfaces de coleção imutáveis (`Collection`, `List`, `Set`, `Map`) para declarar coleções que não são modificadas. Ao usar funções de fábrica para criar instâncias de coleções, sempre que possível use funções que retornam tipos de coleção imutáveis:

```kotlin
// Bad: use of a mutable collection type for value which will not be mutated
fun validateValue(actualValue: String, allowedValues: HashSet<String>) { ... }

// Good: immutable collection type used instead
fun validateValue(actualValue: String, allowedValues: Set<String>) { ... }

// Bad: arrayListOf() returns ArrayList<T>, which is a mutable collection type
val allowedValues = arrayListOf("a", "b", "c")

// Good: listOf() returns List<T>
val allowedValues = listOf("a", "b", "c")
```

### Valores padrão de parâmetros {id="default-parameter-values"}

Prefira declarar funções com valores padrão de parâmetros a declarar funções sobrecarregadas.

```kotlin
// Bad
fun foo() = foo("a")
fun foo(a: String) { /*...*/ }

// Good
fun foo(a: String = "a") { /*...*/ }
```

### Aliases de tipo {id="type-aliases"}

Se você tem um tipo função ou um tipo com parâmetros de tipo que é usado várias vezes em uma base de código, prefira definir um alias de tipo para ele:

```kotlin
typealias MouseClickHandler = (Any, MouseEvent) -> Unit
typealias PersonIndex = Map<String, Person>
```
Se você usar um alias de tipo privado ou interno para evitar colisão de nomes, prefira o `import ... as ...` mencionado em 
[Pacotes e imports](packages.md).

### Parâmetros de lambda {id="lambda-parameters"}

Em lambdas curtas e não aninhadas, recomenda-se usar a convenção `it` em vez de declarar o parâmetro explicitamente. Em lambdas aninhadas com parâmetros, sempre declare os parâmetros explicitamente.

### Retornos em lambdas {id="returns-in-a-lambda"}

Evite usar múltiplos retornos rotulados em uma lambda. Considere reestruturar a lambda para que ela tenha um único ponto de saída.
Se isso não for possível ou não ficar claro o suficiente, considere converter a lambda em uma função anônima.

Não use um retorno rotulado para a última instrução de uma lambda.

### Argumentos nomeados {id="named-arguments"}

Use a sintaxe de argumento nomeado quando um método recebe vários parâmetros do mesmo tipo primitivo, ou para parâmetros do tipo `Boolean`,
a menos que o significado de todos os parâmetros seja absolutamente claro pelo contexto.

```kotlin
drawSquare(x = 10, y = 10, width = 100, height = 100, fill = true)
```

### Instruções condicionais {id="conditional-statements"}

Prefira usar a forma de expressão de `try`, `if` e `when`.

```kotlin
return if (x) foo() else bar()
```

```kotlin
return when(x) {
    0 -> "zero"
    else -> "nonzero"
}
```

O exemplo acima é preferível a:

```kotlin
if (x)
    return foo()
else
    return bar()
```

```kotlin
when(x) {
    0 -> return "zero"
    else -> return "nonzero"
}
```

### if versus when

Prefira usar `if` para condições binárias em vez de `when`.
Por exemplo, use esta sintaxe com `if`:

```kotlin
if (x == null) ... else ...
```

Em vez desta, com `when`:

```kotlin
when (x) {
    null -> // ...
    else -> // ...
}
```

Prefira usar `when` se houver três ou mais opções.

### Condições de guarda em expressões when {id="guard-conditions-in-when-expression"}

Use parênteses ao combinar múltiplas expressões booleanas em expressões ou instruções `when` com [condições de guarda](control-flow.md#guard-conditions-in-when-expressions):

```kotlin
when (status) {
    is Status.Ok if (status.info.isEmpty() || status.info.id == null) -> "no information"
}
```

Em vez de:

```kotlin
when (status) {
    is Status.Ok if status.info.isEmpty() || status.info.id == null -> "no information"
}
```

### Valores Boolean anuláveis em condições {id="nullable-boolean-values-in-conditions"}

Se você precisar usar um `Boolean` anulável em uma instrução condicional, use verificações `if (value == true)` ou `if (value == false)`.

### Laços de repetição {id="loops"}

Prefira usar funções de ordem superior (`filter`, `map` etc.) a laços. Exceção: `forEach` (prefira um `for` regular, a menos que o receiver de `forEach` seja anulável ou que `forEach` seja usado como parte de uma cadeia de chamadas mais longa).

Ao escolher entre uma expressão complexa que usa várias funções de ordem superior e um laço, entenda o custo das operações executadas em cada caso e tenha em mente as considerações de desempenho.

### Laços em intervalos {id="loops-on-ranges"}

Use o operador `..<` para percorrer um intervalo com limite superior exclusivo:

```kotlin
for (i in 0..n - 1) { /*...*/ }  // bad
for (i in 0..<n) { /*...*/ }  // good
```

### Strings

Prefira templates de string à concatenação de strings.

Prefira strings de múltiplas linhas a incluir sequências de escape `\n` em literais de string comuns.

Para manter a indentação em strings de múltiplas linhas, use `trimIndent` quando a string resultante não exigir nenhuma indentação interna, ou `trimMargin` quando a indentação interna for necessária:

```kotlin
fun main() {
//sampleStart
    println("""
     Not
     trimmed
     text
     """
    )

    println("""
     Trimmed
     text
     """.trimIndent()
    )

    println()

    val a = """Trimmed to margin text:
            |if(a > 1) {
            |    return a
            |}""".trimMargin()

   println(a)
//sampleEnd
}
```
{kotlin-runnable="true"}

Saiba a diferença entre [strings de múltiplas linhas em Java e Kotlin](java-to-kotlin-idioms-strings.md#use-multiline-strings).

### Funções versus propriedades {id="functions-vs-properties"}

Em alguns cenários, funções sem argumentos podem ser intercambiáveis com propriedades somente leitura. Embora a semântica seja parecida, há convenções de estilo sobre quando preferir uma à outra.

Prefira uma propriedade a uma função quando o algoritmo subjacente:

* Não lança exceções.
* É barato de calcular (ou é armazenado em cache na primeira execução).
* Retorna o mesmo resultado nas invocações, se o estado do objeto não tiver mudado.

### Funções de extensão {id="extension-functions"}

Use funções de extensão com liberdade. Sempre que tiver uma função que trabalha principalmente sobre um objeto, considere torná-la uma função de extensão que recebe esse objeto como receiver. Para minimizar a poluição da API, restrinja a visibilidade das funções de extensão na medida em que faça sentido. Quando necessário, use funções de extensão locais, funções de extensão de membro ou funções de extensão de nível superior com visibilidade `private`.

### Funções infix {id="infix-functions"}

Declare uma função como `infix` apenas quando ela trabalhar com dois objetos que desempenham um papel semelhante. Bons exemplos: `and`, `to`, `zip`.
Mau exemplo: `add`.

Não declare um método como `infix` se ele modifica o objeto receiver.

### Funções de fábrica {id="factory-functions"}

Se você declarar uma função de fábrica para uma classe, evite dar a ela o mesmo nome da própria classe. Prefira um nome distinto, deixando claro por que o comportamento da função de fábrica é especial. Somente se realmente não houver nenhuma semântica especial você pode usar o mesmo nome da classe.

```kotlin
class Point(val x: Double, val y: Double) {
    companion object {
        fun fromPolar(angle: Double, radius: Double) = Point(...)
    }
}
```

Se você tem um objeto com vários construtores sobrecarregados que não chamam construtores de superclasses diferentes e não podem ser reduzidos a um único construtor com parâmetros que tenham valores padrão, prefira substituir os construtores sobrecarregados por funções de fábrica.

### Tipos de plataforma {id="platform-types"}

Uma função ou método público que retorna uma expressão de tipo de plataforma deve declarar explicitamente o seu tipo Kotlin:

```kotlin
fun apiCall(): String = MyJavaApi.getProperty("name")
```

Qualquer propriedade (em nível de pacote ou de classe) inicializada com uma expressão de tipo de plataforma deve declarar explicitamente o seu tipo Kotlin:

```kotlin
class Person {
    val name: String = MyJavaApi.getProperty("name")
}
```

Um valor local inicializado com uma expressão de tipo de plataforma pode ou não ter declaração de tipo:

```kotlin
fun main() {
    val name = MyJavaApi.getProperty("name")
    println(name)
}
```

### Scope functions apply/with/run/also/let

O Kotlin oferece um conjunto de funções para executar um bloco de código no contexto de um determinado objeto: `let`, `run`, `with`, `apply` e `also`.
Para orientação sobre como escolher a função de escopo certa para o seu caso, consulte [Funções de escopo](scope-functions.md).

## Convenções de código para bibliotecas {id="coding-conventions-for-libraries"}

Ao escrever bibliotecas, é recomendado seguir um conjunto adicional de regras para garantir a estabilidade da API:

 * Sempre especifique explicitamente a visibilidade dos membros (para evitar expor declarações como API pública por acidente).
 * Sempre especifique explicitamente os tipos de retorno das funções e os tipos das propriedades (para evitar alterar o tipo de retorno por acidente quando a implementação mudar).
 * Forneça comentários [KDoc](kotlin-doc.md) para todos os membros públicos, exceto para overrides que não exijam nova documentação (para viabilizar a geração de documentação da biblioteca).

Saiba mais sobre boas práticas e ideias a considerar ao escrever uma API para a sua biblioteca em [Diretrizes para autores de bibliotecas](api-guidelines-introduction.md).

<!-- ia-translate: true -->
