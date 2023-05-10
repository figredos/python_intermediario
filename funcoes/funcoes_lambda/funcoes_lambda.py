lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


lista_1 = sorted(lista, key=lambda item: item['nome'])  # A função lambda ordena os itens em relação ao nome
lista_2 = sorted(lista, key=lambda item: item['sobrenome'])  # A função lambda ordena os itens em relação ao nome

exibir(lista_1)
exibir(lista_2)
