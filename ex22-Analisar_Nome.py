nome = str(input('Digite seu nome:')).strip()
dividido = nome.split()
pnome = len(dividido[0])
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(pnome))