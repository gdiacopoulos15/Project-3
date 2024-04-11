
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QLabel
from card import Card

class Blackjack(object):
    def main(self):
        app = QApplication(sys.argv)
        window = QWidget()
        
        layout = QGridLayout()
        hitButton = QPushButton("HIT")
        doubleButton = QPushButton("DOUBLE")
        stayButton = QPushButton("STAY")
        splitButton = QPushButton("SPLIT")
        betMoreButton = QPushButton("BET ⬆")
        betLessButton = QPushButton("BET ⬇")
        hintButton = QPushButton("HINT")
        #object, location, size
        layout.addWidget(hitButton, 0, 0, 1,1)
        layout.addWidget(doubleButton, 1, 0, 1,1)
        layout.addWidget(stayButton, 2, 0, 1,1)
        layout.addWidget(splitButton, 3,0,1,1)
        layout.addWidget(betMoreButton, 4,0,1,1)
        layout.addWidget(betLessButton, 5,0,1,1)
        layout.addWidget(hintButton, 6,0,1,1)
        #layout.addWidget(subWindow, 0,,0)
        label = QLabel(window)
        label.setText("Score: ")
        label.move(900,900)

        firstCard = Card()
        secondCard= Card()
        dealerCard = Card()
        layout.addWidget(firstCard, 5,1,1,2)
        layout.addWidget(secondCard, 5,3,1,2)
        layout.addWidget(dealerCard, 0,1,1,2)
        window.setFixedSize(1200,1000)
        window.setLayout(layout)
        window.setVisible(True)
        #if __name__ == "__main__":

        sys.exit(app.exec_())
        #QWidget()
        #gridlayout


if __name__ == "__main__":
    Blackjack().main()