# Importando pacotes e funções
from functools import partial


# Função print_iter imprime iteráveis
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# Função que aumenta preços
def aumenta_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


# Criando closure para aumento de 10 por cento
aumenta_10_por_cento = partial(aumenta_porcentagem, 1.1)


# Fazendo o mapeamento da função produtos com list comprehension
# novos_produtos = [
#     {**produto, 'preco': aumenta_10_por_cento(produto['preco'])}
#     for produto in produtos
# ]

# Criando uma função que mapeia dados, aumentando seu preço
def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumenta_10_por_cento(
            produto['preco']
        )
    }


novos_produtos = map(muda_preco_de_produtos, produtos)

print_iter(produtos)
print_iter(novos_produtos)

print(novos_produtos)
