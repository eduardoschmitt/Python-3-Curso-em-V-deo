from datetime import date
ano = int(input('\033[1;92mDigite um ano ou\033[1;94m digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'	\033[0;0m O ano de {ano} é bissexto.')
else:
    print(f'	\033[0;0mO ano de {ano} não é bissexto.')