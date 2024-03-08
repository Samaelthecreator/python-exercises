
arr = [1,34,-3,4,5,23,2345,3546,756,-123,324,-234,-234,234,-2,3,4,6]


n = len(arr)

def maximum(arr):
    max = 0
    for i in range(0,n,1):
        if max < arr[i]:
            max = arr[i]
    #print(f"el valor máximo es: {max}")
    return max   

def minimum(arr):
    min = 0
    for i in range(0,n,1):
       if min > arr[i]:
        min = arr[i]
    #print(f"el valor mínimo es: {min}")
    return min

minimum(arr)
maximum(arr)


