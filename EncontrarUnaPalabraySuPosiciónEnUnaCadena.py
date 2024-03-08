# Can you find the needle in the haystack?
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle, so

cadena = "Hola a todos hijos de la gran puta"

def find_needle(haystack) : return "La posición de la cadena es: " + str(haystack.split(" ").index("hijos")) #La función split tiene 
                                                                                                             #varios argumentos: 
                                                                                                             # split(separador, máximo numero de separaciones)
int(find_needle(cadena))


Otras formas de hacerlo:

# 1.-
# def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')

# 2.-
# def find_needle(haystack):
# 	return 'found the needle at position {}'.format(haystack.index('needle'))