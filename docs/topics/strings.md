[//]: # (title: Strings)
<web-summary>Aprenda a trabalhar com strings em Kotlin, incluindo literais de string, templates de string, strings de múltiplas linhas e operações comuns com texto.</web-summary>

O tipo [`String`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) representa uma sequência de
[caracteres](characters.md). Você pode usá-lo para valores de texto, como palavras, frases, mensagens ou texto estruturado.

O tipo `String` é imutável. Depois que você cria um objeto `String`,
o conteúdo dele permanece o mesmo durante toda a vida útil. Qualquer operação que pareça
modificar a string, na verdade, cria uma nova string.

## Declarar strings {id="declare-strings"}

Para declarar um literal `String`, coloque o valor entre aspas duplas (`""`). Você pode especificar o tipo `String`
explicitamente ou deixar o Kotlin inferir o tipo a partir do valor:

```kotlin
val name: String = "Kotlin"
val message = "Hello, world!" // Kotlin infers String
```

Literais de string entre aspas duplas aceitam [sequências de escape](characters.md#escape-sequences), como `\n` ou `\t`:

```kotlin
val message = "Hello,\nworld!"
val quote = "Kotlin says, \"Hi\"."
```

### Strings de múltiplas linhas {id="multiline-strings"}

Para armazenar um texto que consiste em várias linhas ou que contém aspas que você não quer escapar,
use uma string de múltiplas linhas delimitada por aspas triplas (`""" """`):

```kotlin
val text = """
Hello,
Kotlin
"""

val quote = """Kotlin says, "Hi"."""
```

> Strings de múltiplas linhas não aceitam sequências de escape.
> O Kotlin trata esses caracteres como texto comum.
>
{style="note"}

Strings de múltiplas linhas preservam as quebras de linha e as indentações conforme escritas no código-fonte.
Esse comportamento é útil quando você quer que o valor em tempo de execução corresponda ao layout do texto no arquivo.

No exemplo a seguir, os espaços antes de cada linha fazem parte da string resultante:

```kotlin
val text = """
    Hello,
    Kotlin
"""
```

Para remover a indentação inicial comum, use
a função [`trimIndent()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/trim-indent.html). Ela detecta a indentação mínima comum das linhas não vazias e a remove:

```kotlin
fun main() {
//sampleStart
    val text = """
        Hello,
        Kotlin
    """.trimIndent()
    
    println(text)
//sampleEnd
}
```
{kotlin-runnable="true"}

Para controlar a remoção de indentação de forma mais explícita, use
a função [`trimMargin()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/trim-margin.html). Ela
remove tudo antes e incluindo o prefixo de margem em cada linha:

```kotlin
fun main() {
//sampleStart
    val text = """
        |Hello,
        |Kotlin
    """.trimMargin()
    
    println(text)
//sampleEnd
}
```
{kotlin-runnable="true"}

Por padrão, a função `trimMargin()` usa o caractere de barra vertical (`|`) como prefixo de margem, mas você pode passar outro caractere
como parâmetro. Por exemplo: `trimMargin(">")`.

> Quando você processa uma string com funções como `trimIndent()` ou `trimMargin()`, a string resultante
> usa apenas separadores de nova linha (`\n`), independentemente da plataforma.
>
{style="note"}


## Templates de string {id="string-templates"}

Templates de string permitem incluir variáveis e expressões diretamente dentro de um literal `String`.
Esse processo é chamado de _interpolação_. Você pode usar templates de string tanto em strings comuns
quanto em strings de múltiplas linhas.

Para inserir uma variável em uma string, use o símbolo `$`:

```kotlin
fun main() { 
//sampleStart
    val name = "Kotlin"
    println("Hello, $name") 
    // Hello, Kotlin
//sampleEnd
}
```
{kotlin-runnable="true"}

Para inserir uma expressão em uma string ou colocar uma variável diretamente ao lado de outro texto, use `${}`:

```kotlin
fun main() {
//sampleStart
    val text = "abc"
    println("The length of $text is ${text.length}")
    // The length of abc is 3
      
    val language = "Kotlin"
    println("${language}Lang")
    // KotlinLang
//sampleEnd
}
```
{kotlin-runnable="true"}

> Você também pode combinar strings com o operador `+`. No entanto, templates de string costumam ser
> mais fáceis de ler e mais idiomáticos.
>
{style="tip"}

Expressões de template também podem conter strings entre aspas duplas sem escape:

```kotlin
// Double-quoted string
val test = "${"test".uppercase()}"

// Multiline string
val result = """
Result: ${"OK".lowercase()}
"""
```

### Valores anuláveis em templates de string {id="nullable-values-in-string-templates"}

Se uma expressão ou variável interpolada resultar em `null`, o compilador do Kotlin
insere o texto `null` na string resultante. Para substituir `null` por outro valor,
use o [operador Elvis](null-safety.md#elvis-operator) (`?:`):

```kotlin 
fun main(){
//sampleStart
    val text: String? = null
  
    println("Hello, $text")
    // Hello, null

    println("Hello, ${text ?: "Kotlin"}")
    // Hello, Kotlin
//sampleEnd
}
```
{kotlin-runnable="true"}

### Interpolação de string com múltiplos cifrões {id="multi-dollar-string-interpolation"}

Em templates de string comuns, um único cifrão (`$`) inicia a interpolação. Se você precisar
incluir cifrões literais em uma string, use a **interpolação de string com múltiplos cifrões**.

A interpolação de string com múltiplos cifrões permite especificar quantos cifrões consecutivos são
necessários para disparar a interpolação. Cifrões em quantidade menor que esse número são tratados como caracteres literais.

Por exemplo, quando você usa `$$` antes de um literal de string,
a interpolação começa somente com dois cifrões consecutivos:

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

> Se você usa a interpolação de string com um único cifrão, a interpolação com múltiplos cifrões não afeta o código.
> Você pode continuar usando um único `$` e aplicar múltiplos cifrões
> quando precisar.
>
{style="tip"}

## Operações básicas com strings {id="basic-string-operations"}

O Kotlin oferece várias operações para trabalhar com strings. Esta seção apresenta algumas das mais usadas.

> Saiba mais sobre todas as funções disponíveis na
> [referência da API](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/).
>
{style="tip"}

### Obter o tamanho da string {id="get-string-length"}

Para obter o número de caracteres em uma string, use a propriedade
[`length`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/length.html):

```kotlin 
fun main (){
//sampleStart
    val language = "Kotlin"
    println(language.length)
    // 6
//sampleEnd
}
```
{kotlin-runnable="true"}

### Acessar caracteres {id="access-characters"}

Você pode acessar um caractere individual em uma string
com o operador de índice (`[]`):

```kotlin 
fun main (){
//sampleStart
    val language = "Kotlin"
    
    println(language[0])
    // K
    println(language[5])
    // n
//sampleEnd
}
```
{kotlin-runnable="true"}

> O índice de uma string começa em zero.
> Se você tentar acessar um índice fora do intervalo válido, o Kotlin lança uma exceção.
>
{style="tip"}

Você também pode iterar sobre os caracteres de uma string:

```kotlin
fun main(){
//sampleStart
    for (char in "Kotlin") {
      println(char)
    }
//sampleEnd    
}
```
{kotlin-runnable="true"}

### Extrair partes de uma string {id="extract-parts-of-a-string"}

Para extrair partes de uma string, use uma das seguintes funções:

* [`substring()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/substring.html) para retornar uma nova string com a parte selecionada do
  texto original.
* [`subSequence()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/sub-sequence.html) para retornar uma `CharSequence` com a parte selecionada
  do texto original.

Por exemplo:

```kotlin
fun main() {
//sampleStart    
    val text = "Kotlin"
    println(text.substring(1))
    // otlin
    println(text.substring(1, 5))
    // otli
    println(text.subSequence(1, 5))
    // otli
//sampleEnd
}
```
{kotlin-runnable="true"}

Como o tipo `String` é imutável, essas funções não modificam a string original.

### Comparar strings {id="compare-strings"}

Você pode verificar se duas strings têm o mesmo conteúdo com o operador `==`:

```kotlin
fun main(){
//sampleStart
    println("kotlin" == "kotlin")
    // true
  
    println("kotlin" == "Kotlin")
    // false
//sampleEnd    
}
```
{kotlin-runnable="true"}

Você também pode comparar strings lexicograficamente (caractere por caractere) com a função [`compareTo()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/compare-to.html).
Ela percorre as duas strings até encontrar o primeiro par de caracteres diferentes e retorna:

* `0` quando as strings são iguais.
* Um valor menor que `0` quando o receiver é menor que o argumento.
* Um valor maior que `0` quando o receiver é maior que o argumento.

```kotlin
fun main() {
//sampleStart    
    println("abc".compareTo("abd") < 0)
    // true
    
    println("abc".compareTo("ABC") > 0)
    // true
    
    // Pass true to ignore case differences
    println("abc".compareTo("ABC", ignoreCase = true) == 0)
    // true
//sampleEnd  
}
```
{kotlin-runnable="true"}

### Trabalhar com o conteúdo da string {id="work-with-string-content"}

Se você quiser alterar o conteúdo de uma string, crie uma cópia modificada dela
com funções como [`.trim()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/trim.html), [`.replace()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/replace.html),
[`.uppercase()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/uppercase.html) e [`.lowercase()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/lowercase.html):

```kotlin
fun main() {
//sampleStart
    val text = "  Hello, Kotlin  "

    println(text.trim())
    // Hello, Kotlin

    println(text.replace("Kotlin", "world"))
    //   Hello, world  

    println(text.uppercase())
    //   HELLO, KOTLIN  

    println(text.lowercase())
    //   hello, kotlin  
//sampleEnd    
}
```
{kotlin-runnable="true"}

Você também pode verificar o conteúdo da string com as funções
[`contains()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/contains.html), [`startsWith()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/starts-with.html)
e [`endsWith()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/ends-with.html):

```kotlin
fun main() { 
//sampleStart
    val domain = "kotlinlang.org"
    
    // Checks if the string contains "."
    println(domain.contains("."))
    // true
    
    // Checks if the string starts with "kotlin"
    println(domain.startsWith("kotlin"))
    // true
    
    // Checks if the string ends with ".org"
    println(domain.endsWith(".org"))
    // true
//sampleEnd
}
 ```
{kotlin-runnable="true"}

### Dividir strings {id="split-strings"}

Você pode dividir uma string em partes usando um delimitador com
a função [`split()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/split.html):

```kotlin
fun main() { 
//sampleStart
    val numbers = "one, two, three"
    println(numbers.split(", "))
    // [one, two, three]
//sampleEnd
}
```
{kotlin-runnable="true"}

Se você quiser dividir uma string em linhas individuais, use
a função [`lines()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/lines.html):

```kotlin
fun main() { 
//sampleStart
    val numbers = "one\ntwo\nthree"
    println(numbers.lines())
    // [one, two, three]
//sampleEnd
}
```
{kotlin-runnable="true"}

### Montar e formatar strings {id="build-and-format-strings"}

> Para a maioria das tarefas de formatação no Kotlin, use [templates de string](#string-templates).
>
{style="tip"}

Quando você concatena strings com o operador `+`, o Kotlin cria um novo objeto `String` a cada operação.
No entanto, essa abordagem pode ser ineficiente em loops ou ao montar muitos pedaços.
Para evitar esses problemas, você pode usar a função `buildString()` ou `StringBuilder`. Eles reúnem
todos os pedaços em um único buffer mutável e produzem apenas uma string no final.

Use a função [`buildString()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/build-string.html)
quando a lógica que determina o que anexar for complexa. Por exemplo, quando você tem várias condições
que contribuem com um fragmento diferente. Com `buildString()`, você não manipula o buffer diretamente.
A função cria um `StringBuilder` internamente, executa o bloco e retorna a string resultante.

```kotlin
fun main() {
//sampleStart

    val hasErrors = true
    val hasWarnings = true
    val isComplete = false
    
    // buildString creates an empty buffer
    val status = buildString {
        // Appends "Errors found" to the buffer
        if (hasErrors) append("Errors found")
        if (hasWarnings) {
            // The buffer is not empty, appends "; "
            if (isNotEmpty()) append("; ")
            // Appends "Warnings found"
            append("Warnings found")
        }
        // isComplete = false, nothing to append
        if (isComplete) {
            if (isNotEmpty()) append("; ")
            append("Completed")
        }
        // The buffer is not empty, skips the fallback
        if (isEmpty()) append("OK")
    }
    
    println(status)
    // Errors found; Warnings found
//sampleEnd
}
```
{kotlin-runnable="true"}

Use [`StringBuilder`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/-string-builder/) quando precisar do buffer como um valor explícito.
Por exemplo, para alterar o texto existente:

```kotlin
fun main() {
//sampleStart
    val text = "Hello, Kotlin"
    val builder = StringBuilder(text)

    builder.replace(7, 13, "world")
    println(builder.toString()) 
    // Hello, world
//sampleEnd
}
```
{kotlin-runnable="true"}

Na JVM, você também pode formatar uma string com a função [`String.format()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/format.html):

```kotlin
val text = String.format("Hello, %s", "Kotlin") 
```  

> Use a função `String.format()` somente quando precisar especificamente de especificadores de formatação
> no estilo do formatador na JVM.
> Saiba mais sobre especificadores de formatação na [documentação da Java Class Formatter](https://docs.oracle.com/javase/8/docs/api/java/util/Formatter.html#summary).
>
{style="note"}

## Conversão de strings {id="string-conversion"}

Muitas vezes, strings são usadas para representar valores de outros tipos, como números, valores `Boolean` ou identificadores vindos da entrada.
O Kotlin oferece funções para converter valores em strings e para converter strings em outros tipos.

Para retornar uma representação em string de um valor, use a função [`toString()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/to-string.html):

```kotlin
val number = 10
val text = number.toString()
```

Em templates de string e na concatenação de strings, o Kotlin converte valores para string automaticamente.

Para converter uma string em outro tipo, use as funções de parsing correspondentes:

* Para valores inteiros: [`toByte()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-byte.html), [`toShort()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-short.html), [`toInt()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-int.html), [`toLong()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-long.html)
* Para valores de ponto flutuante: [`toDouble()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-double.html), [`toFloat()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-float.html)
* Para booleanos: [`toBoolean()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-boolean.html), [`toBooleanStrict()`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-boolean-strict.html)

Essas funções retornam um valor do tipo solicitado se a string tiver um formato válido.
Se a entrada puder ser inválida, use as variantes `OrNull`. Elas retornam `null`
em vez de lançar uma exceção, o que as torna seguras para entrada do usuário ou para dados que você não controla
totalmente:

```kotlin
val toInt = "10".toInt() // 10

// 1000000000000 exceeds maximum value of Int
val toIntInvalid = "1000000000000".toIntOrNull()

val toBoolean = "true".toBooleanStrict() // true
val toBooleanInvalid = "yes".toBooleanStrictOrNull() // null
```

<!-- ia-translate: true -->
