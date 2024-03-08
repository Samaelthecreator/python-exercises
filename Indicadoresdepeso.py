def bmi(weight, height):
    
    bmi = weight/height**2
    
    if bmi <= 18.5:
        print("Underweight")
    elif bmi > 18.5 and bmi <=25.0:
        print("Normal")
    elif bmi > 25 and bmi <=30.0:
        print("Overweight")
    else:
        print("Obese")

bmi(110,1.80)

# otra forma de realizarlo es

# def bmi(weight, height):
#     b = weight / height ** 2
#     return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]