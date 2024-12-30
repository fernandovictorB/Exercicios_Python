nome = input('Qual seu nome ?')
print('Muito prazer {}!'.format(nome))

casa = float(input('{}, Qual é o valor da casa que deseja comprar ? R$'.format(nome)))
anos = int(input('Em quanto anos você deseja pagar a casa ?'))
salario = float(input('{}, Qual seu salário ? R$'.format(nome)))

tempo = anos * 12
parcela = salario * 30 / 100
parcelafinal = casa / tempo

if parcelafinal > parcela:
    print('Infelizmente seu financiamento não pode ser aprovado, as parcelas vão utilizar mais de 30% do seu salário.')
else:
    parcelafinal <= parcela
    print('PARABÉNS! Seu financiamento foi aprovado com sucesso!')
    print('O valor de sua parcela vai ficar no valor de R${:.2f}'.format(parcelafinal))
