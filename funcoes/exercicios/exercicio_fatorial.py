"""
Função Fatorial

Função que calcula o fatorial do número inserido. Fatorial é uma operação matemática que calcula a multiplicação entre
todos os números que precedem o valor n de n!, sendo n! = n * n-1 * n-2 * ... * 3 * 2 * 1.
A função fatorial tem como argumentos o valor 'n', do qual será calculado o fatorial, um 'numero' que será acrescido de
1 até o momento onde for igual ao número 'n', e um 'acumulador', que recebe a multiplicação dos valores até 'numero'
chegar a 'n'. A função é regressiva, ou seja, é chamada dentro do seu próprio escopo até o valor de 'numero' igualar
'n'.
"""

def fatorial(n, numero=1, acumulador=1):
    acumulador *= numero

    if numero < n:
        numero += 1
        return fatorial(n, numero, acumulador)


    return acumulador

