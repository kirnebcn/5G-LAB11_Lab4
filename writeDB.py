from influxdb import InfluxDBClient

def writeDB(influxParams, DB_JSON, new_class):
    # 1) Get input data
    host = influxParams['host']
    port = influxParams['port']
    user = influxParams['user']
    password = influxParams['password']
    dbname = influxParams['dbname_visualization']

    # 2) Create empty visualization database
    client = InfluxDBClient(host, port, user, password, dbname)
    client.drop_database(dbname)
    client.create_database(dbname)

    # 3) Update DB_JSON with the classes in new_class
    for i in range(len(DB_JSON)):
        DB_JSON[i]["tags"]["class"] = new_class[int(DB_JSON[i]["tags"]["obsId"])]
    # 4) Write visualization database
    client.write_points(DB_JSON)
