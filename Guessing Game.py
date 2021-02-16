from random import randint

for x in range(1,6):
    guessnumber = int(input("Enter the guessing number 1 to 5 : "))
    randomnumber  = randint(1,5)

    if guessnumber == randomnumber:
        print("You have Won")
    else:
        print("You have loss")
        print("Random number was : ",randomnumber)