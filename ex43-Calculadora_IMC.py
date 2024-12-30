peso = float(input('Qual seu peso ?'))
altura = float(input('Qual sua altura ?'))

IMC1 = altura * altura
IMC = peso / IMC1

if IMC < 18.5:
    print('Você está abaixo de peso!')
elif IMC >= 18.5 and IMC < 25:
    print('Você está no seu peso ideal!')
elif IMC >= 25 and IMC < 30:
    print('Você está com sobrepeso!')
elif IMC >= 30 and IMC <= 40:
    print('Você está com obesidade')
elif IMC > 40:
    print('Você está com obesidade mórbida!')