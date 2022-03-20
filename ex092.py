pessoa = dict()
pessoa["Nome"] = str(input('Digite o nome: '))
pessoa["Idade"] = int(input('Digite seu ano de nascimento: '))
pessoa["Idade"] = 2021 - pessoa["Idade"]
pessoa["CTPS"] = int(input('Digite o tempo com a carteira de trabalho, ou 0 para nenhum: '))
if pessoa["CTPS"] > 0:
    pessoa["Ano de Contratação"] = int(input('Digite o ano de contratação: '))
    pessoa["Salário"] = float(input('Digite o salário: '))
    pessoa["Aposentadoria"] = 35 - (2021 - pessoa["Ano de Contratação"])
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')