import pandas as pd
import numpy as np
k = [0,1,3,0,0,0]
Sesion = [0,0,0,0,0,0]

Vmc = int(input("Determineme el valor del volumen del microciclo: "))
for j in range (0,6,1):
   k[j] = int(input(f" determineme el valor del dia {j+1}:"))
    

print(k, Vmc)    

def FactorK(Vmc,k):
    for i in range (0,6,1):
        Sesion[i] = k[i]*Vmc/sum(k)

    return Sesion


print(FactorK(Vmc, k))