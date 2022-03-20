import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
year = int(year)

maiorIdade = int(0)
menorIdade = int(0)

for c in range(0,7):
    ano = int(input(f'Digite o ano de nascimento da {c + 1}ª pessoa: '))
    if (year - ano) >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1
print(f'Das 7 pessoas, {maiorIdade} são maiores de idade e {menorIdade} são menor de idade')