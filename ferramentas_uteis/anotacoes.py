# Criando uma função com retorno int
def numero() -> int:
    return 42

# Criando uma função que recebe um argumento lista e retorna string
def desempacota_e_junta(argumento: 'list') -> str:
    montante = ''

    return montante.join(argumento)

lista = ['a', 'b', 'c']
print(desempacota_e_junta(lista))
