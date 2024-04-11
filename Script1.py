import random


def getCard():
    global y
    y= random.randrange(1,53)
    if(y<=4):
        aceNum = ace()
        if(aceNum == 1):
            return 1
        else:
            return 11
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

def getDealerCard():
    global x
    x= random.randrange(1,53)
    if(x<=4):
        aceNum = dealerAce()
        if(aceNum == 1):
            return 1
        else:
            return 11
    elif(x<=8):
        return 2
    elif(x<=12):
        return 3   
    elif(x<=16):
        return 4
    elif(x<=20):
        return 5
    elif(x<=24):
        return 6
    elif(x<=28):
        return 7
    elif(x<=32):
        return 8
    elif(x<=36):
        return 9
    else:
        return 10
    
def playerCard():
    global total
    global dTotal
    dTotal = 0
    total = 0
    pCard = getCard()
    pCard2 = getCard()
    global dealerHand
    dealer = dealerFirstCard()
    dealerHand.append(dealer)
    print(pCard)
    print(pCard2)
    global hand
    hand = [pCard, pCard2]

    if (pCard + pCard2 == 21):
        return 21
    
    for i in hand:
        total+=i
    
    firstTurn = input("Hit, Double, Split, or Stay? ")
    firstTurn = firstTurn.lower()

    if(firstTurn == "double"):
        total = 0
        pDouble = hit()
        hand.append(pDouble)
        for i in hand:
            total+=i
        firstTurn = "stay"

    #if(firstTurn = "split"):


    while(firstTurn != "stay"):
        
        total = 0

        if(firstTurn == "hit"):
            pCard3 = hit()
            hand.append(pCard3)
            print(pCard3)

        for i in hand:
            total+=i

        index = 0
        for num in hand:
            if(num == 11 and total > 21):
                hand[index] = 1
            index+=1
            total = 0
            for j in hand:
                total+=j
        

        total = 0

        for i in hand:
            total+=i

        print(total)
        if(total>=21):
            firstTurn = "stay" 
        
        else:
            firstTurn = input("Hit or Stay? ")
        
    if(total <= 21):
        dealerCards(dealer)

    return total

def dealerFirstCard():
    dCard = getDealerCard()
    print("d" + str(dCard))
    return dCard
    
def dealerCards(fCard):
    global dTotal
    dealerHand.append(getDealerCard())
    
    
    
    for i in dealerHand:
        dTotal+=i

    print("d" + str(dTotal))
    while(dTotal<17):
        dNewCard = getDealerCard()
        dealerHand.append(dNewCard)
        dIndex = 0
        for num in dealerHand:
            if(num == 11 and total > 21):
                dealerHand[dIndex] = 1
                dTotal =0
                for i in dealerHand:
                    dTotal+=i
            dIndex+=1
            
        dTotal+=dNewCard
        print("d"+str(dTotal))
        
        

def hit():
    return getCard()

def ace():
    if(total >= 11):
        return 1
    else:
        return 11

def dealerAce():
    if(dTotal >= 11):
        return 1
    else:
        return 11




#global numPlayers
#numPlayers = input("How many players? ")

hand = []
dealerHand = []
userTotal = playerCard()
print("User total is " + str(userTotal))
#userTotal2 = playerCard()
#print("User total is " + str(userTotal2))
dealerTotal = 0
for i in dealerHand:
    dealerTotal+=i
print("Dealer total is " + str(dealerTotal))

    
