import numpy as np # importando numpy

def pathClassifier(medidas_BER):

    mida = len(medidas_BER)     # en principio vale 100 (100 obsId)

    '''
    # Pasa la clave obsId (ahora str) a un número entero
    for i in range(len(medidas_BER)):
        medidas_BER[i] = int(medidas_BER[i])
    '''

    # Creamos arrays (listas) vacíos de long n+1, porque el 0 lo dejaremos vacío (obsId comienza en 1 y acaba en 100)
    # De hecho, para el diccionario medidas_BER los índices van de 1 a 100
    media = [0]*(mida+1)
    mediana = [0]*(mida+1)
    minimo = [0]*(mida+1)
    maximo = [0]*(mida+1)

    clase1 = '1'    # medidas normales de BER
    clase2 = '2'    # incidencia: escalón
    clase3 = '3'    # incidencia: picos de BER
    clase4 = '4'    # incidencia: BER incremental

    dicc_clases = {a:[] for a in range(1,mida+1)}

    for i in range(1,mida+1):
        # Media aritmética
        media[i] = np.mean(medidas_BER[i])
        # Mediana: valor central de todos los datos cuando están ordenados de menor a mayor
        mediana[i] = np.median(medidas_BER[i])
        minimo[i] = np.amin(medidas_BER[i])
        maximo[i] = np.amax(medidas_BER[i])
    
    # Calculamos el sumatorio de las diferencias entre los valores de la serie
    suma_dif = [0]*(mida+1)

    for i in range(1,mida+1):
        for j in range (1,len(list(medidas_BER[i]))):
            suma_dif[i]+= (medidas_BER[i][j] - medidas_BER[i][j-1])

    # Clasificador
    for i in range(1,mida+1):
        if (suma_dif[i] > 6e-6):
            if (media[i] < mediana[i]):
                dicc_clases[i] = clase2                         # Escalón
            else:
                dicc_clases[i] = clase4                         # Incremental
        elif (maximo[i] > 2e-4) or (maximo[i]-minimo[i] > 5e-5):
            dicc_clases[i] = clase3                             # Picos
        else:
            dicc_clases[i] = clase1                             # Normal

    return dicc_clases