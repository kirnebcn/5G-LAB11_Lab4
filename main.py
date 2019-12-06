from queryDB import queryDB
from pathClassifier import pathClassifier
#from writeDB import writeDB
# Initialization params

influxParams={}
influxParams['host']='localhost'
influxParams['port']=8086
influxParams['user']='root'
influxParams['password']=''
influxParams['dbname_monitoring']='MON_DATA'
influxParams['dbname_visualization']='VIS_DATA'

'''
queryParams={}
queryParams['query'] = 'SELECT * FROM ber'
queryParams['tag'] = "obsId"
queryParams['values'] =[str(i+1) for i in range(100)]
queryParams['variable'] = "BER"

print("Retrieving Monitoring Data...")
BER_data,DB_JSON=queryDB(influxParams,queryParams)

print("Classifying Paths...")
new_class=pathClassifier(BER_data)

print(new_class)

print("Writing Visualization DB...")
writeDB(influxParams, DB_JSON, new_class)
'''

print("Llegint dades de monitorització...")
BER_data=queryDB(influxParams)

print()
print("Classificant mesures...")
new_class=pathClassifier(BER_data)

print(new_class);

for i in range (1, len(new_class)+1):
    print(i,new_class[i])

print(list(new_class.items()))

