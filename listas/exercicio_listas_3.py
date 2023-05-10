# Exercício - Lista de tarefas com desfazer e refazer.

# Criando função 'lista_de_tarefas'.
def lista_de_tarefas(tarefas=None, desfazer=None):  # Argumentos por padrão 'None' para serem usados em recursão.
    # Criando tupla com possíveis comandos
    comandos = ('LISTAR', 'DESFAZER', 'REFAZER', 'FINALIZAR')

    # Checando a existência das listas, caso não, criando listas de tarefas e desfazer.
    if not tarefas:
        tarefas = []
    if not desfazer:
        desfazer = []

    # Entrada digitada pelo user.
    entrada = input('Comandos: LISTAR, DESFAZER, REFAZER, FINALIZAR.\nDigite para adicionar à lista de tarefas:\n')

    print('\n')

    # Condicionais para checar a existência da entrada nos comandos e executa-los, ou adicionar item à lista.
    if entrada in comandos:
        if entrada == comandos[0]:
            if tarefas:
                print('Listando: ')
                for item in tarefas:
                    print(item)

            print('Não existem tarefas a serem feitas.')

        if entrada == comandos[1]:
            if tarefas:
                desfazer.append(tarefas.pop())
                print('Desfeito: ')
                print(desfazer[-1])

            print('Não existe nada a desfazer.')

        if entrada == comandos[2]:
            if desfazer:
                tarefas.append(desfazer.pop())
                print('Refeito: ')
                print(tarefas[-1])

            print('Não existe nada a refazer.\n')

        if entrada == comandos[3]:
            return tarefas

    # Adicionando itens à lista.
    else:
        tarefas.append(entrada)
    print('#'*80, '\n')

    # Fazendo a Recursão.
    return lista_de_tarefas(tarefas, desfazer)


if __name__ == '__main__':
    tarefas_todo = lista_de_tarefas()
    print(tarefas_todo)
