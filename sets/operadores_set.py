set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}

# União - |
uniao_1 = set_1 | set_2
# ou
uniao_2 = set_1.union(set_2)

# Intersecção - &
interseccao_1 = set_1 & set_2
# ou
interseccao_2 = set_1.intersection(set_2)

# Diferença - -
diferenca_1 = set_1 - set_2
# ou
diferenca_2 = set_1.difference(set_2)

# Diferença simétrica - ^
diferenca_1 = set_1 ^ set_2
# ou
diferenca_2 = set_1.symmetric_difference(set_2)