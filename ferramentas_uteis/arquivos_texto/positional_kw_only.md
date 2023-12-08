# Positional only e Keyword only

## O que é

Funções recebem argumentos, podem ser key word ou posicionais, por padrão, o python aceita dentro de uma função, a chamada posicional ou usando o nome do argumento (key word). Contudo, é possível que essa disposição acabe por gerar problemas no código, caso, por exemplo, alguma função esteja sendo chamada usando key word, e essa chave mude. Portando é possível definir argumentos que não podem nunca ser usados como key word, assim como exigir que eles sejam usados dessa forma.

## Positional only parameters (/)

Usar '/' após um, ou uma série de argumento, "informa" o python de que os argumentos que precedem '/' devem ser apenas posicionais. Caso tente usar o argumento como nomeado, é levantado um erro de tipo, pois um argumento posicional está sendo usado como nomeado.

## Keyword only arguments (*)

O uso de '\*' precedendo um ou uma série de argumentos, "informa" o python de que os argumentos que sucedem '*' devem obrigatoriamente ser nomeados. Caso tente usar o argumento como posicional, é levantado um erro de tipo, pois um argumento nomeado está sendo usado como posicional.
