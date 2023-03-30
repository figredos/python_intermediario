"""
                                    Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável

Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.

"""


def multiplica(*args):
    total = 0

    for numero in args:
        total *= numero

    return total


def par_impar(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} é ímpar!')


if __name__ == '__main__':
    numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    print(multiplica(*numeros))

    par_impar(87625438974653)