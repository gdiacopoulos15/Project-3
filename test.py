import random

def getCard():
    global y
    y= random.randrange(1,53)
    if(y<=4):
        return 1
    elif(y<=8):
        return 2
    elif(y<=12):
        return 3   
    elif(y<=16):
        return 4
    elif(y<=20):
        return 5
    elif(y<=24):
        return 6
    elif(y<=28):
        return 7
    elif(y<=32):
        return 8
    elif(y<=36):
        return 9
    else:
        return 10
    
print(getCard())
print(getCard())

    
