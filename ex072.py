num = int(input('Digite um número entre 0 e 20: '))
while num > 20 or num < 0:
    num = int(input('Erro 001. Digite um número entre 0 e 20: '))
numtupla = 'zero','um', 'dois', 'três', 'quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
print(numtupla[num])