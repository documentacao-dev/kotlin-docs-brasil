[//]: # (title: Retornos e saltos)

O Kotlin tem três expressões de salto estruturais:

* `return` retorna, por padrão, da função mais próxima que a envolve ou de uma [função anônima](lambdas.md#anonymous-functions).
* `break` encerra o laço mais próximo que o envolve.
* `continue` avança para o próximo passo do laço mais próximo que o envolve.

Todas essas expressões podem ser usadas como parte de expressões maiores:

```kotlin
val s = person.name ?: return
```

O tipo dessas expressões é o [tipo Nothing](exceptions.md#the-nothing-type).

## Rótulos de break e continue {id="break-and-continue-labels"}

Qualquer expressão em Kotlin pode ser marcada com um _rótulo_.
Rótulos têm a forma de um identificador seguido do sinal `@`, como `abc@` ou `fooBar@`.
Para rotular uma expressão, basta adicionar um rótulo na frente dela.

```kotlin
loop@ for (i in 1..100) {
    // ...
}
```

Agora, você pode qualificar um `break` ou um `continue` com um rótulo:

```kotlin
loop@ for (i in 1..100) {
    for (j in 1..100) {
        if (...) break@loop
    }
}
```

Um `break` qualificado com um rótulo salta para o ponto de execução logo após o laço marcado com esse rótulo.
Um `continue` avança para a próxima iteração desse laço.

> Em alguns casos, você pode aplicar `break` e `continue` *de forma não local* sem definir rótulos explicitamente.
> Esses usos não locais são válidos em expressões lambda usadas dentro de [funções inline](inline-functions.md#break-and-continue) que as envolvem.
>
{style="note"}

## Retorno para rótulos {id="return-to-labels"}

No Kotlin, funções podem ser aninhadas usando literais de função, funções locais e expressões de objeto.
Um `return` qualificado permite retornar de uma função externa.

O caso de uso mais importante é retornar de uma expressão lambda. Para retornar de uma expressão lambda,
rotule-a e qualifique o `return`:

```kotlin
//sampleStart
fun foo() {
    listOf(1, 2, 3, 4, 5).forEach lit@{
        if (it == 3) return@lit // local return to the caller of the lambda - the forEach loop
        print(it)
    }
    print(" done with explicit label")
}
//sampleEnd

fun main() {
    foo()
}
```
{kotlin-runnable="true"}

Agora, ele retorna apenas da expressão lambda. Muitas vezes é mais conveniente usar _rótulos implícitos_, porque esse rótulo
tem o mesmo nome da função à qual a lambda é passada.

```kotlin
//sampleStart
fun foo() {
    listOf(1, 2, 3, 4, 5).forEach {
        if (it == 3) return@forEach // local return to the caller of the lambda - the forEach loop
        print(it)
    }
    print(" done with implicit label")
}
//sampleEnd

fun main() {
    foo()
}
```
{kotlin-runnable="true"}

Como alternativa, você pode substituir a expressão lambda por uma [função anônima](lambdas.md#anonymous-functions).
Um `return` em uma função anônima retorna da própria função anônima.

```kotlin
//sampleStart
fun foo() {
    listOf(1, 2, 3, 4, 5).forEach(fun(value: Int) {
        if (value == 3) return  // local return to the caller of the anonymous function - the forEach loop
        print(value)
    })
    print(" done with anonymous function")
}
//sampleEnd

fun main() {
    foo()
}
```
{kotlin-runnable="true"}

Observe que o uso de retornos locais nos três exemplos anteriores é semelhante ao uso de `continue` em laços regulares.

Não existe um equivalente direto para `break`, mas ele pode ser simulado adicionando uma lambda `run` externa
e retornando de forma não local a partir dela:

```kotlin
//sampleStart
fun foo() {
    run loop@{
        listOf(1, 2, 3, 4, 5).forEach {
            if (it == 3) return@loop // non-local return from the lambda passed to run
            print(it)
        }
    }
    print(" done with nested loop")
}
//sampleEnd

fun main() {
    foo()
}
```
{kotlin-runnable="true"}

O retorno não local aqui é possível porque a lambda do `forEach()` aninhado atua como uma [função inline](inline-functions.md).

Ao retornar um valor, o parser dá preferência ao return qualificado:

```kotlin
return@a 1
```

Isso significa "retornar `1` no rótulo `@a`" e não "retornar uma expressão rotulada `(@a 1)`".

> Em alguns casos, você pode retornar de uma expressão lambda sem usar rótulos. Esses retornos *não locais* ficam em uma lambda,
> mas saem da [função inline](inline-functions.md#returns) que a envolve.
>
{style="note"}

<!-- ia-translate: true -->
