from datetime import date

data_atual = date.today()
print(data_atual)

data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
print(data_em_texto)
