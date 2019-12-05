import numpy as np # importando numpy
from scipy import stats # importando scipy.stats
#import pandas as pd  # importando pandas

def pathClassifier(medidas_BER):

    for i in range(len(medidas_BER)):
        # Media aritmética
        print('Calculando media...')
        media[i] = np.mean(medidas_BER[i])

        # Mediana: valor central de todos los datos cuando están ordenados de menor a mayor
        print('Calculando mediana...')
        mediana[i] = np.median(medidas_BER[i])

        # Desviación típica: cuantifica la dispersión de los datos alrededor de la media aritmética
        print('Calculando desviación típica...')
        desviacion_tipica[i] = np.std(medidas_BER[i])

        # Varianza: media aritmética del cuadrado de las desviaciones respecto a la media. Intenta describir la dispersión de los datos
        print('Calculando varianza...')
        varianza[i] = np.var(medidas_BER[i])

        # Moda: valor con mayor frecuencia absoluta. Quizás más adecuado para valores discretos
        print('Calculando moda...')
        moda[i] = stats.mode(medidas_BER[i])

        # Valor mínimo
        print('Calculando valor mínimo...')
        minimo[i] = np.amin(medidas_BER[i])

        # Valor máximo
        print('Calculando valor máximo...')
        maximo[i] = np.amax(medidas_BER[i])

        print()
        print("Media:             ", media)
        print("Mediana:           ", mediana)
        print("Desviación típica: ", desviacion_tipica)
        print("Varianza:          ", varianza)
        print("Moda:              ", moda)
        print("Valor mínimo:      ", minimo)
        print("Valor máximo:      ", maximo)

    return(maximo)