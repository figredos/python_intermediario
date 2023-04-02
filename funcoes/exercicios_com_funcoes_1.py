"""
                                EXERCÍCIO
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""


def calcula(vezes):
    def multiplica(valor):
        return valor * vezes

    return multiplica


if __name__ == '__main__':
    duplica = calcula(2)
    triplica = calcula(3)
    quadruplica = calcula(4)

    print(duplica(2))
    print(triplica(2))
    print(quadruplica(2))
