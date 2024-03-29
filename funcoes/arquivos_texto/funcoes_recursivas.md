# Funções recursivas

## O que são

Funções recursivas são funções que usam de si mesmas dentro do seu escopo. Ou seja, caso alguma condição, checada dentro da função seja ou não verdadeira, a função repete a sua chamada dentro de si mesma, possibilitando um uso recursivo. São úteis para dividir problemas grandes em partes menores. Toda função recursiva deve ter, um problema que possa ser dividido em partes menores (calcular os digitos de validação de um cpf), um caso recursiva que resolve o pequeno problema e um caso base (para que a função interrompa a execução após um ponto).

## Implementação

A implementação de uma função recursiva é extremamente simples, é necessário apenas usar a função dentro de seu próprio escopo. Contudo, é importante impedir que a função execute ininterruptamente, usando algum tipo de checagem dentro do seu escopo, antes de fazer a recursividade.

## Stack Overflow

Stack overflow é o nome dado à situação onde uma função recursiva excede um limite de recursões ininterruptas, isso ocorre para que o python não "afogue" a memória do computador. Isso pode ocorrer pois o código salva os valores da função dentro da memória do computador, uma vez que o código está rodando de forma ininterrupta, eventualmente, o valor salvo será extremamente grande de forma a causar danos à capacidade da máquina de salva-lo.
