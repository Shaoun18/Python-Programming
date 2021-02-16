#2+4+6+.......+n

n = int(input("Enter the last number :"))
i = 2
sum = 0
while i <= n:
    sum = sum +i
    i = i+2
print(sum)