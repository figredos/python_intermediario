from itertools import zip_longest

# Criando as listas
lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']

# Agregando os elementos de uma lista com a outra
lista_agregada = list(zip(lista_1, lista_2))
lista_agregada_reversa = list(zip_longest(lista_1, lista_2))

print(lista_agregada)
print(lista_agregada_reversa)
