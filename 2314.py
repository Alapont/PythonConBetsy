#!/c/Users/pablo/AppData/Local/Programs/Python/Python38/python
import random
num14=0
num24=0
iter=10
def getNum():
    return random.randrange(14,24,9)
for x in range(0, iter):
    x= getNum();
    # print(x, end=", ");
    if (x==14):
        num14 = num14 +1
    else:
        num24 = num24 +1
print("14:{:d}\n24:{:d}".format(num14,num24))

