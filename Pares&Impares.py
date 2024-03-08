x = 4  # Asigna el valor 4 a la variable number

def ParImpar(y):  # Cambia el nombre del parámetro a "num" para evitar conflictos
    if y % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    return result

print("El valor es", ParImpar(x))  # Imprime el resultado