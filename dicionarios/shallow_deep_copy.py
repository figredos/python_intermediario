import copy

dicionario_1 = {
    'chave_1': 1,
    'chave_2': 2,
    'lista_1': [0, 1, 2],
}

dicionario_2 = copy.deepcopy(dicionario_1)

dicionario_2['chave_1'] = 1000
dicionario_2['lista_1'] = 9999

print(dicionario_1)
print(dicionario_2)
