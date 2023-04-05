# Criando dicionário
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# Fazendo o mapeamento
produtos_1 = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] < 20
    else {**produto}
    for produto in produtos
]

print(*produtos_1, sep='\n')
