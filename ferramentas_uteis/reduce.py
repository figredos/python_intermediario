# Importando a função reduce da biblioteca functools
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# Fazendo um reduce simples, usando a função lambda, o reduce soma os elementos da lista, começando a partir do 0
total = reduce(lambda x, y: x + y,
               [1, 2, 3, 4, 5],
               0
               )

# Fazendo reduce em cima da lista produtos
total_produtos = reduce(lambda x, y: x + y['preco'],    # Função que realiza a soma dos preços
                        produtos,   # Iterável sobre o qual será aplicada a função
                        0   # Acumulador com valor inicial igual a 0
                        )

print(total_produtos)
