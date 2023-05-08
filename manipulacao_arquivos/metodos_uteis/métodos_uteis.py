# Abrindo o arquivo usando context manager no modo w (write, escrita)
with open('métodos_uteis.txt', 'w', encoding='windows-1252') as arquivo:
    # Escrevendo no arquivo
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

# Abrindo o arquivo usando context manager no modo r (read, leitura)
with open('métodos_uteis.txt', 'r') as arquivo:
    # Lendo os dados do arquivo
    print('#'* 10)
    print('Primeira leitura: ')
    print(arquivo.read())

# Abrindo o arquivo usando context manager no modo w+ (write +, escrita e leitura)
with open('métodos_uteis.txt', 'w+', encoding='windows-1252') as arquivo:
    # Escrevendo no arquivo
    arquivo.write('Linha 3\n')  # Esses comandos acabam por sobrescrever os acima
    arquivo.write('Linha 4\n')

    # Escrevendo múltiplas linhas em um arquivo
    arquivo.writelines(('Linha 5\n', 'Linha 6\n'))

    # Reajustando a posição do cursor
    arquivo.seek(0, 0)

    # Lendo o arquivo
    print('#' * 10)
    print('Segunda leitura: ')
    print(arquivo.read())

    # Reajustando a posição do cursor
    arquivo.seek(0, 0)

    # Lendo o apenas uma linha arquivo
    print('#' * 10)
    print('Lendo apenas uma linha: ')
    print(arquivo.readline())