file = open("file text.txt","r+") #file read code
'''
for line in file:
    print(line)
    '''
text = file.read()  #file read
print(text)
size = len(text)
print(size)
file.close() #file close

file = open("file text.txt","a") #file write code

file.write("\n This is my family")

file.close()