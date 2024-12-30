import datetime

ano_nascimento = int(input('Qual ano você nasceu ?'))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Você é um atleta mirim!')
elif idade > 9 and idade <= 14:
    print('Você é um atleta infantil!')
elif idade > 14 and idade <= 19:
    print('Você é um atleta junior!')
elif idade == 20:
    print('Você é um atleta sênior!')
else:
    print('Você é um atleta master!')

