# Zip

## O que é

É uma ferramenta do python que cria um iterável que agrega os elementos de dois ou mais iteráveis. Junta os elementos de cada um em ordem, o primeiro com o primeiro, o segundo com o segundo e assim por diante. Faz isso baseado no tamanho do menor iterável. Retorna um zip object, que pode ser transformado em listas, tuplas, etc.

## zip_longest

Ferramenta do módulo itertools, que exerce a mesma função do zip, contudo, ao invés de usar o tamanho do iterável menor, ele usa o iterável maior. Quando existem uma lista com tamanho maior que a outra, ele agrega um elemento none à o elemento que falta na lista menor.