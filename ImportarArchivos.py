#Conexion con la API Google Sheets

import gspread #importamos la libreria para conectar google sheets

# vinculamos las credenciales utilizando la ruta del archivo que corresponde a las credenciales de la API
gc = gspread.service_account(filename = "C:/Users/52473/OneDrive/Documentos/Lenguajes de programación/Python Lenguaje/Ejercicios/Spyder/conexionesyproyectos-c04c2fe50ab6.json")

#Abrir el archivo por titulo
Hoja = gc.open("TiemposSelectivo")

#Seleccionar primera hoja

worksheet = Hoja.get_worksheet(0)

worksheet.update('B1','Esta es la prueba en VSC')