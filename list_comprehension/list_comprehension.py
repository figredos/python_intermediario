# Criando uma lista
lista_1 = []

# Adicionando coisas à lista de forma tradicional
for numero in range(10):
    lista_1.append(numero)

# Criando uma lista com list comprehension
lista_2 = [numero for numero in range(10)]

# Checando igualdade das listas 1 e 2
if lista_2 == lista_1:
    print('As listas são iguais!')