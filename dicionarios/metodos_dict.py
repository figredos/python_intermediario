pessoa = {
    'nome': 'Giulia',
    'sobrenome': 'Fusaro',
    # 'idade': 900,
}

# print(len(pessoa))    # Retorna o número de chaves do dicionário

# print(list(pessoa.keys()))    # Retorna as chaves do dicionário

# print(list(pessoa.values()))  # Retorna os valores do dicionário

# print(list(pessoa.items()))  # Retorna tanto as chaves como os valores do dicionário

# pessoa.setdefault('idade', 0)   # Faz com que um campo não existente, tenha um valor caso seja chamado
# print(pessoa['idade'])

# print(pessoa.get('nome')) # Obtém uma chave específica, e caso ela não exista, retorna um valor (por padrão 'None')

# nome = pessoa.pop('nome')   # Apaga um item com a chave especificada
# print('nome')
# print(pessoa)

# ultima_chave = pessoa.popitem()   # Apaga o último item do dicionário
# print(ultima_chave)
# print(pessoa)

# Atualiza o dicionário, adicionando, mudando valores.
# pessoa.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# pessoa.update(nome='novo valor', idade=30)

# tupla = ('nome', 'novo valor'), ('idade', 30)
# pessoa.update(tupla)
# print(pessoa)

