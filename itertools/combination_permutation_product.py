# Importando as funções da biblioteca itertools
from itertools import product, permutations, combinations

# Criando iteráveis
pessoas = [
    'João', 'Joana', 'Luiz', 'Giulia'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster'],
]

# Fazendo as possíveis combinações em grupos de 2 com os nomes na lista "pessoas"
# print(*list(combinations(pessoas, 2)), sep='\n')

# Fazendo as possíveis permutações em grupos de 2 com os nomes na lista "pessoas"
# print(*list(permutations(pessoas, 2)), sep='\n')

# Fazendo combinações entre os elementos das listas presentes em camisetas
print(*list(product(*camisetas)), sep='\n')