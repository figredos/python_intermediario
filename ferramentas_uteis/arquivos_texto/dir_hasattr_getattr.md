# dir hasattr getattr

## dir

É uma função que mostra todos os métodos de uma determinada classe. A função recebe como seu argumento o objeto o qual é intendido iterar sobre os atributos, e os retorna em formato de lista.

## hasattr

É uma função que checa a presença de um argumento nomeado como um método da classe. Recebe como argumento um objeto, e o nome do método a ser buscado, e retorna um booleano, True caso tenha sido encontrado o método, e False caso contrário.

## getattr

É uma função que retorna o método buscado, de forma similar a uma high order function (ver 'funcoes/higher_order_functions.py'). Recebe como argumento um objeto e um método, de forma similar à função hasattr, contudo possui em seu retorno o método caso encontrado.
