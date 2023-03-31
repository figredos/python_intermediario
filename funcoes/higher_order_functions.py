"""
                                        HIGHER ORDER FUNCTIONS
São funções com retorno como outras funções.
                                        FIRST ORDER FUNCTIONS
São funções com retorno como dados comuns, sejam eles números, textos, etc.
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Giulia')
)
