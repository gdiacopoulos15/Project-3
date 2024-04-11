from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout
import random


class Card(QPushButton):
    def __init__(self):
        super(QPushButton,self).__init__()
        #self.btn_Save.setEnabled(False)
        #self.btn_Close.setEnabled(False)
        cardList = ['A', '2','3','4','5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        cardValue = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        y = random.randrange(1,14)
        #cardNum = random.choice(cardList)
        self.type = cardList[y]
        self.setText(self.type)
        total = []
        total.append(cardValue[y])
        


        


    