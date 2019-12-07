from queryDB import queryDB
from pathClassifier import pathClassifier
from writeDB import writeDB
# Initialization params

influxParams={}
influxParams['host']='localhost'
influxParams['port']=8086
influxParams['user']='root'
influxParams['password']=''
influxParams['dbname_monitoring']='MON_DATA'
influxParams['dbname_visualization']='VIS_DATA'

queryParams={}
queryParams['query'] = 'SELECT * FROM ber'
queryParams['tag'] = "obsId"
queryParams['values'] = [(i+1) for i in range(100)]      # Cambio str(i+1) por (i+1) por coherencia con clasificador
queryParams['variable'] = "BER"

print("Llegint dades de monitorització...")
BER_data,DB_JSON=queryDB(influxParams,queryParams)

print("Classificant mesures...")
new_class=pathClassifier(BER_data)

print("Desant BD de visualització...")
writeDB(influxParams, DB_JSON, new_class)

print("Procés finalitzat correctament. Veure classificació a Grafana.")