# Funções decoradoras

## O que são

Decorators, ou funções decoradoras são uma forma de executar funções mais facilmente, principalmente quandoexiste uma função de higher order (que retorna outra função) com closure.

## Como implementar e sintax sugar

Syntax sugar (açúcar sintático), é o nome dado à forma com a qual são implementados os decoradores em python. É feito usando um "@", seguido pelo nome da função a qual deve ser decorada. É chamado assim pois são a forma usada para simplificar o código.

## Funcionamento da função decoradora

A função decoradora, como estabelecido previamente, é a responsável por decorar outras funções. Ela faz isso usando o conceito de higher order functions, onde tem como retorno uma função, e é usada também, com closure, onde se adia a execução de uma função. O compilador do python, quando identifica um syntax sugar acima de uma função torna a execução da função requisitada como se fosse o da função interna da decoradora.

## Decoradores com parâmetros

É possível usar decoradores que recebem parâmetros. Isso é feito, utilizando uma função decoradora no próprio decorador. Fazendo isso o decorador menor se encontra no escopo do decorador maior, da mesma forma que a função interna está no escopo do decorador menor. Decoradores são aplicados em order decrescente, sendo que o primeiro a ser executado será o mais de baixo.

Obs.: Pensar em decoradores, como literalmente decoradores, uma vez que a função deles é adicionar coisas a funções com o intuito de adicionar, restringir, alterar, remover coisas de funções.