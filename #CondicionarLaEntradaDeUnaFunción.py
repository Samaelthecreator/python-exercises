#Condicionar la entrada de una función



name = 'Samael'

def saludo(nombre):
    if isinstance(nombre,str):
        return 'Hola, ' + nombre , '¿Como estas?'
    else:
        return "Tipo de dato no válido"

print(saludo(name))