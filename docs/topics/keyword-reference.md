[//]: # (title: Palavras-chave e operadores)

## Palavras-chave reservadas {id="hard-keywords"}

Os tokens a seguir são sempre interpretados como palavras-chave e não podem ser usados como identificadores:

 * `as`
     - é usado para [conversões de tipo](typecasts.md#unsafe-cast-operator).
     - especifica um [alias para um import](packages.md#imports)
 * `as?` é usado para [conversões de tipo seguras](typecasts.md#unsafe-cast-operator).
 * `break` [encerra a execução de um laço](returns.md).
 * `class` declara uma [classe](classes.md).
 * `continue` [passa para a próxima etapa do laço mais próximo que o envolve](returns.md).
 * `do` inicia um [laço do/while](control-flow.md#while-loops) (um laço com pós-condição).
 * `else` define o ramo de uma [expressão if](control-flow.md#if-expression) executado quando a condição é falsa.
 * `false` especifica o valor 'false' do [tipo Boolean](booleans.md).
 * `for` inicia um [laço for](control-flow.md#for-loops).
 * `fun` declara uma [função](functions.md).
 * `if` inicia uma [expressão if](control-flow.md#if-expression).
 * `in`
     - especifica o objeto percorrido em um [laço for](control-flow.md#for-loops).
     - é usado como operador infixo para verificar se um valor pertence a [um intervalo](ranges.md),
       a uma coleção ou a outra entidade que [define um método 'contains'](operator-overloading.md#in-operator).
     - é usado em [expressões when](control-flow.md#when-expressions-and-statements) com a mesma finalidade.
     - marca um parâmetro de tipo como [contravariante](generics.md#declaration-site-variance).
 * `!in`
     - é usado como operador para verificar se um valor NÃO pertence a [um intervalo](ranges.md),
       a uma coleção ou a outra entidade que [define um método 'contains'](operator-overloading.md#in-operator).
     - é usado em [expressões when](control-flow.md#when-expressions-and-statements) com a mesma finalidade.
 * `interface` declara uma [interface](interfaces.md).
 * `is`
     - verifica se [um valor tem determinado tipo](typecasts.md#is-and-is-operators).
     - é usado em [expressões when](control-flow.md#when-expressions-and-statements) com a mesma finalidade.
 * `!is`
     - verifica se [um valor NÃO tem determinado tipo](typecasts.md#is-and-is-operators).
     - é usado em [expressões when](control-flow.md#when-expressions-and-statements) com a mesma finalidade.
 * `null` é uma constante que representa uma referência de objeto que não aponta para nenhum objeto.
 * `object` declara [uma classe e sua instância ao mesmo tempo](object-declarations.md).
 * `package` especifica o [pacote do arquivo atual](packages.md).
 * `return` [retorna da função ou função anônima mais próxima que a envolve](returns.md).
 * `super`
     - [se refere à implementação da superclasse de um método ou propriedade](inheritance.md#calling-the-superclass-implementation).
     - [chama o construtor da superclasse a partir de um construtor secundário](classes.md#inheritance).
 * `this`
     - se refere [ao receiver atual](this-expressions.md).
     - [chama outro construtor da mesma classe a partir de um construtor secundário](classes.md#constructors-and-initializer-blocks).
 * `throw` [lança uma exceção](exceptions.md).
 * `true` especifica o valor 'true' do [tipo Boolean](booleans.md).
 * `try` [inicia um bloco de tratamento de exceções](exceptions.md).
 * `typealias` declara um [alias de tipo](type-aliases.md).
 * `typeof` é reservada para uso futuro.
 * `val` declara uma [propriedade](properties.md) somente leitura ou uma [variável local](basic-syntax.md#variables).
 * `var` declara uma [propriedade](properties.md) mutável ou uma [variável local](basic-syntax.md#variables).
 * `when` inicia uma [expressão when](control-flow.md#when-expressions-and-statements) (executa um dos ramos informados).
 * `while` inicia um [laço while](control-flow.md#while-loops) (um laço com pré-condição).

## Palavras-chave suaves {id="soft-keywords"}

Os tokens a seguir atuam como palavras-chave no contexto em que são aplicáveis, e podem ser usados
como identificadores em outros contextos:

 * `by`
     - [delega a implementação de uma interface a outro objeto](delegation.md).
     - [delega a implementação dos acessores de uma propriedade a outro objeto](delegated-properties.md).
 * `catch` inicia um bloco que [trata um tipo específico de exceção](exceptions.md).
 * `constructor` declara um [construtor primário ou secundário](classes.md#constructors-and-initializer-blocks).
 * `context` declara [parâmetros de contexto](context-parameters.md) para funções e propriedades.
 * `delegate` é usado como [alvo de uso de anotação](annotations.md#annotation-use-site-targets).
 * `dynamic` faz referência a um [tipo dinâmico](dynamic-type.md) em código Kotlin/JS.
 * `field`
     - declara um [campo de apoio explícito](properties.md#explicit-backing-fields).
     - é usado como [alvo de uso de anotação](annotations.md#annotation-use-site-targets).
 * `file` é usado como [alvo de uso de anotação](annotations.md#annotation-use-site-targets).
 * `finally` inicia um bloco que [é sempre executado quando um bloco try é encerrado](exceptions.md).
 * `get`
     - declara o [getter de uma propriedade](properties.md).
     - é usado como [alvo de uso de anotação](annotations.md#annotation-use-site-targets).
 * `import` [importa uma declaração de outro pacote para o arquivo atual](packages.md).
 * `init` inicia um [bloco de inicialização](classes.md#constructors-and-initializer-blocks).
 * `param` é usado como [alvo de uso de anotação](annotations.md#annotation-use-site-targets).
 * `property` é usado como [alvo de uso de anotação](annotations.md#annotation-use-site-targets).
 * `receiver` é usado como [alvo de uso de anotação](annotations.md#annotation-use-site-targets).
 * `set`
     - declara o [setter de uma propriedade](properties.md).
     - é usado como [alvo de uso de anotação](annotations.md#annotation-use-site-targets).
* `setparam` é usado como [alvo de uso de anotação](annotations.md#annotation-use-site-targets).
* `value` junto com a palavra-chave `class` declara uma [classe inline](inline-classes.md).
* `where` especifica as [restrições para um parâmetro de tipo genérico](generics.md#upper-bounds).

## Palavras-chave de modificador {id="modifier-keywords"}

Os tokens a seguir atuam como palavras-chave nas listas de modificadores das declarações, e podem ser usados como identificadores
em outros contextos:

 * `abstract` marca uma classe ou membro como [abstrato](classes.md#abstract-classes).
 * `actual` indica uma implementação específica de plataforma em [projetos multiplataforma](https://kotlinlang.org/docs/multiplatform/multiplatform-expect-actual.html).
 * `annotation` declara uma [classe de anotação](annotations.md).
 * `companion` declara um [companion object](object-declarations.md#companion-objects).
 * `const` marca uma propriedade como [constante em tempo de compilação](properties.md#compile-time-constants).
 * `crossinline` proíbe [retornos não locais em uma lambda passada para uma função inline](inline-functions.md#returns).
 * `data` instrui o compilador a [gerar membros canônicos para uma classe](data-classes.md).
 * `enum` declara uma [enumeração](enum-classes.md).
 * `expect` marca uma declaração como [específica de plataforma](https://kotlinlang.org/docs/multiplatform/multiplatform-expect-actual.html), esperando uma implementação nos módulos de plataforma.
 * `external` marca uma declaração como implementada fora do Kotlin (acessível por meio de [JNI](java-interop.md#using-jni-with-kotlin) ou em [JavaScript](js-interop.md#external-modifier)).
 * `final` proíbe [sobrescrever um membro](inheritance.md#overriding-methods).
 * `infix` permite chamar uma função usando [notação infixa](functions.md#infix-notation).
 * `inline` instrui o compilador a [expandir inline a função e as lambdas passadas a ela no local da chamada](inline-functions.md).
 * `inner` permite referenciar a instância da classe externa a partir de uma [classe aninhada](nested-classes.md).
 * `internal` marca uma declaração como [visível no módulo atual](visibility-modifiers.md).
 * `lateinit` permite inicializar uma [propriedade não nulável fora de um construtor](properties.md#late-initialized-properties-and-variables).
 * `noinline` desativa a [expansão inline de uma lambda passada para uma função inline](inline-functions.md#noinline).
 * `open` permite [criar subclasses de uma classe ou sobrescrever um membro](classes.md#inheritance).
 * `operator` marca uma função como [sobrecarga de operador ou implementação de uma convenção](operator-overloading.md).
 * `out` marca um parâmetro de tipo como [covariante](generics.md#declaration-site-variance).
 * `override` marca um membro como [sobrescrita de um membro da superclasse](inheritance.md#overriding-methods).
 * `private` marca uma declaração como [visível na classe ou no arquivo atual](visibility-modifiers.md).
 * `protected` marca uma declaração como [visível na classe atual e nas suas subclasses](visibility-modifiers.md).
 * `public` marca uma declaração como [visível em qualquer lugar](visibility-modifiers.md).
 * `reified` marca um parâmetro de tipo de uma função inline como [acessível em tempo de execução](inline-functions.md#reified-type-parameters).
 * `sealed` declara uma [sealed class](sealed-classes.md) (uma classe com herança restrita).
 * `suspend` marca uma função ou lambda como suspensa (utilizável como [coroutine](coroutines-overview.md)).
 * `tailrec` marca uma função como [recursiva de cauda](functions.md#tail-recursive-functions) (permitindo que o compilador substitua a recursão por iteração).
 * `vararg` permite [passar um número variável de argumentos para um parâmetro](functions.md#variable-number-of-arguments-varargs).

## Identificadores especiais {id="special-identifiers"}

Os identificadores a seguir são definidos pelo compilador em contextos específicos, e podem ser usados como identificadores comuns
em outros contextos:

 * `field` é usado dentro de um acessor de propriedade para se referir ao [campo de apoio da propriedade](properties.md#backing-fields).
 * `it` é usado dentro de uma lambda para [se referir ao seu parâmetro implicitamente](lambdas.md#it-implicit-name-of-a-single-parameter).

## Operadores e símbolos especiais {id="operators-and-special-symbols"}

O Kotlin oferece os seguintes operadores e símbolos especiais:

 * `+`, `-`, `*`, `/`, `%` - operadores matemáticos
     - `*` também é usado para [passar um array para um parâmetro vararg](functions.md#variable-number-of-arguments-varargs).
 * `=`
     - operador de atribuição.
     - é usado para especificar [valores padrão para parâmetros](functions.md#parameters-with-default-values).
 * `+=`, `-=`, `*=`, `/=`, `%=` - [operadores de atribuição compostos](operator-overloading.md#augmented-assignments).
 * `++`, `--` - [operadores de incremento e decremento](operator-overloading.md#increments-and-decrements).
 * `&&`, `||`, `!` - operadores lógicos 'e', 'ou' e 'não' (para operações bit a bit, use as [funções infixas](numbers.md#bitwise-operations) correspondentes).
 * `==`, `!=` - [operadores de igualdade](operator-overloading.md#equality-and-inequality-operators) (traduzidos para chamadas de `equals()` para tipos não primitivos).
 * `===`, `!==` - [operadores de igualdade referencial](equality.md#referential-equality).
 * `<`, `>`, `<=`, `>=` - [operadores de comparação](operator-overloading.md#comparison-operators) (traduzidos para chamadas de `compareTo()` para tipos não primitivos).
 * `[`, `]` - [operador de acesso por índice](operator-overloading.md#indexed-access-operator) (traduzido para chamadas de `get` e `set`).
 * `!!` [afirma que uma expressão não é nula](null-safety.md#not-null-assertion-operator).
 * `?.` executa uma [chamada segura](null-safety.md#safe-call-operator) (chama um método ou acessa uma propriedade se o receiver não for nulo).
 * `?:` usa o valor da direita se o valor da esquerda for null (o [operador elvis](null-safety.md#elvis-operator)).
 * `::` cria uma [referência a membro](lambdas.md#function-references) ou uma [referência a classe](reflection.md#obtain-a-runtime-class).
 * `.`
     - acessa [membros](classes.md), incluindo [classes aninhadas](nested-classes.md) e [entradas de enum](enum-classes.md#working-with-enum-constants).
     - define e chama [extensões](extensions.md).
     - qualifica nomes e [pacotes](packages.md).
     - separa a parte inteira e a fracionária de um [literal de ponto flutuante](numbers.md#floating-point-types).
 * `..`, `..<` criam [intervalos](ranges.md).
 * `:` separa um nome de um tipo em uma declaração.
 * `?` marca um tipo como [nulável](null-safety.md#nullable-types-and-non-nullable-types).
 * `->`
     - separa os parâmetros e o corpo de uma [expressão lambda](lambdas.md#lambda-expression-syntax).
     - separa os parâmetros e a declaração do tipo de retorno em um [tipo de função](lambdas.md#function-types).
     - separa a condição e o corpo de um ramo de uma [expressão when](control-flow.md#when-expressions-and-statements).
 * `@`
     - introduz uma [anotação](annotations.md#usage).
     - introduz ou referencia um [rótulo de laço](returns.md#break-and-continue-labels).
     - introduz ou referencia um [rótulo de lambda](returns.md#return-to-labels).
     - referencia uma [expressão 'this' de um escopo externo](this-expressions.md#qualified-this).
     - referencia uma [superclasse externa](inheritance.md#calling-the-superclass-implementation).
 * `;` separa várias instruções na mesma linha.
 * `$` referencia uma variável ou expressão em um [template de string](strings.md#string-templates).
 * `_`
     - substitui um parâmetro não utilizado em uma [expressão lambda](lambdas.md#underscore-for-unused-variables).
     - substitui um parâmetro não utilizado em uma [declaração de desestruturação](destructuring-declarations.md#underscore-for-unused-variables).

Para a precedência dos operadores, veja [esta referência](https://kotlinlang.org/grammar/#expressions) na gramática do Kotlin.

<!-- ia-translate: true -->
