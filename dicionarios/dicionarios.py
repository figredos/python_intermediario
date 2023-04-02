pessoa = {
    'nome': 'Giulia',
    'sobrenome': 'Fusaro',
    'idade': 20,
    'altura (cm)': 161,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra tal', 'numero': 321}
    ],
}

# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])
