from collections import deque
bank = deque(["shaoun","Mominul","Pilot"])      # Push the value
print(bank)
bank.popleft()                                 # Pop the value
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
if not bank:
    print("No Person Left")