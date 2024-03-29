# Map, Partial e Generator type

## Recaptulando mapeamento de dados

Mapeamento, como feito em list comprehension, é uma forma de pegar um   dado e transformá-lo em outro. Esse dado é fornecido por um iterável, e uma vez feito o mapeamento, é retornado outro iterável com o dado transformado.

## Partial

Partial é uma função disponibilizada pelo pacote "functools". A função "partial" tem como principal função o a criação automática de uma função closure (como visto em 'python_intermediario\funcoes\closure.py'). Como outras funções que executam closures, "partial" recebe uma função e '*args' e retorna um 'executável' da função desejada.

## Map

É uma função nativa do python que faz o mapeamento de dados de forma similar ao mapeamento em list comprehension. O mapeamento de dados com a função 'map', funciona a partir do recebimento de uma função e dos dados nos quais aquela função deve ser aplicada. A principal diferença entre a função 'map' e o mapeamento de dados em list comprehension é a automatização da tarefa, uma vez que a função 'map' é útil para algo que será repetidamente executado, além disso, a função 'map' retorna um iterável ao invés de uma lista (sendo também mais leve, uma vez que, não está sendo criada uma lista na memória).
