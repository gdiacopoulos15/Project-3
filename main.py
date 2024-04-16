
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QLabel, QLineEdit
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
        self.betPerRoundLabel = QLabel(self.betWindow)

        #bet amount
        self.totalMoney = 0
        self.betMoney = 0
        
        #buttons on main screen
        self.layout = QGridLayout()
        self.hitButton = QPushButton("HIT")
        self.doubleButton = QPushButton("DOUBLE")
        self.stayButton = QPushButton("STAY")
        self.splitButton = QPushButton("SPLIT")
        betMoreButton = QPushButton("BET ⬆")
        betLessButton = QPushButton("BET ⬇")
        hintButton = QPushButton("HINT")
        #object, location, size
        
        #adding buttons
        self.layout.addWidget(self.hitButton, 0, 0, 1,1)
        self.layout.addWidget(self.doubleButton, 1, 0, 1,1)
        self.layout.addWidget(self.stayButton, 2, 0, 1,1)
        self.layout.addWidget(self.splitButton, 3,0,1,1)
        self.layout.addWidget(betMoreButton, 4,0,1,1)
        self.layout.addWidget(betLessButton, 5,0,1,1)
        self.layout.addWidget(hintButton, 6,0,1,1)
        #self.layout.addWidget(subWindow, 0,,0)

        #adding score label
        label = QLabel(self.window)
        label.setText("Score: ")
        label.move(900,900)
        self.scoreLabel = QLabel(self.window)

        label2 = QLabel(self.window)
        label2.setText("Dealer \nScore: ")
        label2.move(900,200)
        self.dealerScoreLabel = QLabel(self.window)

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

        #setting score
        self.playerTot = firstCard.value + secondCard.value
        self.scoreLabel.setText(str(self.playerTot))
        self.scoreLabel.move(975,900)

        #setting dealer score
        self.dealerTot = dealerCard.value

        self.dealerScoreLabel.setText(str(self.dealerTot))
        self.dealerScoreLabel.move(1025,200)

        #calling hit button if hit button is clicked
        self.hitButton.clicked.connect(self.hit)
        
        self.stayButton.clicked.connect(self.stay)

        self.doubleButton.clicked.connect(self.double)

        #better input widget
        startLayout.addWidget(self.betInput,1,0,1,1)
        betLabel.setText("Enter money to start with.")
        betLabel.move(25,25)
        betButton = QPushButton("START")
        startLayout.addWidget(betButton, 2,0,1,1)
        betButton.clicked.connect(self.bet)

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
        additionalCard = Card()
        self.layout.addWidget(additionalCard,5,self.length,1,2)
        self.length +=2
        self.playerTot += additionalCard.value
        self.scoreLabel.setText(str(self.playerTot))
        self.scoreLabel.move(975,900)
        if(self.playerTot > 21):
            self.hitButton.setEnabled(False)

    def stay(self):
        newDealerCard = Card()
        self.layout.addWidget(newDealerCard, 0, self.dealerLength,1,2)
        self.dealerLength+=2
        self.dealerTot += newDealerCard.value
        self.dealerScoreLabel.setText(str(self.dealerTot))
        self.dealerScoreLabel.move(1025,200)
        if(self.dealerTot < 17):
            moreCard = Card()
            self.layout.addWidget(moreCard, 0, self.dealerLength,1,2)
            self.dealerLength+=2
            self.dealerTot += moreCard.value
            self.dealerScoreLabel.setText(str(self.dealerTot))
            self.dealerScoreLabel.move(1025,200)
        
        self.stayButton.setEnabled(False)

    def double(self):
        doubleCard = Card()
        self.layout.addWidget(doubleCard,5,5,1,2)
        self.playerTot += doubleCard.value
        self.scoreLabel.setText(str(self.playerTot))
        self.scoreLabel.move(975,900)
        self.stay()

    def bet(self):
        self.totalMoney = int(self.betInput.text())
        self.betLabel = QLabel(self.window)
        self.betLabel.setText("Money: " + str(self.totalMoney))
        self.betLabel.move(50,0)
        self.startWindow.setVisible(False)
        self.window.setFixedSize(1200,1000)
        self.window.setLayout(self.layout)
        self.window.setVisible(True)
        #self.betRound()
        

   # def betRound(self):
        #showing bet window
    #    self.betWindow.setFixedSize(800, 600)
     #   self.betWindow.setLayout(self.layout)
      #  self.betWindow.setVisible(True)

        #adding text box and bet button
       # self.betLayout.addWidget(self.betInput,1,0,1,1)
        #self.betPerRoundLabel.setText("Enter money to bet.")
        #self.betPerRoundLabel.move(25,25)
        #betButton2 = QPushButton("BET")
        #self.betLayout.addWidget(betButton2, 2,0,1,1)

        #self.betMoney = int(self.inputPerRound.text())
        #self.betPerRoundLabel = QLabel(self.window)
        #self.betPerRoundLabel.setText("Bet Amount: " + str(self.betMoney))
        #self.betPerRoundLabel.move(50,50)
        #self.betWindow.setVisible(False)
        #showing main window
        #if(betButton2.clicked.connect):
         #   self.window.setFixedSize(1200,1000)
          #  self.window.setLayout(self.layout)
           # self.window.setVisible(True)
        



if __name__ == "__main__":

    Blackjack().main()