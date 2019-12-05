# QueryDB accede a la BD MON_DATA y genera como salida el diccionario donde cada elemento tiene
# clave obsId y valor ber

from influxdb import InfluxDBClient
import numpy as np # importando numpy
from scipy import stats # importando scipy.stats

# Instancia el objeto InfluxDBClient
host='localhost'
port=8086
user='root'
password=''
dbname='MON_DATA'

cliente = InfluxDBClient(host, port, user, password, dbname)

# consulta = 'SELECT * FROM ber where "obsId"=\'1\''  ... en caso de querer introducir ' en la query

# Obtiene todos los datos de la BD, en la forma de un objeto ResultSet de InfluxDB
consulta = 'SELECT * FROM ber'

resultado = cliente.query(consulta)     # objeto ResultSet de InfluxDB, no es un array de diccionarios

medidas = list(resultado.get_points())        # obtenemos una lista de todos los resultados (lista de diccionarios)

# obtenemos una lista de todas los posibles valores de obsId (valores repetidos) Tamaño 288000 (288000 medidas)
lista_obsid = [medida["obsId"] for medida in medidas]

# Obtenemos una lista con todos los obsId únicos con ayuda del tipo de datos set
# Un set sólo almacena un valor determinado una única vez aunque se inserte más veces
set_obsid = set(lista_obsid)        # insertamos la lista en el set --> {'96', '12', '83', '17', ..., '34'} Tamaño 100
obsid_unicos = list(set_obsid)      # convierte el set a lista --> ['96', '12', '83', '17', ..., '34'] Tamaño 100

# También se puede hacer con una funcion numpy: unique
# import numpy as np
# lista_obsid_np = np.array(lista_obsid)
# obsid_unicos = np.unique(lista_obsid_np)

# Pasa los elementos de obsId a un número entero
for i in range(len(obsid_unicos)):
    obsid_unicos[i]=int(obsid_unicos[i])

obsid_unicos.sort()  # ordena las obsId de menor a mayor

# Recorremos obsid y montamos el diccionario de salida en formato
# {1: [7.24313637610657e-05, ...], 2: [7.03297965520217e-05, ...], ...,
#  100: [7.24313637610657e-05, ...]}

dicc_salida = {}

for obsId in obsid_unicos:
    B = list(resultado.get_points(tags={"obsId": str(obsId)}))
    S = [b["BER"] for b in B]
    dicc_salida[obsId] = S

medidas_BER = dicc_salida
mida = len(medidas_BER)+1

# Creamos arrays (listas) de longitud n+1, porque el 0 lo dejaremos vacío (obsId comienza en 1 y acaba en 100)
# De hecho, para el diccionario medidas_BER los índices van de 1 a 100
media=[0]*mida
mediana=[0]*mida
desviacion_tipica=[0]*mida
varianza=[0]*mida
moda=[0]*mida
minimo=[0]*mida
maximo=[0]*mida

for i in range(mida-1):
    # Media aritmética
    print('Calculando media...')
    media[i+1] = np.mean(medidas_BER[i+1])

    # Mediana: valor central de todos los datos cuando están ordenados de menor a mayor
    print('Calculando mediana...')
    mediana[i+1] = np.median(medidas_BER[i+1])

    # Desviación típica: cuantifica la dispersión de los datos alrededor de la media aritmética
    print('Calculando desviación típica...')
    desviacion_tipica[i+1] = np.std(medidas_BER[i+1])

    # Varianza: media aritmética del cuadrado de las desviaciones respecto a la media. Intenta describir la dispersión de los datos
    print('Calculando varianza...')
    varianza[i+1] = np.var(medidas_BER[i+1])

    # Valor mínimo
    print('Calculando valor mínimo...')
    minimo[i+1] = np.amin(medidas_BER[i+1])

    # Valor máximo
    print('Calculando valor máximo...')
    maximo[i+1] = np.amax(medidas_BER[i+1])

print()
print("Media:             ", media)
print("Mediana:           ", mediana)
print("Desviación típica: ", desviacion_tipica)
print("Varianza:          ", varianza)
print("Valor mínimo:      ", minimo)
print("Valor máximo:      ", maximo)

print("Normal (1)")
print("Media:             ", media[1])
print("Mediana:           ", mediana[1])
print("Desviación típica: ", desviacion_tipica[1])
print("Varianza:          ", varianza[1])
print("Valor mínimo:      ", minimo[1])
print("Valor máximo:      ", maximo[1])

print("Normal (100)")
print("Media:             ", media[100])
print("Mediana:           ", mediana[100])
print("Desviación típica: ", desviacion_tipica[100])
print("Varianza:          ", varianza[100])
print("Valor mínimo:      ", minimo[100])
print("Valor máximo:      ", maximo[100])

print("Esglaó (67)")
print("Media:             ", media[67])
print("Mediana:           ", mediana[67])
print("Desviación típica: ", desviacion_tipica[67])
print("Varianza:          ", varianza[67])
print("Valor mínimo:      ", minimo[67])
print("Valor máximo:      ", maximo[67])

print("Pics (7)")
print("Media:             ", media[7])
print("Mediana:           ", mediana[7])
print("Desviación típica: ", desviacion_tipica[7])
print("Varianza:          ", varianza[7])
print("Valor mínimo:      ", minimo[7])
print("Valor máximo:      ", maximo[7])

print("Pics (23)")
print("Media:             ", media[23])
print("Mediana:           ", mediana[23])
print("Desviación típica: ", desviacion_tipica[23])
print("Varianza:          ", varianza[23])
print("Valor mínimo:      ", minimo[23])
print("Valor máximo:      ", maximo[23])

print("Pics (61)")
print("Media:             ", media[61])
print("Mediana:           ", mediana[61])
print("Desviación típica: ", desviacion_tipica[61])
print("Varianza:          ", varianza[61])
print("Valor mínimo:      ", minimo[61])
print("Valor máximo:      ", maximo[61])

print("Pics (76)")
print("Media:             ", media[76])
print("Mediana:           ", mediana[76])
print("Desviación típica: ", desviacion_tipica[76])
print("Varianza:          ", varianza[76])
print("Valor mínimo:      ", minimo[76])
print("Valor máximo:      ", maximo[76])

print("Incrementals (57)")
print("Media:             ", media[57])
print("Mediana:           ", mediana[57])
print("Desviación típica: ", desviacion_tipica[57])
print("Varianza:          ", varianza[57])
print("Valor mínimo:      ", minimo[57])
print("Valor máximo:      ", maximo[57])

print("Incrementals (73)")
print("Media:             ", media[73])
print("Mediana:           ", mediana[73])
print("Desviación típica: ", desviacion_tipica[73])
print("Varianza:          ", varianza[73])
print("Valor mínimo:      ", minimo[73])
print("Valor máximo:      ", maximo[73])

print("Incrementals (89)")
print("Media:             ", media[89])
print("Mediana:           ", mediana[89])
print("Desviación típica: ", desviacion_tipica[89])
print("Varianza:          ", varianza[89])
print("Valor mínimo:      ", minimo[89])
print("Valor máximo:      ", maximo[89])
