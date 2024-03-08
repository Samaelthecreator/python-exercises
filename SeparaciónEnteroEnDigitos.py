entero=12456
 
 
def digitize(n): 
   digitos = [int(digito) for digito in str(entero)]
   digitos.reverse()
   return digitos

print(digitize(entero))

# otra forma de realizarlo es:
# def digitize(n):
#     return [int(x) for x in str(n)[::-1]]

#     Ó

# def digitize(n):
# return [int(x) for x in reversed(str(n))]


