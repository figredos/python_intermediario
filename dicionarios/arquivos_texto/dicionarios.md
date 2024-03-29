# Dicionários

## O que são

São estrutura de dados do tipo "par chave e valor". São uma forma de organizar mais minuciosamente os dados em python. Chaves podem ser consideradas como o índice de um dicionário, de forma sililar a o uso de índices em listas. As chaves podem ser de tipos imutáveis; int, float; bool; tupla; str, etc. Valores, contudo, podem ser de qualquer tipo, seja mutável ou não, podendo assumir até mesmo valor de outros dicionários.

## Implementação

Para usar um dicionário, usa-se a notação '{}'. Para chaves e valores, usamos a seguinte notação:

~~~Python
meu_dicionario = {chave : valor}
~~~

Dicionarios podem ser criados usando o comando dict(), assim como listas podem usar list().

## Manipulando chaves e valores

É possível criar uma chave com valor num dicionário, simplesmente adicionando um valor a uma chave préviamente não existente, o mesmo serve para valores, sendo possível adicionar valores a chaves existentes, simplesmente atribuindo um valor à aquela chave. Para deletar uma chave, simplesmente usar o comando 'del' seguido pela chave a qual se quer apagar.

Obs.: Caso sejam criadas várias chaves com nomes iguais, a última será a única mantida. É como se a chave estivesse sendo atualizada constantemente.

## Métodos úteis

Dicionários, como muitas coisas em python, são um tipo de objeto, e assim como outros objetos (ver POO) possuem métodos. Estes são alguns dos mais úteis de dicionários:

~ len - informa quantas chaves o dicionário possui

~ keys - é um iterável para as chaves

~ values - é um iterável para os valores

~ items - é um iterável para as chaves e para os valores

~ setdefault - adiciona um valor caso a chave não exista

~ copy - retorna uma cópia rasa (shallow copu)

~ get - obtém chave

~ pop - apaga um item com a chave especificada (del)

~ popitem - apaga o último item adicionado

~ update - atualiza um dicionário com outro

## Tipos de cópia de dicionário

Shallow copy é um tipo de cópia que faz com que tudo o que for mutável dentro de um dicionário seja copiado para o outro. Contudo, caso dentro do dicionário exista algum tipo de valor mutável, tanto o dicionário original quanto a cópia apontam para o mesmo local da memória, fazendo com que os valores sendo alterados em apenas um dicionário afete ambos. Para essa função existe o método .deepcopy(), que copia todas as estruturas de um dicionário para outro, sejam essas mutáveis ou não.

## Empacotando e Desempacotando

É possível fazer o empacotamento e desempacotamento de um dicionário em python. Para fazer o desempacotamento e até mesmo o empacotamento de um dicionário em outro, ou fazer a união de dois dicionários em um só, podemos usar '**' antes do nome do dicionário, fazendo com que o desempacotamento do dicionário.

## **kwargs (argumentos nomeados)

Argumentos nomeados são um tipo de dado em python que tem um formato de dicionário, ou seja, possui chave e valor, ou seja são nomeados.

## Dict Comprehension

É uma forma simplificada de criar dicts. VER LIST COMPREHENSION
