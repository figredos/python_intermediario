# Criando uma lista de listas, contendo o número e seu quadrado.
lista_1 = [[numero, numero**2] for numero in range(21)]

# "Desempacotando" os elementos na lista
lista_2 = [numeros for listinhas in lista_1 for numeros in listinhas]

print(lista_2)