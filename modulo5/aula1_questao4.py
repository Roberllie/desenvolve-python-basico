from datetime import datetime 

data_e_horas_atuais = datetime.now()

data_e_horas_texto = data_e_horas_atuais.strftime('data: %d/%m/%Y\nhora: %H:%M')
                                                  
print(data_e_horas_texto)
