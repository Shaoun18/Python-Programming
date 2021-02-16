def add(*numbers):
    sum = 0                            # debugging
    for num in numbers:
        sum = sum + num
    return sum
print(add(10,20))