from datetime import datetime

data_atual = datetime.today()
print(data_atual)

data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
print(data_em_texto)

data_formatada = data_atual.strftime('%d/%m/%Y')
print(data_formatada)

data_e_hora_atuais = data_atual.strftime('%d/%m/%Y %H:%Mh')
print(data_e_hora_atuais)

data_e_hora_em_texto = '26/02/2022 10:34';
data_e_hora_em_texto_formatada = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M')
print(data_e_hora_em_texto_formatada)
