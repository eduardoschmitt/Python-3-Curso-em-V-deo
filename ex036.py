valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Quantos anos ele deseja pagar? '))

prestacaoMensal = valorCasa / (anos * 12)

print(f'Para pagar uma casa de R$ {valorCasa} em 7 anos a prestação será de'
      f' {prestacaoMensal:.2f}')

if prestacaoMensal < (salario * 0.3):
    print('Empréstimo aprovado')
else:
    print('Empréstimo Negado')