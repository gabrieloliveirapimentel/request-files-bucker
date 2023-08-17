from datetime import datetime
import pytz

file_name = "arquivo.txt"
  
with open(file_name, "w") as file:
  timeZone = pytz.timezone('America/Sao_Paulo')
  timeNow = datetime.now(timeZone)
  current_time =  timeNow.strftime('%d/%m/%Y %H:%M:%S')
    
  file.write("Horario atual: " + current_time)

print("Arquivo criado com sucesso")
