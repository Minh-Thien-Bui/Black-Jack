from tkinter import *
import random

class Card:
    def __init__(self, value = 1, image = "Image Directory"):
        self.__value = value
        self.__image = image

    def getValue(self):
        return self.__value

    def getImage(self):
        return self.__image

    def setValue(self, value):
        self.__value = value

    def setImage(self, image):
        self.__image = image


class BlackJack():
    def __init__(self):
        window = Tk()
        window.title("Blackjack")

        self.aceSpades = Card()
        self.twoSpades = Card(2)
        self.threeSpades = Card(3)
        self.fourSpades = Card(4)
        self.fiveSpades = Card(5)
        self.sixSpades = Card(6)
        self.sevenSpades = Card(7)
        self.eightSpades = Card(8)
        self.nineSpades = Card(9)
        self.tenSpades = Card(10)
        self.jackSpades = Card(10)
        self.queenSpades = Card(10)
        self.kingSpades = Card(10)
        self.aceHearts = Card()
        self.twoHearts = Card(2)
        self.threeHearts = Card(3)
        self.fourHearts = Card(4)
        self.fiveHearts = Card(5)
        self.sixHearts = Card(6)
        self.sevenHearts = Card(7)
        self.eightHearts = Card(8)
        self.nineHearts = Card(9)
        self.tenHearts = Card(10)
        self.jackHearts = Card(10)
        self.queenHearts = Card(10)
        self.kingHearts = Card(10)
        self.aceDiamonds = Card()
        self.twoDiamonds = Card(2)
        self.threeDiamonds = Card(3)
        self.fourDiamonds = Card(4)
        self.fiveDiamonds = Card(5)
        self.sixDiamonds = Card(6)
        self.sevenDiamonds = Card(7)
        self.eightDiamonds = Card(8)
        self.nineDiamonds = Card(9)
        self.tenDiamonds = Card(10)
        self.jackDiamonds = Card(10)
        self.queenDiamonds = Card(10)
        self.kingDiamonds = Card(10)
        self.aceClubs = Card()
        self.twoClubs = Card(2)
        self.threeClubs = Card(3)
        self.fourClubs = Card(4)
        self.fiveClubs = Card(5)
        self.sixClubs = Card(6)
        self.sevenClubs = Card(7)
        self.eightClubs = Card(8)
        self.nineClubs = Card(9)
        self.tenClubs = Card(10)
        self.jackClubs = Card(10)
        self.queenClubs = Card(10)
        self.kingClubs = Card(10)
        self.jokerBlack = Card(0)
        self.jokerRed = Card(0)

        self.deck = [
            self.aceSpades,
            self.twoSpades,
            self.threeSpades,
            self.fourSpades,
            self.fiveSpades,
            self.sixSpades,
            self.sevenSpades,
            self.eightSpades,
            self.nineSpades,
            self.tenSpades,
            self.jackSpades,
            self.queenSpades,
            self.kingSpades,
            self.aceHearts,
            self.twoHearts,
            self.threeHearts,
            self.fourHearts,
            self.fiveHearts,
            self.sixHearts,
            self.sevenHearts,
            self.eightHearts,
            self.nineHearts,
            self.tenHearts,
            self.jackHearts,
            self.queenHearts,
            self.kingHearts,
            self.aceDiamonds,
            self.twoDiamonds,
            self.threeDiamonds,
            self.fourDiamonds,
            self.fiveDiamonds,
            self.sixDiamonds,
            self.sevenDiamonds,
            self.eightDiamonds,
            self.nineDiamonds,
            self.tenDiamonds,
            self.jackDiamonds,
            self.queenDiamonds,
            self.kingDiamonds,
            self.aceClubs,
            self.twoClubs,
            self.threeClubs,
            self.fourClubs,
            self.fiveClubs,
            self.sixClubs,
            self.sevenClubs,
            self.eightClubs,
            self.nineClubs,
            self.tenClubs,
            self.jackClubs,
            self.queenClubs,
            self.kingClubs
        ]

        random.shuffle(self.deck)

        self.cardFace = []
        
        for i in range(52):
            self.deck[i].setImage("image/card/" + str(i + 1) + ".gif")
            self.cardFace.append(PhotoImage(file = self.deck[i].getImage()))
            
        frame = Frame(window)
        frame.pack()

        self.dealerHand = []
        for i in range(4):
            self.dealerHand.append(Label(frame, image = self.cardFace[i]))
            self.dealerHand[i].pack(side = LEFT)

        Button(window, text = "Hit", command = hit).pack()

        Button(window, text = "Stay", command = stay).pack()

        window.mainloop()

def hit():
    print("You Drew")

def stay():
    print("You Stayed")

BlackJack()
