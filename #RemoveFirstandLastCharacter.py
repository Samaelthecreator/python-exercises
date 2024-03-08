#Remove First and Last Character

string= "yeifyskhifh"

def remove_char(s):
    print(s[0])
    print(s[-1])
    print(s)
    str= s.replace(s[-1],"",1)   #replace(objeto a tomar para remplazar, objeto por el que se remplazará, numero de remplazos)
    str1 = str.replace(s[0],"",1)  
    print(str1)


remove_char(string)
