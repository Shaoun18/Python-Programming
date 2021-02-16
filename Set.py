num1 = {1,2,3,4,5,5}                   #set data structure
num2 = set([2,3,6,8,7])
num2.add(9)
num2.remove(9)
print(num1)
print(7 in num2)

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)