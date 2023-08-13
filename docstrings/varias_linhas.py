"""Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções.
A função soma, é simples e conhecida do suficiente.
"""

# Criando uma variável
variavel_1 = 1


# Definindo a função soma
def soma(x: int | float, y: int | float) -> int | float:  # Aqui, podemos ver type annotations
    """
    Soma x e y      # Breve descrição da função

    A função soma faz a soma de dois dados números.
    """

    return x + y


class Foo:
    """
    Esta é uma classe de exemplo

    Esta classe contém exemplos de documentação de arquivos e classes em python.
    """

    # Definindo o método soma
    def soma(self, x: int | float, y: int | float) -> int | float:  # Aqui, podemos ver type annotations
        """
        Soma x e y      # Breve descrição da função

        A função soma faz a soma de dois dados números.
        """

        return x + y


variavel_2 = 2
variavel_3 = 3
variavel_4 = 4
