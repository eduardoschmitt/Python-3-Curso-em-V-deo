import datetime

dataAtual = datetime.datetime.now()
data = dataAtual.date()
ano = data.strftime("%Y")
ano = int(ano)

anoA = int(input('Digite o ano de nascimento do atleta: '))
idade = ano - anoA
if idade <= 9:
    print('Categoria MIRIM')
elif idade <=14:
    print('Categoria INFANTIL')
elif idade <=19:
    print('Categoria JUNIOR')
elif idade <=20:
    print('Categoria SÊNIOR')
elif idade >= 21:
    print('Categoria MASTER')