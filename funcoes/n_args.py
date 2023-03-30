def soma(*args):  # Empacotamento de argumentos
    return sum(args)


soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# soma_numeros = soma(numeros)    # Não funciona, pois, a função não recebe tuplas, e sim números inteiros
soma_numeros = soma(*numeros)  # Usando o carácter '*', fazemos com que a variável seja desempacotada
