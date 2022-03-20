peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Abaixo de 18.5: abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Entre 18.5 e 25: peso ideal')
elif imc >= 25 and imc < 30:
    print('25 até 30: sobrepeso')
elif imc >= 30 and imc < 40:
    print('30 até 40: obesidade')
elif imc >= 40:
    print('Obesidade mórbida')