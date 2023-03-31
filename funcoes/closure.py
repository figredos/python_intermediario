def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'

    return saudar


if __name__ == '__main__':
    falar_boa_tarde = criar_saudacao('Boa tarde')
    falar_boa_semana = criar_saudacao('Boa semana')

    lista_de_nomes = ['João', 'Maria', 'David', 'Sara', 'Miguel', 'Emília', 'Daniel', 'Olivia', 'Guilherme', 'Ana']

    for nome in lista_de_nomes:
        print(falar_boa_tarde(nome))
        print(falar_boa_semana(nome))
