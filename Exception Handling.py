# first code
'''
try:
    list = [10,20,30,0]
    result = list [0] / list [3]  #this line is exception handling
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Does not divide by zero")
finally:
    print("Succesful")
'''
# second code
'''
try:
    num1 = int(input("Enter the first Number : "))
    num2 = int(input("Enter the second Number :"))
    result = num2 / num1
    print(result)

except(ZeroDivisionError,ValueError):
    print("you have enter the valued number")

finally:
    print("Thanks")
'''
# third code
'''
def vote(age):
    if age <= 18:
        raise ValueError("Invaid Object")
    return "You are allowed to vote"
try:
    print(vote(20))
    print(vote(17))
except ValueError as error:
    print("error")
'''