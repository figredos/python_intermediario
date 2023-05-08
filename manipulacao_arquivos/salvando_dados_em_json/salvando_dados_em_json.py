# Importando o módulo json
import json

# Criando dicionário pessoa (objeto)
pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

# Abrindo o arquivo com context manager
with open('salvando_dados.json', 'w', encoding='UTF-8') as arquivo:
    # Usando o comando json.dump() para transformar um objeto python dict em json
    json.dump(pessoa,
              arquivo,
              ensure_ascii=False,
              indent=2,
              )