velocidade = float(input('Quantos Km/h você está ?'))

if velocidade > 80:
    print('Você foi multado!')
    multa = velocidade - 80
    valormulta = multa * 7
    print('Você devera pagar uma multa no valor de R${:.2f}'.format(valormulta))
else:
    print('Tudo certo, Boa viagem!')