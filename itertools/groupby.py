# Importando a função do pacote itertools
from itertools import groupby

# Criando o iterável
letras = ['a', 'b', 'c', 'd', 'd', 'a', 'a', 'c']

# Ordenando a lista
letras.sort()

# Agrupando os elementos da lista
elementos_agrupados = groupby(letras)

# # Imprimindo os elementos da lista de agrupados
# for chave, elemento in elementos_agrupados:
#     print(chave)
#     print(list(elemento))

# Criando um novo iterável
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Giulia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# Ordenando o iterável
alunos_ordenados = sorted(alunos, key=lambda x: x['nota'])

# Criando o agrupamento com o iterável
alunos_ordenados_agrupados = groupby(alunos_ordenados, key=lambda x: x['nota'])

# Imprimindo o agrupamento do iterável
for chave, elemento in alunos_ordenados_agrupados:
    print(chave)
    print(list(elemento))