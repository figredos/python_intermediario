# Criando uma list comprehension simples
lista_1 = [x for x in range(3)]

# Criando uma list comprehension com dois 'for's
lista_2 = [
    (x, y)
    for x in range(3)
    for y in range(2, 6)
]

print(lista_1)
print(lista_2)