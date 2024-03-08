#Convertir una cadena de carácteres en mayusculas o en minusculas

texto = "Hola soy el Samael"

def uppercase(text):
    uppertext = text.upper()

    print(f"el texto es el siguiente: {uppertext}")

    return uppertext    

def lowercase(text):
    lowcase = texto.lower()

    print(f"el texto es el siguiente: {lowcase}")   

    return lowcase

uppercase(texto)
lowercase(texto)

#Una manera mas eficiente sin realizar tanto código es el siguiente

#def uppercase(s): return s.upper()