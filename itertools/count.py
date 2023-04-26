# Importando os pacotes
from itertools import count

# Count é um iterador sem fim
count_1 = count(16, 8)
range_1 = range(8, 100, 8)

print('Count')
for i in count_1:
    if i >= 100:
        break

    print(i)

print('Range')
for i in range_1:
    print(i)
