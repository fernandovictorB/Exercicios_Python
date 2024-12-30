salario = float(input('Qual seu salário ?'))

if salario > 1250:
    aumento = salario * (10 / 100)
    novosalario = salario + aumento
    print('O seu novo salário vai ser de R${:.2f}'.format(novosalario))
else:
    aumento = salario * (15 / 100)
    novosalario = salario + aumento
    print('O seu novo salário vai ser de R${:.2f}'.format(novosalario))
