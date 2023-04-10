# Criando uma string
nome = 'Giulia'

# A função dir, lista todos os métodos de um determinado tipo de dado.
# for i in dir(nome):
     # print(i)

# A função hasattr, checa se uma determinada variável possui um determinado método.
print(hasattr(nome, 'upper'))
print(hasattr(nome, 'mor'))

# A função getattr possibilita o uso de um método como função.
# A função getattr possibilita também o recebimento de um método dinâmicamente.
mor = 'upper'

print(getattr(nome, mor)())
