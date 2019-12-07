# QueryDB accede a la BD MON_DATA y genera como salida el diccionario donde cada elemento tiene
# clave obsId y valor ber

from influxdb import InfluxDBClient
import numpy as np

def queryDB(influxParams,queryParams):

    # 1) Get input data
    host = influxParams['host']
    port = influxParams['port']
    user = influxParams['user']
    password = influxParams['password']
    dbname = influxParams['dbname_monitoring']

    query = queryParams['query']
    tag = queryParams['tag']
    values = queryParams['values']
    variable = queryParams['variable']

    # 2) Get BER monitoring data in the desired format for facilitating analysis
    cliente = InfluxDBClient(host, port, user, password, dbname)    # Instancia el objeto InfluxDBClient

    # Obtiene todos los datos de la BD, en la forma de un objeto ResultSet de InfluxDB
    resultado = cliente.query(query)     # objeto ResultSet de InfluxDB, no es un array de diccionarios

    medidas = list(resultado.get_points())  # obtenemos una lista de todos los resultados (lista de diccionarios)
                                            # mediante el método get_points() del objeto ResultSet de InfluxDB

    # Recorremos obsid y montamos el diccionario de salida en formato
    # {1: [7.24313637610657e-05, ...], 2: [7.03297965520217e-05, ...], ..., 100: [7.24313637610657e-05, ...]}
    dicc_salida = {}

    for obsId in values:
        B = list(resultado.get_points(tags={tag: str(obsId)}))
        S = [b[variable] for b in B]
        dicc_salida[obsId] = S

    # 3) Generate monitoring database in JSON file format to facilitate creating visualization data
    rs = cliente.query(query)
    J = rs.raw
    aux = J['series']
    DB_JSON = []
    for serie in aux:
        measurement = serie['name']
        fields = np.array(serie['columns'])
        values = serie['values']
        timePos = int(np.where(fields == 'time')[0])
        classPos = int(np.where(fields == 'class')[0])
        idPos = int(np.where(fields == 'obsId')[0])
        BERpos = int(np.where(fields == 'BER')[0])
        for value in values:
            point = {}
            point["measurement"] = measurement
            point["tags"] = {}
            point["tags"]["class"] = value[classPos]
            point["tags"]["obsId"] = value[idPos]
            point["time"] = value[timePos]
            point["fields"] = {}
            point["fields"]["BER"] = value[BERpos]
            DB_JSON.append(point)

    return (dicc_salida, DB_JSON)
