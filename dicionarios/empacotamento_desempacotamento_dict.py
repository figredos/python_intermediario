pessoa = {
    'nome': 'Matheus',
    'sobrenome': 'Fellet',
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.75,
}

pessoa_completa = {**pessoa, **dados_pessoa}


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(1, 2, nome='Giulia', qualquer_coisa=42)
