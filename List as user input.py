# 10 20 30 40 50
'''
n = int(input("Enter a text number : "))
list = n.split()
sum = 0
for num in list:
    sum = sum + int(num)
print("sum")
'''

# word test

numofwords = 0
numofletters = 0
numofdigit = 0

text = input("Enter a text of number : ")

for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numofletters = numofletters +1

    elif x >= '0' and x <= '9':
        numofwords = numofwords +1

    elif x == ' ':
        numofdigit = numofdigit + 1

print("Number of Letters : ",numofletters)
print("Number of words : ",numofwords)
print("Number of Digit : ",numofdigit)

