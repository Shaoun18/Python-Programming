# Xargs
def student(*deatils):                   # tuples using
    print(deatils)

student(56,"Shaoun")

# XargS
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
add(10,20)
add(40,60)

# XXargs
def student(**details):                   # tuples using
    print(details)

student(Id = 56,Name = "Shaoun")
