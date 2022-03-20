import datetime

ano = int(input('Digite o ano do seu nascimento: '))
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
year = int(year)
idade = year - ano
if idade < 18:
    print(f'Voce tem {idade} anos e ainda vai se alistar')
elif idade == 18:
    print(f'Voce tem {idade} e esta na hora de se alistar')
elif idade > 18:
    print(f'Voce tem {idade} e ja passou da hora de se alistar')
else:
    print('ERROR 404')