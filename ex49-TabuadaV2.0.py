tabuada = int(input('Qual tabuada deseja:'))
resultado = 0
for n in range (1, 11):
    resultado = tabuada * n
    print('{}x{}= {}'.format(tabuada, n, resultado))