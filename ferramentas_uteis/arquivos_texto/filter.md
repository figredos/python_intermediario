# Filter

## O que é

Filter é uma função do python que faz a filtragem de dados em um iterável. De forma similar a map e outras funções usar a função filter é opcional, principalmente para o uso de programação funcional, uma vez que é possível obter os mesmos resultados fazendo um list comprehension (ou equivalente) no iterável.

## Implementação

Assim como a função map, filter recebe uma função (anônima ou não) como primeiro parâmetro, e em seguida o iterável no qual aquela função deverá ser aplicada.

## Vantagem

Similarmente à função map, a grande vantagem de usar um filter ao invés de list comprehension (ou similar) para realizar uma filtragem de dados, é que o list comprehension cria a lista, enquanto o filter cria um objeto iterável.isso implica que o filter usa um espaço menor na memória do que o list comprehension (ou similar).
