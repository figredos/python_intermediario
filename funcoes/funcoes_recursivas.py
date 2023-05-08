# Funções recursivas
# Criando uma função que conta de 0 até 10
def recursiva(inicio=0, fim=10):
    # Caso base
    if inicio >= fim:
        return fim

    # Caso recursivo (contar até chegar ao final)
    inicio += 1
    return recursiva(inicio, fim)
