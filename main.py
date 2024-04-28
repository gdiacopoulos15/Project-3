
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QLabel, QLineEdit
from PyQt5.QtGui import QColor, QPainter, QIntValidator
from card import Card

class Blackjack(object):
    def main(self):
        #applivation and widgets
        app = QApplication(sys.argv)
        self.window = QWidget()
        
        #entering total money widget set up
        self.startWindow = QWidget()
        startLayout = QGridLayout()
        self.betInput = QLineEdit()
        betLabel = QLabel(self.startWindow)

        #bet per round widget set up
        self.betWindow = QWidget()
        self.betLayout = QGridLayout()
        self.inputPerRound = QLineEdit()
        self.betPerRoundLabelBettingWindow = QLabel(self.betWindow)

        #creating win window
        self.winWindow = QWidget()
        self.winLayout = QGridLayout()
        self.winLabel = QLabel(self.winWindow)

        #creating label for scores
        self.scoreLabel = QLabel(self.window)
        self.dealerScoreLabel = QLabel(self.window)

        #bet amount
        self.totalMoney = 0
        self.betMoney = 0

        #creating arrays for totals
        self.arrayPlayer = []
        self.arrayDealer = []
        self.arrayS1 = []
        self.arrayS2 = []
        
        #buttons on main screen
        self.layout = QGridLayout()

        self.score1 = QLabel(self.window)
        self.score2 = QLabel(self.window)
        self.scoreLabel2 = QLabel(self.window)
        
        #calling newGame to show first game
        self.newGame()

        
        #adding dealer score label
        label2 = QLabel(self.window)
        label2.setText("Dealer \nScore: ")
        label2.adjustSize()
        label2.move(900,200)
        self.dealerScoreLabel = QLabel(self.window)
        self.betWindow.setVisible(False)
       
        #better input widget
        startLayout.addWidget(self.betInput,1,0,1,1)
        betLabel.setText("Enter money to start with.")
        betLabel.adjustSize()
        betLabel.move(25,25)
        betButton = QPushButton("START")
        startLayout.addWidget(betButton, 2,0,1,1)
        betButton.clicked.connect(self.bet)

        #setting main window visible
        self.startWindow.setFixedSize(800,600)
        self.startWindow.setLayout(startLayout)
        self.startWindow.setVisible(True)

        
        #if __name__ == "__main__":

        sys.exit(app.exec_())
        #QWidget()
        #gridlayout


    def hit(self):
        #disabiling buttons
        self.doubleButton.setEnabled(False)
        self.splitButton.setEnabled(False)

        #getting another card
        additionalCard = Card()
        self.layout.addWidget(additionalCard,5,self.length,1,2)
        self.length +=2
        
        #checking for ace
        if(additionalCard.value == 11 and self.playerTot >= 11):
            additionalCard.value = 1

        #getting new total and adding card to array
        self.arrayPlayer.append(additionalCard.value)
        self.playerTot += additionalCard.value

        #checking if an ace is already in the hand
        index = 0
        for i in self.arrayPlayer:
            if(self.playerTot > 21 and i == 11):
                self.arrayPlayer[index] = 1
                self.playerTot = self.playerTot - 10
            index += 1


        #adding score label
        self.scoreLabel.setText(str(self.playerTot))
        self.scoreLabel.move(1025,800)
        
        #disabiling button if total is 21 or higher
        if(self.playerTot > 21):
            self.hitButton.setEnabled(False)
            self.stayButton.setEnabled(False)
            self.lost()

    def stay(self):
        #disabiling buttons
        self.hitButton.setEnabled(False)
        self.doubleButton.setEnabled(False)
        self.splitButton.setEnabled(False)
        
        
        #getting a dealer a card
        newDealerCard = Card()
        self.layout.addWidget(newDealerCard, 0, self.dealerLength,1,2)
        self.dealerLength+=2

        #checking for ace
        if(newDealerCard.value == 11 and self.dealerTot == 11):
            newDealerCard.value = 1
            
        #adding to total and adding to array
        self.dealerTot += newDealerCard.value
        self.arrayDealer.append(newDealerCard.value)

        #setting dealer score label
        self.dealerScoreLabel.setText(str(self.dealerTot))
        self.dealerScoreLabel.move(1025,200)

        #having dealer get new card if their total is less than 17
        while(self.dealerTot < 17):
            moreCard = Card()
            self.layout.addWidget(moreCard, 0, self.dealerLength,1,2)
            self.dealerLength+=2
            if(moreCard.value == 11 and self.dealerTot >= 11):
                moreCard.value = 1
            self.arrayDealer.append(moreCard.value)
            self.dealerTot += moreCard.value

            index = 0
            for i in self.arrayDealer:
                if(self.dealerTot > 21 and i == 11):
                    self.arrayDealer[index] = 1
                    self.dealerTot = self.dealerTot - 10
                index += 1

            self.dealerScoreLabel.setText(str(self.dealerTot))
            self.dealerScoreLabel.move(1025,200)
        
        #disabiling stay button
        self.stayButton.setEnabled(False)

        #if win statement
        if(self.playerTot <= 21 and (self.playerTot > self.dealerTot or self.dealerTot > 21)):
            self.win()
        
        #if tie statement
        elif(self.playerTot <= 21 and self.playerTot == self.dealerTot):
            self.tie()

        #if lost 
        else:
            self.lost()
        


    def win(self):
        #setting win window visible
        self.winWindow.setFixedSize(200,100)
        self.winWindow.setLayout(self.winLayout)
        self.winWindow.setVisible(True)

        #getting new money total
        self.totalMoney += self.betMoney

        #printing to new window
        self.winLabel.setText("YOU WIN!!!")
        self.winLabel.adjustSize()
        self.winLabel.move(50,40)
        self.winWindow.setStyleSheet("background-color: green;")
        self.betLabel.setText("Money: $" + str(self.totalMoney))
        self.betLabel.adjustSize()

    def tie(self):
        #setting window visible
        self.winWindow.setFixedSize(200,100)
        self.winWindow.setLayout(self.winLayout)
        self.winWindow.setVisible(True)

        #getting new money total
        self.totalMoney = self.totalMoney

        #printing to new window
        self.winLabel.setText("YOU TIED.")
        self.winLabel.adjustSize()
        self.winLabel.move(50,40)
        self.winWindow.setStyleSheet("background-color: yellow;")
        self.betLabel.setText("Money: $" + str(self.totalMoney))
        self.betLabel.adjustSize()

    def lost(self):
        #setting window visible
        self.winWindow.setFixedSize(200,100)
        self.winWindow.setLayout(self.winLayout)
        self.winWindow.setVisible(True)
        
        #getting new money total
        self.totalMoney = self.totalMoney - self.betMoney
        
        #printing to new window
        self.winLabel.setText("YOU LOST :(")
        self.winLabel.adjustSize()
        self.winLabel.move(50,40)
        self.winWindow.setStyleSheet("background-color: red;")
        self.betLabel.setText("Money: $" + str(self.totalMoney))
        self.betLabel.adjustSize()

    def double(self):
        #doubling bet amount
        self.betMoney = self.betMoney + self.betMoney
        
        self.betPerRoundLabel.setText("Bet Amount: $" + str(self.betMoney))
        self.betPerRoundLabel.adjustSize()

        #disabliling buttons
        self.hitButton.setEnabled(False)
        self.splitButton.setEnabled(False)

        #getting another card
        doubleCard = Card()
        self.layout.addWidget(doubleCard,5,5,1,2)
        self.arrayPlayer.append(doubleCard.value)

        #checking for ace
        if(doubleCard.value == 11 and self.playerTot >= 11):
            doubleCard.value = 1

        self.playerTot += doubleCard.value

        #checking for aces already in hand
        index = 0
        for i in self.arrayPlayer:
            if(self.playerTot > 21 and i == 11):
                self.arrayPlayer[index] = 1
                self.playerTot = self.playerTot - 10
            index += 1
        
        self.playerTot = 0

        #setting value
        for i in self.arrayPlayer:
            self.playerTot+=i
        
        self.scoreLabel.setText(str(self.playerTot))
        self.scoreLabel.move(1025,800)

        if(self.playerTot > 21):
            self.lost()

        else:
            #calling stay
            self.stay()
        

    def split(self):
        #doubling money
        self.betMoney = self.betMoney*2
        self.betPerRoundLabel.setText("Bet Amount: $" + str(self.betMoney))
        self.betPerRoundLabel.adjustSize()

        #creating hit and stay buttons for split
        self.hitButton1 = QPushButton("HIT 1")
        self.hitButton2 = QPushButton("HIT 2")
        self.stayButton1 = QPushButton("STAY 1")
        self.stayButton2 = QPushButton("STAY 2")
        
        #clearing arrays
        self.arrayS1.clear()
        self.arrayS2.clear()
        
        #disabiling other buttons
        self.doubleButton.setEnabled(False)
        self.hitButton.setEnabled(False)
        self.stayButton.setEnabled(False)
        self.splitButton.setEnabled(False)
        self.stayButton1.setEnabled(False)
        self.stayButton2.setEnabled(False)
        self.hitButton2.setEnabled(False)

        #adding widgets
        self.layout.addWidget(self.hitButton1, 1, 1, 1,1)
        self.layout.addWidget(self.stayButton1, 1, 2, 1,1)
        self.layout.addWidget(self.hitButton2, 2, 1, 1,1)
        self.layout.addWidget(self.stayButton2, 2, 2, 1,1)

        self.score1.setText("Score 1: ")
        self.score1.adjustSize()
        self.score1.move(50,620)

        self.score2.setText("Score 2: ")
        self.score2.adjustSize()
        self.score2.move(50,675)

        #adding values
        self.total1 = int(self.playerTot/2)
        self.total2 = int(self.playerTot/2)

        self.arrayS1.append(self.total1)
        self.arrayS2.append(self.total2)

        
        self.label.setText("")
        
        #moving totals on screen
        self.scoreLabel.setText(str(self.total1))
        self.scoreLabel.move(150,620)

        self.scoreLabel2.setText(str(self.total2))
        self.scoreLabel2.move(150, 675)

        #checking for clicked buttons
        self.hitButton1.clicked.connect(self.hit1)
        self.hitButton2.clicked.connect(self.hit2)
        self.stayButton1.clicked.connect(self.stay1)
        self.stayButton2.clicked.connect(self.stay2)

        #height for cards
        self.height1 = 6
        self.height2 = 6

    def hit1(self):
        #adding a card
        hit1Card = Card()
        
        #adding card to screen
        self.layout.addWidget(hit1Card,self.height1,1,1,2)
       
        #adding 1 to height
        self.height1+=1

        #checking for aces
        if(hit1Card.value == 11 and self.total1 > 11):
            hit1Card.value = 1
        self.total1 += hit1Card.value

        self.arrayS1.append(hit1Card.value)

        #checking for aces in hand
        index = 0
        for i in self.arrayS1:
            if(self.total1 > 21 and i == 11):
                self.arrayS1[index] = 1
                self.total1 = self.total1 - 10
            index += 1

        
        self.scoreLabel.setText(str(self.total1))

        self.stayButton1.setEnabled(True)
        
        #disabiling hit button
        if(self.total1 >= 21):
            self.hitButton1.setEnabled(False)
        
    def hit2(self):
        #adding a card
        hit2Card = Card()

        #adding card to screen
        self.layout.addWidget(hit2Card, self.height2, 3, 1, 2)

        #adding 1 to height
        self.height2+=1

        #checking for aces
        if(hit2Card.value == 11 and self.total2 > 11):
            hit2Card.value = 1
        
        self.total2 += hit2Card.value

        self.arrayS1.append(hit2Card.value)

        #checking for aces in hand
        index = 0
        for i in self.arrayS2:
            if(self.total2 > 21 and i == 11):
                self.arrayS2[index] = 1
                self.total2 = self.total2 - 10
            index += 1

        self.scoreLabel2.setText(str(self.total2))

        self.stayButton2.setEnabled(True)

        #disabiling buttons
        if(self.total2 >= 21):
            self.hitButton2.setEnabled(False)

        if(self.total1 > 21 and self.total2 > 21):
            self.stayButton2.setEnabled(False)
            self.lost()


    def stay1(self):
        #enabiling and disabiling buttons
        self.hitButton2.setEnabled(True)
        self.stayButton1.setEnabled(False)
        self.hitButton1.setEnabled(False)


    def stay2(self):
        self.stayButton2.setEnabled(False)
        
        #getting a dealer a card
        newDealerCard = Card()
        self.layout.addWidget(newDealerCard, 0, self.dealerLength,1,2)
        self.dealerLength+=2
        if(newDealerCard.value == 11 and self.dealerTot >= 11):
                newDealerCard.value = 1
        self.dealerTot += newDealerCard.value
        
        #setting dealer score label
        self.dealerScoreLabel.setText(str(self.dealerTot))
        self.dealerScoreLabel.move(1025,200)

        #having dealer get new card if their total is less than 17
        while(self.dealerTot < 17):
            moreCard = Card()
            self.layout.addWidget(moreCard, 0, self.dealerLength,1,2)
            self.dealerLength+=2
            if(moreCard.value == 11 and self.dealerTot > 11):
                moreCard.value = 1
            self.dealerTot += moreCard.value

            index = 0
            for i in self.arrayDealer:
                if(self.dealerTot > 21 and i == 11):
                    self.arrayPlayer[index] = 1
                    self.dealerTot = self.dealerTot - 10
                index += 1

            self.dealerScoreLabel.setText(str(self.dealerTot))
            self.dealerScoreLabel.move(1025,200)

        #setting win logic for the split
        if(self.total1 <= 21 and self.total2 <= 21 and ((self.total1 > self.dealerTot and self.total2 > self.dealerTot) or self.dealerTot > 21)):
            self.win()
        
        elif(self.total1 > 21 and self.total2 > 21 or (self.total1 < self.dealerTot and self.total2 < self.dealerTot and self.dealerTot < 21) or (self.total1 < self.dealerTot and self.total2 > 21 and self.dealerTot <21) or (self.total1 > 21 and self.total2 < self.dealerTot and self.dealerTot < 21)):
            self.lost()

        elif((self.total1 == self.dealerTot or self.total2 == self.dealerTot) and (self.total1 <= 21 and self.total2 <= 21 and ((self.total1 > self.dealerTot or self.total2 > self.dealerTot)))):
            self.totalMoney = int(self.totalMoney + (self.betMoney/2))
            self.tie()

        elif((self.total1 == self.dealerTot or self.total2 == self.dealerTot) and (self.total1 > 21 or self.total2 > 21 or (self.total1 < self.dealerTot or self.total2 < self.dealerTot))):
            self.totalMoney = int(self.totalMoney - (self.betMoney/2))
            self.tie()
        else:
            self.tie()
        
        

    def bet(self):
        #adding bet amount label to main window
        self.totalMoney = int(self.betInput.text())
        self.betLabel = QLabel(self.window)
        self.betLabel.setText("Money: $" + str(self.totalMoney))
        self.betLabel.adjustSize()
        self.betLabel.move(50,0)

        #setting enter total money window to false
        self.startWindow.setVisible(False)

        #setting the main window to visible
        self.window.setFixedSize(1200,1000)
        self.window.setLayout(self.layout)
        self.window.setStyleSheet("background-color: lightgreen;")

        #calling bet round
        self.betRound()
       

    def newGame(self):
        #clearing arrays
        self.arrayPlayer.clear()
        self.arrayDealer.clear()
        self.arrayS1.clear()
        self.arrayS2.clear()
        #getting rid of current cards
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().deleteLater()

        self.score1.setText("")
        self.score2.setText("")
        self.scoreLabel2.setText("")
        
        #calling bet round
        self.betRound()

        #creating buttons
        self.hitButton = QPushButton("HIT")
        self.doubleButton = QPushButton("DOUBLE")
        self.stayButton = QPushButton("STAY")
        self.splitButton = QPushButton("SPLIT")
        self.newGameButton = QPushButton("NEW GAME")
        
        
        #adding buttons
        self.layout.addWidget(self.hitButton, 0, 0, 1,1)
        self.layout.addWidget(self.doubleButton, 1, 0, 1,1)
        self.layout.addWidget(self.stayButton, 2, 0, 1,1)
        self.layout.addWidget(self.splitButton, 3,0,1,1)
        self.layout.addWidget(self.newGameButton, 6,0,1,1)

        
        #enabiling all of them
        self.doubleButton.setEnabled(True)
        self.splitButton.setEnabled(True)
        self.hitButton.setEnabled(True)
        self.stayButton.setEnabled(True)
        self.splitButton.setEnabled(True)

        #score total and length of window
        self.playerTot = 0
        self.dealerTot = 0
        self.length = 5
        self.dealerLength = 3
        
        
        #calling first cards onto screen
        firstCard = Card()
        secondCard= Card()
        dealerCard = Card()
        self.layout.addWidget(firstCard, 5,1,1,2)
        self.layout.addWidget(secondCard, 5,3,1,2)
        self.layout.addWidget(dealerCard, 0,1,1,2)

        #checking if both are aces
        if(firstCard.value == 11 and secondCard.value == 11):
            secondCard.value =1

        #adding cards to array
        self.arrayPlayer.append(firstCard.value)
        self.arrayPlayer.append(secondCard.value)
        self.arrayDealer.append(dealerCard.value)

        #score label reset
        self.label = QLabel(self.window)
        self.label.setText("Score: ")
        self.label.adjustSize()
        self.label.move(900,800)
        
        #disabiling split unless cards are same
        self.splitButton.setEnabled(False)
        if(firstCard.type == secondCard.type):
            self.splitButton.setEnabled(True)

        #setting score
        self.playerTot = firstCard.value + secondCard.value
        self.scoreLabel.setText(str(self.playerTot))
        self.scoreLabel.move(1025,800)

        #setting dealer score
        self.dealerTot = dealerCard.value
        
        self.dealerScoreLabel.setText(str(self.dealerTot))
        self.dealerScoreLabel.move(1025,200)


        #calling hit button if hit button is clicked
        self.hitButton.clicked.connect(self.hit)
        
        self.stayButton.clicked.connect(self.stay)

        self.doubleButton.clicked.connect(self.double)

        self.splitButton.clicked.connect(self.split)

        self.newGameButton.clicked.connect(self.newGame)

        

    #betMoney = per round bet
    #self.totalMoney = total money in game

    def betRound(self):
        #creating line edit
        self.betInputBettingWindow = QLineEdit()

        #validating that number inputed is valid
        moneyCheck = QIntValidator(0, self.totalMoney)
        self.betInputBettingWindow.setValidator(moneyCheck)

        #showing bet window
        self.betWindow.setFixedSize(800, 600)
        self.betWindow.setLayout(self.betLayout)
        self.betWindow.setVisible(True)
        self.window.setVisible(False)

        #adding text box and bet button
        self.betLayout.addWidget(self.betInputBettingWindow,1,0,1,1)
        self.betPerRoundLabelBettingWindow.setText("Enter money to bet.")
        self.betPerRoundLabelBettingWindow.adjustSize()
        self.betPerRoundLabelBettingWindow.move(25,25)
        betButton2 = QPushButton("BET")
        self.betLayout.addWidget(betButton2, 2,0,1,1)
        betButton2.clicked.connect(self.amountBet)

        
    def amountBet(self):
        #creating int for bet amount per game
        if(self.betInputBettingWindow.hasAcceptableInput()):
            self.betMoney = 0
            self.betMoney = int(self.betInputBettingWindow.text())
            
            #creating label
            self.betPerRoundLabel = QLabel(self.window)
            self.betPerRoundLabel.setText("")
            self.betPerRoundLabel.adjustSize()
            self.betPerRoundLabel.setText("Bet Amount: $" + str(self.betMoney))
            self.betPerRoundLabel.adjustSize()
            self.betPerRoundLabel.move(50,50)
            self.betWindow.setVisible(False)
            self.window.setVisible(True)

            #disabiling double and split button if total money is less than twice the bet money
            if(self.betMoney*2 > self.totalMoney):
                self.doubleButton.setEnabled(False)
                self.splitButton.setEnabled(False)
        
        #showing main window
        

        



if __name__ == "__main__":

    Blackjack().main()