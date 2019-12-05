# Usando como referencia webs:
# Estadística ---> https://relopezbriega.github.io/blog/2015/06/27/probabilidad-y-estadistica-con-python/
# Importar archivos a Python ---> https://unipython.com/importar-datos-con-python/

import numpy as np # importando numpy
from scipy import stats # importando scipy.stats
import pandas as pd # importando pandas

# Asignamos el archivo a la variable (tipo carácter): archivo_medidas
# name,time,BER,class,obsId
#archivo_medidas = 'C:\Users\Ara\Downloads\Q3_QoT.csv'

# Cargamos el fichero como el array: datos
# dato = np.loadtxt(archivo , delimiter=',')
# np.loadtxt(d, dtype={'names': ('gender', 'age', 'weight'),'formats': ('S1', 'i4', 'f4')})
# medidas = np.loadtxt(archivo_medidas, delimiter=',', usecols = (2,4),
#                     dtype={'names': ('gender', 'age', 'weight'),'formats': ('S1', 'i4', 'f4')})

serie_cte = [1.1, 1.2, 1, 1.3, 1.01, 1, 1.2, 1.12, 1.01, 1.23]
serie_step = [1.1, 1.2, 1.01, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5]
serie_incr = [1.1, 1.3, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5, 2.7, 2.9]
serie_picos = [1.01, 1.1, 3, 1.14, 1.05, 5, 1.02, 1.13, 4, 1.07]

# Media aritmética
media = [np.mean(serie_cte), np.mean(serie_step), np.mean(serie_incr), np.mean(serie_picos)]

# Mediana: valor central de todos los datos cuando están ordenados de menor a mayor
mediana =  [np.median(serie_cte), np.median(serie_step), np.median(serie_incr), np.median(serie_picos)]

# Desviación típica: cuantifica la dispersión de los datos alrededor de la media aritmética
desviacion_tipica = [np.std(serie_cte), np.std(serie_step), np.std(serie_incr), np.std(serie_picos)]

# Varianza: media aritmética del cuadrado de las desviaciones respecto a la media. Intenta describir la dispersión de los datos
varianza = [np.var(serie_cte), np.var(serie_step), np.var(serie_incr), np.var(serie_picos)]

# Moda: valor con mayor frecuencia absoluta. Quizás más adecuado para valores discretos
moda =  [stats.mode(serie_cte), stats.mode(serie_step), stats.mode(serie_incr), stats.mode(serie_picos)]

print()
print("Media:             ", media)
print("Mediana:           ", mediana)
print("Desviación típica: ", desviacion_tipica)
print("Varianza:          ", varianza)
print("Moda:              ", moda)

dicc_series={}
dicc_series[1]=serie_cte
dicc_series[2]=serie_step
dicc_series[3]=serie_incr
dicc_series[4]=serie_picos

media = [0]*len(dicc_series)
mediana = [0]*len(dicc_series)
desviacion_tipica = [0]*len(dicc_series)
varianza = [0]*len(dicc_series)
moda =  [0]*len(dicc_series)

for i in range(len(dicc_series)):
    media[i] = np.mean(dicc_series[i+1])
    mediana[i] = np.median(dicc_series[i+1])
    desviacion_tipica[i] = np.std(dicc_series[i+1])
    varianza[i] = np.var(dicc_series[i+1])
    moda[i] = stats.mode(dicc_series[i+1])

print()
print("Media:             ", media)
print("Mediana:           ", mediana)
print("Desviación típica: ", desviacion_tipica)
print("Varianza:          ", varianza)
print("Moda:              ", moda)

