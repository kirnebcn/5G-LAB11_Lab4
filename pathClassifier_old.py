import numpy as np # importando numpy
from scipy import stats # importando scipy.stats
#import pandas as pd  # importando pandas

def pathClassifier(medidas_BER):

    mida = len(medidas_BER)

    # Creamos arrays (listas) vacíos de long n+1, porque el 0 lo dejaremos vacío (obsId comienza en 1 y acaba en 100)
    # De hecho, para el diccionario medidas_BER los índices van de 1 a 100
    media = [0] * (mida+1)
    mediana = [0] * (mida+1)
    #desviacion_tipica = [0] * (mida+1)
    #varianza = [0] * (mida+1)
    minimo = [0] * (mida+1)
    maximo = [0] * (mida+1)

    clase1 = "1"
    clase2 = "2"
    clase3 = "3"
    clase4 = "4"

    dicc_clases = {a:[] for a in range(1,mida+1)}


    for i in range(1,mida+1):
        # Media aritmética
        media[i] = np.mean(medidas_BER[i])
        # Mediana: valor central de todos los datos cuando están ordenados de menor a mayor
        mediana[i] = np.median(medidas_BER[i])
        # Desviación típica: cuantifica la dispersión de los datos alrededor de la media aritmética
        #desviacion_tipica[i] = np.std(medidas_BER[i])
        # Varianza: media aritmética del cuadrado de las desviaciones respecto a la media. Intenta describir la dispersión de los datos
        #varianza[i] = np.var(medidas_BER[i])
        minimo[i] = np.amin(medidas_BER[i])
        maximo[i] = np.amax(medidas_BER[i])

    print("Media:",media)
    print("Mediana:", mediana)
    #print("Desviación típica:", desviacion_tipica)
    #print("Varianza:", varianza)

    suma_dif = [0] * (mida+1)

    # Calculamos el sumatorio de las diferencias entre los valores de la serie
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

    '''
    lista=[21,33,35,37,68,81,95,97]

    for i in lista:
        print("obsId: ", i)
        print("suma_dif = ", suma_dif[i])
        print("suma_dif > 6e-6? : ", suma_dif[i]>6e-6)
        print("maximo = ", maximo[i])
        print("maximo > 1e-4 ? : ", maximo[i] > 1e-4)
        print("minimo = ", minimo[i])
        print("media = ", media[i])
        print("maximo/minimo = ", maximo[i] / minimo[i])
        print("maximo/minimo > 2 ? :",(maximo[i] / minimo[i]) > 2)
        print("maximo-minimo = ",maximo[i] - minimo[i])
    '''

    return dicc_clases
