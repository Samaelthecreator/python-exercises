#Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

def repeat(n,s):
    totalstring = s 
    i=1
    
    while i<n:
        totalstring +=s
        i = i+1

    print(f"la cadena repetida es: {totalstring}")



repeat(43,'a}?,g?I,-84)')

#Otra forma mucho más facil de realizar el código es:

# def repeat_str(repeat, string):
#     return repeat * string