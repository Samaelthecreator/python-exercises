
array = [1,2,3,4,5]

def square_sum(numbers):
    res = 0
    for i in range(0,len(numbers),1):
        res += numbers[i]**2
    print(res)

square_sum(array)

#Otros ejemplos de resolución del mismo problema:

# 1.-
# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)
# 2.-
# def square_sum(numbers):
#     return sum(map(lambda x: x**2,numbers))
