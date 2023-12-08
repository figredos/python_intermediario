# Docstrings

## O que é

Docstrings é uma forma de documentar códigos em python. Usando 3 aspas duplas, é possível criar textos descritivos para códigos inteiros, sejam eles destinados apenas à arquivos por completo, ou até mesmo para objetos dentro do arquivo, como funções e classes.

## COMO ACESSAR

Existem algumas formas de acessar os dados de documentação de arquivos. Um deles é a função 'dir()', que mostra os atributos de um objeto e os atributos que podem ser acessador a partir desse objeto, de forma alfabetizada. O outro é com a função 'help()'. A função 'help()', quando chamada, retorna uma descrição completa do arquivo no qual é chamada, contendo o nome do arquivo, a descrição, conforme criada pelo dev, as funções e as variáveis que um arquivo possui, e finalmente o caminho do arquivo.

## Tipos de documentações

Existem diversos tipos de documentação. Essas são definidas por uma série de convenções onde o tipo de formatação se difere de forma ou outra. Algumas coisas que as documentações têm em comum, como por exemplo, o limite de 80 caracteres de cada linha em python. A documentação do início do documento é bem similar, com a primeira linha sendo o nome do arquivo, e em baixo, a descrição do que o arquivo contém e o que pode ser feito com os conteúdos dele.

Para a documentação de objetos em python, podem ser usados uma série de documentações, algumas muito mais complexas que outras. Uma das mais usadas, é type annotations, que descrevem a função, fornecem o nome e tipo dos parâmetros,e o nome e o tipo do retorno. Essas anotações são inseridas junto à definição ou criação de um objeto, são também uma forma mais técnica de descrever objetos. Além disso, dentro da função é possível, da mesma forma que se faz no início dos arquivos, criar uma descrição do objeto, descrevendo tudo citado acima, como a seguir:

~~~python
def soma(x: int | float, y: int | float) -> int | float:    # Aqui, podemos ver type annotations
    """
    Soma x e y      # Breve descrição da função

    :param x: Número 1
    :type x:  int or float
    :param y: Número 1
    :type y:  int or float

    :return: A soma entre x e y
    :rtype: int or float
    """

    return x + y
~~~

Fazer esse tipo de descrição não é uma obrigatoriedade, é possível usar apenas uma dessas descrições dos argumentos, contudo é útil ter a descrição das funções do programa.
