# Sets

## O que são sets

Sets são uma das formas mutáveis de dados em python. São similares a conjuntos matemáticos. Possuem algumas peculiaridades, não possuem dados repetidos, não possuem índices, não tem ordem específica. Sets só aceitam  dados imutáveis.

## Qual a utilidade de sets

A grande utilidade de sets, é justamente sua grande particularidade, não ter dados repetidos. Isso implica que podem facilmente ser usados para eliminar dados repetidos, checar a existência de dados em um outro iterável, etc.

## Como criar um set

Como grande parte dos tipos de dados, é possível criar sets usando uma função específica, 'set()' (a função   set(), iteram sobre o dado que é entregue a eles, e os separam em dados não repetidos). Contudo, a forma mais simples é usando um par de '{}'. Apesar de usarem os mesmos caracteres para serem criados, sets e dicts diferem num simples aspecto, sets não possuem chaves, apenas valores.

## Métodos úteis

Sets, como muitas coisas em python, são um tipo de objeto, e assim como outros objetos (ver POO) possuem métodos. Estes são alguns dos mais úteis de sets:

 ~ add - adiciona um valor ao set.

 ~ update - de forma similar o add, adiciona um valor ao set, contudo, é de forma iterada.

 ~ clear - limpa o set

 ~ discard - elimina um valor específico

## Operadores úteis

Sets também possuem operadores únicos, que ajudam , principalmente, em operações com mais de um set. Alguns deles são:

 ~ | (União): Une dois sets

 ~ & (intersecção): Valores em comum entre dois sets

 ~ - (diferença): Itens presentes apenas no set da esquerda

 ~ ^ (diferença simétrica): Itens que não estão em ambos os sets

## Set Comprehension

É uma forma simplificada de criar sets. VER LIST COMPREHENSION