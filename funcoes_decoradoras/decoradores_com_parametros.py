# Criando uma função que decora um decorador
def decorator_decorator(*args, **kwargs):
    def decorator(func):
        def internal(*args, **kwargs):
            print('Interna')
            result = func(*args, **kwargs)
            return result

        return internal

    return decorator


# Decorando a função
@decorator_decorator(1, 2, 3)
def soma(x, y):
    return x + y


print(soma(1, 2))
