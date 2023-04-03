# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': {'a': '1', 'b': '3', 'c': '4', 'd': '5'},
        'Resposta': 'c',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': {'a': '25', 'b': '55', 'c': '10', 'd': '51'},
        'Resposta': 'a',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': {'a': '4', 'b': '5', 'c': '2', 'd': '1'},
        'Resposta': 'b',
    },
]

certas = 0

for indice in range(3):
    print(perguntas[indice].get('Pergunta'))

    for opcao, valor in perguntas[indice]['Opções'].items():
        print(f'{opcao}) {valor}')

    entrada = input()

    if entrada == perguntas[indice]['Resposta']:
        certas += 1
        print(f'Escolheu opção {entrada}, acertou!\n')
    else:
        print(f'Escolheu opção {entrada}, errou!\n')

if certas == 3:
    print('Parabéns, você gabaritou!')
elif certas == 2:
    print('Parabéns, você QUASE gabaritou')
elif certas == 1:
    print('Tente novamente, você tirou uma nota baixa!')
elif certas == 0:
    print('Tente novamente, você zerou!')
