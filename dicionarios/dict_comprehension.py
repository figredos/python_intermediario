# Criando um dicionário
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# Dictionary Comprehension
produto_novo = {
    chave: valor
    for chave, valor
    in produto.items()
    if chave != 'categoria' # Filtrando itens
}