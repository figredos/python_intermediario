# Diminuir condicionais

Um dos grandes problemas de qualquer dev, é o uso excessivo de condicionais. Existem algumas formas de evitar isso, seja pelo uso de uma alternativa, ou até mesmo entendendo melhor o uso delas e usando os chamados "Guard Clause".

## Guard Clause

Guard Clause, ou Guard, é uma forma de diminuir o uso de condicionais, apenas com a melhor escrita das mesmas. Como pode ser visto no exemplo a seguir, o uso do condicional else não é necessário, uma vez que, caso a condição checada pelo if seja verdadeira, qualquer código escrito após o mesmo não será executado, tornando o else obsoleto.

Ex.:

~~~python
if "condição":
print('Condição é verdadeira')
else:
print('Condição é falsa')
~~~

O código acima, pode ser escrito da seguinte forma:

~~~python
if "condição":
    print('Condição é verdadeira')

print('Condição é falsa')
~~~

Ex_2.:

~~~python
if "condição":
    print('Retorno não necessário')
else:
    return
~~~

O código acima, pode ser escrito da seguinte forma:

~~~python
if not "condição":
    return

print('Retorno não necessário')
~~~

## Outras formas de evitar condicionais

Existem diversas formas de se evitar o uso de condicionais, esse processo tem o intuito de tornar o código mais simples e legível. Um deles, para uma situação onde após a checagem de uma condição, é executada uma função, pode ser criado um dicionário contendo as possibilidades a serem checadas, e cada chave do dicionário recebe uma função lambda da função a ser executada (com intuito de adiar a execução dessa função).
