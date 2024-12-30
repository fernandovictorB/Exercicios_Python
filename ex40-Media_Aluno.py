nota1 = float(input('informe a primeira nota:'))
nota2 = float(input('Informe a segunda nota:'))

media = (nota1 + nota2) / 2
if media < 5.0:
    print('A sua média foi de {:.1f}'.format(media))
    print('Você foi reprovado!')
elif media >= 5.0 and media <= 6.9:
    print('A sua média foi de {:.1f}'.format(media))
    print('Você está de recuperação!')
else:
    print('PARABÉNS! você foi aprovado com uma média {:.1f}'.format(media))

