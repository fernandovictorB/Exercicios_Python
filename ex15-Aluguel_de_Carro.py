dias = int(input('Quantos dias você ficou com o carro?'))
km = float(input('Quantos KM você rodou com o carro?'))
valor = (dias * 60) + (km * 0.15)
print('O valor do aluguel referente a {} dias e {}km fica {}R$'.format(dias, km, valor))