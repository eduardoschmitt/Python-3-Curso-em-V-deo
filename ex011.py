l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
ar = l * a
print('Sua parede tem {:.3f} m²'.format(ar))
print('Para pintar toda a área você precisa de {:.4f} L de tinta'.format(ar/2))