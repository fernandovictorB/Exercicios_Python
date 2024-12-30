from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opçẽs:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual sua jogada ?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0: # Computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('Jogada inválida.')
elif computador == 1: # Computador jogou papel
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    else:
        print('Jogada inválida')
elif computador == 2: # Computador jogou tesoura
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')