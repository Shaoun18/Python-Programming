import re
pattern = r"colour"
if re.search(pattern,"Red is a colour,I love red colour"):   # searching the pattern
    print("Match")
else :
    print("Not Matched")

print (re.match(pattern,"Red is a colour,I love red colour"))          # match the pattern

print(re.findall(pattern,"Red is a colour,I love red colour"))      # findall the pattern

# More Regular Expression

import re
Pattern = r"color"
text = "My favourite color is Black"
match = re.search(Pattern,text)

if match:
    print(match.start())    # searching the pattern
    print(match.end())      # searching the pattern end point
    print(match.span())      # searching the pattern  starting & end point

# search & Replace regular Expression

import re
Pattern = r"colour"
text1 = "My favourite colour is Black.I love White colour as well."
text2 = re.sub(Pattern,"color",text1,count=2)
print(text2)