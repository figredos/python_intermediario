# Anotações

## O que são

Anotações são formas de deixar códigos python mais legíveis. Existem dois tipos de anotações, as de função, que explicitam o tipo de retorno que uma certa função terá, por exemplo, caso uma função retorne um nome em formato str, após o nome da função se encontrará uma seta indicando que o retorno é str:

~~~python
def retorna_nome() -> str:
    return 'Giu'
~~~

É possível também, usar anotações para parâmetros. Isso é feito, ao seguir o nome do parâmetro com ':' e indicar o tipo de dado que aquele parâmetro deve receber.

~~~python
def retorna_nome(letra_inicial: 'str') -> str:
    return 'Giu'
~~~