from random import randint
from time import sleep

computador = (randint(0,5)) # Faz o computador escolher um número

print('Tente adivinhar meu número escolhido entre 0 e 5')
meunumero = int(input('Qual seu palpite:')) # Jogador tenta adivinhar
print('Processando...')
sleep(3)

if computador == meunumero:
    print('Prabéns! Você venceu!')
else:
    print('Você perdeu! Meu número era o {}'.format(computador))