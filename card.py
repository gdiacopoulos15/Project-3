from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout
import random


class Card(QPushButton):
    def __init__(self):
        super(QPushButton,self).__init__()
        #self.btn_Save.setEnabled(False)
        #self.btn_Close.setEnabled(False)
        cardList = ['A', '2','3','4','5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cardValue = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.y = random.randrange(1,13)
        #cardNum = random.choice(cardList)
        self.type = cardList[self.y]
        self.setText(self.type)
        self.value = self.cardValue[self.y]
        self.indexArray = []
        self.indexArray.append(self.y)
        


        


    