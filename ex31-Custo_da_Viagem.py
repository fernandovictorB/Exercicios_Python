distancia = float(input('Quantos KM tem até seu destino ?'))

if distancia <= 200:
    valor = distancia * 0.50
    print('A sua passagem vai ficar R${:.2f}'.format(valor))
else:
    valor = distancia * 0.45
    print('Sua passagem vai ficar R${:.2f}'.format(valor))