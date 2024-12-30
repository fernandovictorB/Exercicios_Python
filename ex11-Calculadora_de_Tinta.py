altura = float(input('Qual a altura da parede ?'))
largura = float(input('Qual largura da parede ?'))

areatotal = altura * largura
latas = areatotal / 2

print('Vai ser necessário {} latas de tinta. '.format(latas))