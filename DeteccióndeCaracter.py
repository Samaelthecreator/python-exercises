nombre = "Roberto"


def are_you_playing_banjo(name):
    res = name+" plays banjo" if name[0].lower =="r"  else name + " does not play banjo"    #El lower convierte todo a minusculas y lo compara, ya que la condición es si es R ó r
    return res 

print(are_you_playing_banjo(nombre))    



# def are_you_playing_banjo(name):
#     if name[0] == "R" or name[0] == "r":
#         print(f"{name} plays bajo")
#     else:
#         print(f"{name} does not play banjo")
#     return name

# are_you_playing_banjo(nombre)