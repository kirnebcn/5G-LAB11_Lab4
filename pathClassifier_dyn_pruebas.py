import numpy as np  # importando numpy

def pathClassifier_dyn(medidas_BER):
    mida = len(medidas_BER)  # en principio vale 100 (100 obsId)

    # Valores de los parámetros "estándar" de BER
    sumdif_thr = 6e-6   # Umbral de la suma de diferencias (sumatorio de valores de la serie diferenciada)
    hpic = 2e-4         # Altura mínima del pico para ser considerado como tal
    hn = 5e-5           # Amplitud máxima de los valores "normales" de BER

    # Clasificación de las medidas
    clase1 = '1'  # medidas normales de BER
    clase2 = '2'  # incidencia: escalón
    clase3 = '3'  # incidencia: picos de BER
    clase4 = '4'  # incidencia: BER incremental

    # Diccionario de salida con la nueva clasificación de las medidas
    dicc_clases = {a: [] for a in range(1, mida + 1)}

    # Creamos arrays (listas) vacíos de long n+1, porque el 0 lo dejaremos vacío (obsId comienza en 1 y acaba en 100)
    # De hecho, para el diccionario medidas_BER los índices van de 1 a 100
    media = [0] * (mida + 1)
    mediana = [0] * (mida + 1)
    minimo = [0] * (mida + 1)
    maximo = [0] * (mida + 1)
    media_dif = [0] * (mida + 1)
    mediana_dif = [0] * (mida + 1)
    minimo_dif = [0] * (mida + 1)
    maximo_dif = [0] * (mida + 1)

    # Calculamos la serie diferenciada y el sumatorio de las diferencias entre los valores de la serie
    suma_dif = [0] * (mida + 1)
    medidas_dif = dicc_clases.copy()

    for i in range(1, mida + 1):
        for j in range(1, len(list(medidas_BER[i]))):
            medidas_dif[i].append(medidas_BER[i][j] - medidas_BER[i][j - 1])
        suma_dif[i] = sum(medidas_dif[i])

    # Calculamos valores estadísticos de las series temporales
    for i in range(1, mida + 1):
        # Media aritmética
        media[i] = np.mean(medidas_BER[i])
        media_dif[i] = np.mean(medidas_dif[i])
        # Mediana: valor central de todos los datos cuando están ordenados de menor a mayor
        mediana[i] = np.median(medidas_BER[i])
        mediana_dif[i] = np.median(medidas_dif[i])
        minimo[i] = np.amin(medidas_BER[i])
        minimo_dif[i] = np.amin(medidas_dif[i])
        maximo[i] = np.amax(medidas_BER[i])
        maximo_dif[i] = np.amax(medidas_dif[i])

    series = [1, 23, 57, 61, 67, 73, 76, 89, 100]

    for serie in series:
        print("\nSerie:", serie)
        print("Medidas BER["+str(serie)+"]:",medidas_BER[serie])
        print("Medidas dif[" + str(serie) + "]:", medidas_dif[serie])
        print("Media:", media[serie])
        print("Media dif:", media_dif[serie])
        print("Mediana:", mediana[serie])
        print("Mediana dif:", mediana_dif[serie])
        print("Mínimo:", minimo[serie])
        print("Mínimo dif:", minimo_dif[serie])
        print("Máximo:", maximo[serie])
        print("Máximo dif:", maximo_dif[serie])

    # Clasificador
    for i in range(1, mida + 1):
        if (suma_dif[i] > sumdif_thr):  # Escalón o incremental
            if (media[i] < mediana[i]):
                dicc_clases[i] = clase2  # Escalón
            else:
                dicc_clases[i] = clase4  # Incremental
        elif (maximo[i] > hpic) or ( (maximo[i] - minimo[i]) > hn):  # Picos o normal
            dicc_clases[i] = clase3  # Picos
        else:
            dicc_clases[i] = clase1  # Normal

    return dicc_clases