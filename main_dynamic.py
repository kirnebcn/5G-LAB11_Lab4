# Versión para entorno dinámico

from queryDB import queryDB
from pathClassifier_dyn import pathClassifier_dyn
from writeDB import writeDB
from datetime import date
from datetime import time
from datetime import datetime

# Initialization params

influxParams={}
influxParams['host']='localhost'
influxParams['port']=8086
influxParams['user']='root'
influxParams['password']=''
influxParams['dbname_monitoring']='MON_DATA'
influxParams['dbname_visualization']='VIS_DATA'

initial_date = datetime(2019,8,1)
print("\nLa data inicial de les mesures és 01/08/2019. ")

while True:
    data_teclat = input('\nEntreu la data final de les mesures en format dd/mm/aaaa : ')
    try:
        final_date = datetime.strptime(data_teclat, '%d/%m/%Y')
    except ValueError:
        print("No ha introduït una data correcta...")
    else:
        break

print()
# Reemplazamos la hora por la adecuada según el día
initial_date = initial_date.replace(hour=0,minute=0, second=0)
final_date = final_date.replace(hour=23,minute=59, second=59)

# Pasamos a formato epoch (linux time) y quitamos los milisegundos (decimales) pasando de float a int
initial_date_epoch = int(datetime.timestamp(initial_date))
final_date_epoch = int(datetime.timestamp(final_date))

queryParams={}
# Variamos la query para tener en cuenta el intervalo temporal. 's' es para especificar epoch en segundos
queryParams['query'] = 'SELECT * FROM ber WHERE time >= '+str(initial_date_epoch)\
                       +'s AND time <= '+str(final_date_epoch)+'s'
queryParams['tag'] = "obsId"
queryParams['values'] = [(i+1) for i in range(100)]      # Cambio str(i+1) por (i+1) por coherencia con clasificador
queryParams['variable'] = "BER"

print("Query: ",queryParams['query'])

print("\nLlegint dades de monitorització del",initial_date,"al",final_date,"...")
BER_data,DB_JSON=queryDB(influxParams,queryParams)

print("Classificant mesures...")
new_class=pathClassifier_dyn(BER_data)

print("Desant BD de visualització...")
writeDB(influxParams, DB_JSON, new_class)

print("Procés finalitzat correctament. Veure classificació a Grafana.")