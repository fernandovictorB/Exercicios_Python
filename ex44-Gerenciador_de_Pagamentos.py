print('{:=^40}'.format(' LOJA BASTOS '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] À vista no dinheiro
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opçao = int(input('Qual a opção ?'))

if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('A sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas ?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('Opção inválida de pagamento. Tente novamente.')
print('Sua compra no valor R${:.2f} vai custar R${:.2f} no final'.format(preço, total))