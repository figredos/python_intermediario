# Criando arquivos em python

# Criando o arquivo sem usar with
arquivo = open('sem_with.txt', 'w', encoding='windows-1252')
arquivo.write('Olá, mundo!')    # Escrevendo no arquivo a frase 'Olá, Mundo!'
arquivo.close()     # Fechando o arquivo manualmente

# Criando arquivo com with
with open('com_with.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!')