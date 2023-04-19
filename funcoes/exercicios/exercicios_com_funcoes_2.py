# Usar a função cria
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def executa_funcao(funcao, x):
    def executando(y):
        return funcao(x, y)
    return executando


soma_com_cinco = executa_funcao(soma, 5)
multiplica_por_dez = executa_funcao(multiplica, 10)

print(soma_com_cinco(5))