
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtGui import QColor, QPainter
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

        #creating label for scores
        self.scoreLabel = QLabel(self.window)
        self.dealerScoreLabel = QLabel(self.window)

        #bet amount
        self.totalMoney = 0
        self.betMoney = 0
        
        #buttons on main screen
        self.layout = QGridLayout()
        
        #calling newGame to show first game
        self.newGame()

        #adding score label
        label = QLabel(self.window)
        label.setText("Score: ")
        label.move(900,900)
        self.scoreLabel = QLabel(self.window)

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
#make cards self
#make cards unclickable

    def hit(self):
        #disabiling buttons
        self.doubleButton.setEnabled(False)
        self.splitButton.setEnabled(False)

        #getting another card
        additionalCard = Card()
        self.layout.addWidget(additionalCard,5,self.length,1,2)
        self.length +=2
        #checking for ace
        if(additionalCard.value == 11 and self.playerTot > 11):
            additionalCard.value = 1
        self.playerTot += additionalCard.value

        #if(self.playerTot > 21 and )
        
        self.scoreLabel.setText(str(self.playerTot))
        self.scoreLabel.move(975,900)
        
        #disabiling button if total is 21 or higher
        if(self.playerTot >= 21):
            self.hitButton.setEnabled(False)

    def stay(self):
        #disabiling buttons
        self.hitButton.setEnabled(False)
        self.doubleButton.setEnabled(False)
        self.splitButton.setEnabled(False)
        
        #getting a dealer a card
        newDealerCard = Card()
        self.layout.addWidget(newDealerCard, 0, self.dealerLength,1,2)
        self.dealerLength+=2
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
            self.dealerScoreLabel.setText(str(self.dealerTot))
            self.dealerScoreLabel.move(1025,200)
        
        #disabiling stay button
        self.stayButton.setEnabled(False)

    def double(self):
        #disabliling buttons
        self.hitButton.setEnabled(False)
        self.splitButton.setEnabled(False)

        #getting another card
        doubleCard = Card()
        self.layout.addWidget(doubleCard,5,5,1,2)
        #setting value
        self.playerTot += doubleCard.value
        self.scoreLabel.setText(str(self.playerTot))
        self.scoreLabel.move(975,900)

        #calling stay
        self.stay()

    def split(self):
        #creating hit and stay buttons for split
        self.hitButton1 = QPushButton("HIT 1")
        self.hitButton2 = QPushButton("HIT 2")
        self.stayButton1 = QPushButton("STAY 1")
        self.stayButton2 = QPushButton("STAY 2")
        #adding another score label
        self.score1 = QLabel(self.window)
        self.score1.setText("Score 1: ")
        self.score1.move(900,950)
        
        #disabiling other buttons
        self.doubleButton.setEnabled(False)
        self.hitButton.setEnabled(False)
        self.stayButton.setEnabled(False)

        #adding widgets
        self.layout.addWidget(self.hitButton1, 1, 1, 1,1)
        self.layout.addWidget(self.stayButton1, 1, 2, 1,1)
        self.layout.addWidget(self.hitButton2, 2, 1, 1,1)
        self.layout.addWidget(self.stayButton2, 2, 2, 1,1)
        #adding values
        
        self.total1 = self.playerTot/2
        self.total2 = self.playerTot/2

        self.hitButton1.clicked.connect(self.hit1)
        #self.hitButton2.clicked.connect(self.hit2)
        #self.stayButton1.clicked.connect(self.stay1)
        self.stayButton2.clicked.connect(self.stay)
        self.height1 = 6

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

        #if(self.playerTot > 21 and )
        
        #printing score to screen
        self.scoreLabel.setText(str(self.total1))
        self.scoreLabel.move(675,600)
        #disabiling hit button
        if(self.total1 >= 21):
            self.hitButton1.setEnabled(False)
        



    def bet(self):
        #adding bet amount label to main window
        self.totalMoney = int(self.betInput.text())
        self.betLabel = QLabel(self.window)
        self.betLabel.setText("Money: " + str(self.totalMoney))
        self.betLabel.move(50,0)
        #setting enter total money window to false
        self.startWindow.setVisible(False)
        #setting the main window to visible
        self.window.setFixedSize(1200,1000)
        self.window.setLayout(self.layout)
        self.window.setStyleSheet("background-color: lightgreen;")

        #calling bet round
        self.betRound()
        #self.window.setVisible(True)
        #self.betRound()

    def newGame(self):
        #getting rid of current cards
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().deleteLater()

        #calling bet round
        self.betRound()

        #creating buttons
        self.hitButton = QPushButton("HIT")
        self.doubleButton = QPushButton("DOUBLE")
        self.stayButton = QPushButton("STAY")
        self.splitButton = QPushButton("SPLIT")
        #betMoreButton = QPushButton("BET ⬆")
        #betLessButton = QPushButton("BET ⬇")
        self.newGameButton = QPushButton("NEW GAME")
        #object, location, size
        
        #adding buttons
        self.layout.addWidget(self.hitButton, 0, 0, 1,1)
        self.layout.addWidget(self.doubleButton, 1, 0, 1,1)
        self.layout.addWidget(self.stayButton, 2, 0, 1,1)
        self.layout.addWidget(self.splitButton, 3,0,1,1)
        #self.layout.addWidget(betMoreButton, 4,0,1,1)
        #self.layout.addWidget(betLessButton, 5,0,1,1)
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

        

       # self.splitButton.setEnabled(False)
        if(firstCard.type == secondCard.type):
           self.splitButton.setEnabled(True)

        #setting score
        self.playerTot = firstCard.value + secondCard.value
        self.scoreLabel.setText(str(self.playerTot))
        self.scoreLabel.move(1025,900)

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

        #self.indexArray.clear()

        

    def betRound(self):
        self.betInputBettingWindow = QLineEdit()
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
        self.betMoney = int(self.betInputBettingWindow.text())
        self.betPerRoundLabel = QLabel(self.window)
        self.betPerRoundLabel.setText("Bet Amount: " + str(self.betMoney))
        self.betPerRoundLabel.adjustSize()
        self.betPerRoundLabel.move(50,50)
        self.betWindow.setVisible(False)
        self.window.setVisible(True)
        #showing main window
        

        



if __name__ == "__main__":

    Blackjack().main()