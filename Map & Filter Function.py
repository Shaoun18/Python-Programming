def square(x):                           # Map Function
    return  x*x
num = [1,2,3,4,5,6]
result = list(map(square,num))
print(result)

num = [1,2,3,4,5,6]                       #Filter Function
result = list(filter(lambda x : x%2 == 0,num))
print(result)