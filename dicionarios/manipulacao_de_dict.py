pessoa = {}

chave = 'nome'

# Declarar uma chave dinamicamente, é uma prática inteligente, pois caso o nome da variável seja
# mudado, o nome da chave muda junto

pessoa[chave] = 'Matheus'  # Criando uma chave dinamicamente

pessoa['sobrenome'] = 'Fellet'  # Criando outra chave

print(pessoa[chave])

pessoa[chave] = 'Giulia'  # Atualizando uma chave

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

# Para checar se uma chave está definida em um dicionário, o invés de usar um bloco try, usar .get(nome-da-chave)
if not pessoa.get('sobrenome'):
    print('A chave buscada não existe!')
else:
    print(pessoa['sobrenome'])
