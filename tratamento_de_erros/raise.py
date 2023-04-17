# Função que gera um erro ao tentar dividir por zero
def erro_divide_por_zero(numero):
    if numero == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero!')
    return True


# Função que gera um erro se o parâmetro numero diferir de int ou float
def deve_ser_int_ou_float(numero):
    if not isinstance(numero, (float, int)):
        raise TypeError(
            f'{numero} deve ser int ou float.'
        )


# Função que checa os dados com tratamento de exceções e retorna a divisão entre os parâmetros
def divide(numerador, divisor):
    deve_ser_int_ou_float(numerador)
    deve_ser_int_ou_float(divisor)
    erro_divide_por_zero(divisor)
    return numerador / divisor
