# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(list_1, list_2):
    is_list(list_1, list_2)
    return [(list_1[i], list_2[i]) for i in range(min(len(list_1), len(list_2)))]


def is_list(*args):
    for arg in args:
        if not isinstance(arg, list):
            raise TypeError('Parâmetro deve ser do tipo list.')


lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']
nova_lista = zipper(lista_1, lista_2)

print(nova_lista)
