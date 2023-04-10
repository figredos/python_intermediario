# Introdução às Generator functions
generator = (n for n in range(1000000))


def gerador(n=0):
    yield 1     # pausar
    print('Continuando')
    yield 2     # pausar
    print('Mais uma')
    yield 2     # pausar
    print('A última')
    return 'ACABOU'


gen = gerador()
print(next(gen))
print(next(gen))
print(next(gen))