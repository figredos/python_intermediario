# Manipulação de arquivos

O python possui uma série de ferramentas que possibilita a manipulação de arquivos de uma série de tipos.

## Criando arquivos

Para fazer a leitura de arquivos em python, é usado o gerente de contexto 'with open()'(a diferença entre usar 'with open()' e associar 'open()' a uma variável, é que usando 'with open()', não é necessário usar 'nome_da_variável.close()' para fechar o arquivo) podendo ser usado para arquivos que existem ou não. Dentro da função 'open()', podem ser usados alguns tipos de modos de manipulação.
Estes são:
    -> r leitura

    -> w escrita

    -> x criação

    -> a escreve ao final

    -> b binário

    -> t modo texto

    -> + leitura e escrita

## Métodos úteis

->.write() - escreve no arquivo

->.read() - le o arquivo

->.writelines() - escreve várias linhas

->.readlines() - lê linha

->.readline() - lê várias linhas

->.seek() - muda a posição do cursor

### MÓDULO OS

->os.remove ou os.unlink - apaga o arquivo

->os.rename - renomeia o arquivo

->os.rename - renomeia o arquivo

### MÓDULO JSON

->json.dump - Gera um arquivo json

->json.load - Carrega um arquivo json
