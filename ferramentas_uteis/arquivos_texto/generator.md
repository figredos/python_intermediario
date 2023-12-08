# Generator

## O que é

Generator é uma forma mais simples e rápida de implementar o protocolo Iterator, pois não necessita a criação de uma classe para tal. Podem ser usados para fazer funções ocuparem menos espaço na memória, o python faz isso, pois o generator só puxa um valor de cada vez, possibilitando ocupar apenas o espaço de um dado na memória. É uma função que sabe pausar.

## Como implementar

Generators podem ser implementados usando ao invés de return numa função, yield. Ou também usando parênteses numa list comprehension ou dado do tipo.

## Generator functions

Em generator functions, onde existe um "retorno" yield, a função age como iterável, ou seja, ela não é executada de uma vez, mas sim a cada vez que é iterada.
