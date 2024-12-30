import datetime

data_nascimento = int(input('Qual ano você nasceu ?'))
ano_atual = datetime.datetime.now().year
data_alistamento = ano_atual - data_nascimento

if data_alistamento == 18:
    print('Você deve se alistar esse ano!')
elif data_alistamento < 18:
    tempo_alistamento = 18 - data_alistamento
    print('Você ainda não tem idade para se alistar!')
    print('Faltam {} ano(s) para o seu alistamento.'.format(tempo_alistamento))
elif data_alistamento > 18:
    atraso = (ano_atual - data_nascimento) - 18
    ano_alistamento = ano_atual - atraso
    print('Você deveria ter se alistado em {}, há {} ano(s) atrás!'.format(ano_alistamento, atraso))
