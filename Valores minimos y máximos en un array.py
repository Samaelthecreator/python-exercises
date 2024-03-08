import numpy as np

arreglo1= np.array([34,-54,-657,-89,2,657,1])
arreglo2 = np.array([21,4,-5,6,89,-23])

def minimum(arr):
    min = np.amin(arr)
    print(f"el valor minimo del array es: {min}")

def maximum(arr):
    max = np.amax(arr)
    print(f"el valor máximo del array es: {max}")
    
minimum(arreglo1)
maximum(arreglo2)

