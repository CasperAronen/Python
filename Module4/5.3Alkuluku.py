import math
def onAlkunum(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
#user_input
try:
    numCheck = int(input("Anna numero: "))
except ValueError:
    print("lmao dumass")
    exit()

if onAlkunum(numCheck):
    print(numCheck ,"on alkunumero")
else:
    print(numCheck ,"ei ole alkunumero.")