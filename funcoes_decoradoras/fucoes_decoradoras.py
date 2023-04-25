# Criando uma função que decora outras
def creates_function(func):
    def internal(*args, **kwargs):
        print('Decorando')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O resultado obtido foi de {resultado}')
        print('A função foi decorada.')
        return resultado

    return internal


# Decorando a função que inverte a string
@creates_function
def inverts_string(string):
    return string[::-1]

# Criando a função que checa o parâmetro entregue
def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parâmetro deve ser uma string!')


if __name__ == '__main__':
    print(inverts_string('ooi'))
