cadena = [2,3,4,5,6,76,900]
long=len(cadena)
print(cadena)
print(long)

dicc={"val1":12, "val2":34, "val3":65}
print(dicc)
print(len(dicc))

array_dicc=[{"obsid":1,"ber":0.0001},{"obsid":2,"ber":0.0002},{"obsid":3,"ber":0.0003}]
print(array_dicc)
print(len(array_dicc))
print(array_dicc[1])
print(array_dicc[1]['obsid'])
print(array_dicc[2]['ber'])
print(array_dicc[len(array_dicc)-1]['obsid'])

dicc_arrays={1:[1,2,3,4], 2:[2,3,4,5],3:[3,4,5,6],4:[4,5,6,7],5:[5,6,7,8]}


otro_dicc=dicc.copy()
print (dicc is otro_dicc)
dicc["val1"]=44
print(dicc)
print(otro_dicc)

lista=[]
print(lista)
lista=[0]*10
print(lista)
lista[1]=10
print(lista)
lista.append(1)
print(lista)

my_list = [('a','b',1),('c','d',2),('e','f',3)]
my_answer = sum(z for x,y,z in my_list)
print(my_list)
print(my_answer)

dicc_1 = {a:[] for a in range(1, 101)}	# Diccionari de sortida (100 obsId)
dicc_2 = {a:"" for a in range(1, 101)}	# Diccionari de sortida (100 obsId)
print(dicc_1)
print(dicc_2)