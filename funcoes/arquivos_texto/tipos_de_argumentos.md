# Tipos de argumentos

## O que são

São uma das formas de escrever e guardar valores em python

## Argumentos não nomeados

São formas de passar argumentos em funções com base na sua posição e não em seu nome. Todo argumento é nomeado, contudo, em grande parte das vezes, não é necessário usa-lo para passar um valor para uma função

## Empacotamento e Desempacotamento de Argumentos

Desempacotar um argumento é uma forma de juntar uma série de valores de uma vez só:

~~~python
x, y, *resto = 1, 2, 3, 4
~~~

Apesar de existirem 4 números para apenas 3 variáveis, quando usamos o símbolo '*', conseguimos juntar todos os elementos restantes, em forma de lista, na variável 'resto'

Empacotar uma variável é o nome dado ao processo contrário ao desempacotamento, onde pegaremos uma série de argumentos e juntaremos todos.

~~~python
def soma(*args):
    return soma(args)
~~~