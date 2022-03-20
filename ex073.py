tabela = 'Palmeiras','Atlético MG','Fortaleza','Bragantina','Flamengo','Athletico-PR','Ceará','Santos',\
         'Atlético-GO','Bahia','Corinthians','Fluminense','Juventude','Internacional', 'Sport Recife', 'Cuiaba',\
         'São Paulo', 'America-MG','Grêmio','Chapecoense'
print(f'OS 5 PRIMEIROS COLOCADOS SÃO: {tabela[0:5]}')
print(f'OS ÚLTIMOS 4 COLOCADOS SÃO: {tabela[16:21]}')

print(f'A TABELA EM ORDEM ALFABÉTICA: {sorted(tabela)}')
print(f'A POSIÇÃO DA CHAPE NA TABELA É: {tabela.index("Chapecoense")+1}')