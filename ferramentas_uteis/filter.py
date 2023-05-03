# Iportando a função getsizeof do pacote sys
from sys import getsizeof

# Função print_iter imprime um iterável
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.30},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Filtragem usando list comprehension (selecionando apenas os produtos com preço menor que 30
produtos_baratos = [produto for produto in produtos if produto['preco'] < 30 ]

# Filtragem usando a função filter (selecionando apenas os produtos com preço menor que 30
produtos_baratos_filter = filter(lambda a: a['preco'] < 30, produtos)

print_iter(produtos_baratos)
print_iter(produtos_baratos_filter)

# Imprimindo a alocação de memória para os iteráveis
print('Tamanho do iterável usando list comprehension:',getsizeof(produtos_baratos))
print('Tamanho do iterável usando filter:',getsizeof(produtos_baratos_filter))
