situacao = dict()
situacao["nome"] = str(input('Digite o nome do aluno: '))
situacao["media"] = float(input('Digite a media do aluno: '))
if situacao["media"] >= 7:
    situacao['situacao'] = 'APROVADO'
else:
    situacao['situacao'] = 'REPROVADO'
for c, k in situacao.items():
    print(f'{c} é igual a {k}')