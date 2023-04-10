import sys

# Generator expression
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
lista = [n for n in range(100000)]
generator = (n for n in range(100000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))