from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout
import random


class Card(QPushButton):
    def __init__(self):
        super(QPushButton,self).__init__()
        #creating card labels and values
        self.cardList = ['A', '2','3','4','5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cardValue = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        #getting a random value
        self.y = random.randrange(0,13)
        
        #getting the type and value for the random number
        self.type = self.cardList[self.y]
        self.setText(self.type)
        self.value = self.cardValue[self.y]
        self.indexArray = []
        self.indexArray.append(self.y)
        
        


        


    