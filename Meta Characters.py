#(1) . Use Meta Characters

import re
pattern = r"colo.r"

if re.match(pattern,"colour"):
    print("1.Matched")


#(2) .. Use Meta Characters

import re
pattern = r"colo..r"

if re.match(pattern,"colourr"):
    print("2.Matched")


#(3) ^ Use Meta Characters

import re
pattern = r"^colo..r$"

if re.match(pattern,"colouar"):
    print("3.Matched")

#(4) *(0 or more) Use Meta Characters

import re
pattern = r"a*"

if re.match(pattern,"aaacolour"):
    print("4.Matched")


#(5) +(1 or more) Use Meta Characters

import re
pattern = r"a+"

if re.match(pattern,"abaaacolour"):
    print("5.Matched")


#(6) + Use Meta Characters

import re
pattern = r"a+b"

if re.match(pattern,"abcolour"):
    print("6.Matched")

#(7) ?(0 or 1) Use Meta Characters

import re
pattern = r"ice(-)?cream"

if re.match(pattern,"ice-cream"):
    print("7.Matched")

#(8) {}(1 up to 3) Use Meta Characters

import re
pattern = r"a{1,3}$"

if re.match(pattern,"aaa"):
    print("8.Matched")