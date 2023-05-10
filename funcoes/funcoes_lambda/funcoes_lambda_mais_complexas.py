def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


print(executa(lambda x, y: x + y, 2, 3))  # Função lambda exercendo a mesma função de soma


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador

    return multiplica


duplica = executa(lambda multiplicador:
                  lambda numero:
                  multiplicador * numero, 2
                  )  # Função lambda exercendo a mesma função de cria_multiplicador

print(duplica(2))
