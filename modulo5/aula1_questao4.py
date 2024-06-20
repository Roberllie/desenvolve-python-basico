import datetime

agora = datetime.datetime.now()

data_formatada = f"Data: {agora.day:02}/{agora.month:02}/{agora.year}"
hora_formatada = f"Hora: {agora.hour:02}:{agora.minute:02}"

print(data_formatada)
print(hora_formatada)
