from datetime import date
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0
for pessoa in range (1, 8):
    nascimento = int(input('Em que ano a {}° nasceu ?'.format(pessoa)))
    idade = ano_atual - nascimento
    if idade >= 21:
        maior_idade += 1
    else:
        menor_idade += 1

print('Ao todo tivemos {} pessoas maior de idade'.format(maior_idade))
print('E também {} pessoas menor de idade'.format(menor_idade))