# Criando uma lista com números de 0 - 24
lista = [i for i in range(26)]

# Criando uma segunda lista com dados filtrados
lista_2 = [i for i in lista if 12 < i < 24]

# Imprimindo as listas
print(f'Lista 1: {lista} ')
print(f'Lista 2: {lista_2} ')

# Vendo a intersecção entre as duas listas
print(f'Intersecção entre lista 1 e 2: {set(lista).intersection(lista_2)}')
