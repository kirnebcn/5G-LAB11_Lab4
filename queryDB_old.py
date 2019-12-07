# QueryDB accede a la BD MON_DATA y genera como salida el diccionario donde cada elemento tiene
# clave obsId y valor ber

from influxdb import InfluxDBClient

def queryDB(influxParams):

    # Instancia el objeto InfluxDBClient
    host = influxParams['host']
    port = influxParams['port']
    user = influxParams['user']
    password = influxParams['password']
    dbname = influxParams['dbname_monitoring']

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

    return dicc_salida
