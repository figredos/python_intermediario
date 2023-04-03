set_1 = set()

# Add - adiciona um item ao set
set_1.add('Matheus')
set_1.add(1)

# Update - adiciona itens de forma iterada, ou seja, caso seja adicionado uma string e ela não esteja envolta em
# parênteses, ela será adicionada letra por letra.
set_1.update(('Olá mundo!',1 , 2, 3, 4))

# Clear - esvazia um set
# set_1.clear()

# Discard - elimina um item específico do set.
set_1.discard('Olá mundo!')
set_1.discard('Matheus')

print(set_1)
