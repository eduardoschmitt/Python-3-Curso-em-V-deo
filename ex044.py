preco = float(input('Digite o preço do produto: '))
print('Qual a condição de pagamento?')
print('1 - à vista dinheiro/cheque: 10% de desconto')
print('2 - à vista no cartão: 5% de desconto')
print('3 - em até 2x no cartão: preço normal')
print('4 - 3x ou mais no cartão: 20% de juros')
cond = int(input('Digite o número correspondente: '))
if cond == 1:
    preco = preco - (preco * 0.1)
    print(f'O preço final é de {preco}')
elif cond == 2:
    preco = preco - (preco * 0.05)
    print(f'O preço final é de {preco}')
elif cond == 3:
    print(f'O preço final é de {preco}')
elif cond == 4:
    preco = preco + (preco * 0.2)
    print(f'O preço final é de {preco}')