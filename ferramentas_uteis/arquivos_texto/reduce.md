# Reduce 

## O que é

Reduce é uma função do pacote functools que faz a redução de um iterável em um valor. Por exemplo, suponha que gostaríamos de somar os elementos da lista [1, 2, 3, 4, 5] e para isso, gostariamos de usar um reduce. Isso seria
feito da seguinte maneira;

~~~python
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
~~~

A função acima resulta em 15

A função pode receber também um valor inicial, após o iterável:

~~~python
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 1)
~~~

A partir da função acima, chegamos ao valor 16, porque a soma é feita a partir do valor 1.

Obs.: É uma boa prática o uso do acumulador, pois evita erros relacionados à soma entre dois tipos diferentes de dados.
