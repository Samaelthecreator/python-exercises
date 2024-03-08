#Función que convierte una cadena de caracteres con numeros a datos tipo int

string = "1234"

def string_to_number(s): return int(s)
    
print(string_to_number(string), type(string_to_number(string)))


# Otra forma de realizarlo:
# def char_to_digit(s):
#     if s == '0':
#         return 0
#     elif s == '1':
#         return 1
#     elif s == '2':
#         return 2
#     elif s == '3':
#         return 3
#     elif s == '4':
#         return 4
#     elif s == '5':
#         return 5
#     elif s == '6':
#         return 6
#     elif s == '7':
#         return 7
#     elif s == '8':
#         return 8
#     else:
#         return 9
    
    
# def string_to_number(s):
#     if isinstance(s, int):
#         return s
    
#     r = 0
#     for c in s:
#         if c == '-':
#             continue
#         r = r * 10 + char_to_digit(c)
    
#     return r if s[0] != '-' else -1 * r