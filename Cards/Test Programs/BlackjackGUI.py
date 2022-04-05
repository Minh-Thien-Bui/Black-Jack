from tkinter import *
import random

class Card:
    def __init__(self, value = 1, image = 1):
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
        self.twoSpades = Card(2, 2)
        self.threeSpades = Card(3, 3)
        self.fourSpades = Card(4, 4)
        self.fiveSpades = Card(5, 5)
        self.sixSpades = Card(6, 6)
        self.sevenSpades = Card(7, 7)
        self.eightSpades = Card(8, 8)
        self.nineSpades = Card(9, 9)
        self.tenSpades = Card(10, 10)
        self.jackSpades = Card(10, 11)
        self.queenSpades = Card(10, 12)
        self.kingSpades = Card(10, 13)
        self.aceHearts = Card(1, 14)
        self.twoHearts = Card(2, 15)
        self.threeHearts = Card(3, 16)
        self.fourHearts = Card(4, 17)
        self.fiveHearts = Card(5, 18)
        self.sixHearts = Card(6, 19)
        self.sevenHearts = Card(7, 20)
        self.eightHearts = Card(8, 21)
        self.nineHearts = Card(9, 22)
        self.tenHearts = Card(10, 23)
        self.jackHearts = Card(10, 24)
        self.queenHearts = Card(10, 25)
        self.kingHearts = Card(10, 26)
        self.aceDiamonds = Card(1, 27)
        self.twoDiamonds = Card(2, 28)
        self.threeDiamonds = Card(3, 29)
        self.fourDiamonds = Card(4, 30)
        self.fiveDiamonds = Card(5, 31)
        self.sixDiamonds = Card(6, 32)
        self.sevenDiamonds = Card(7, 33)
        self.eightDiamonds = Card(8, 34)
        self.nineDiamonds = Card(9, 35)
        self.tenDiamonds = Card(10, 36)
        self.jackDiamonds = Card(10, 37)
        self.queenDiamonds = Card(10, 38)
        self.kingDiamonds = Card(10, 39)
        self.aceClubs = Card(1, 40)
        self.twoClubs = Card(2, 41)
        self.threeClubs = Card(3, 42)
        self.fourClubs = Card(4, 43)
        self.fiveClubs = Card(5, 44)
        self.sixClubs = Card(6, 45)
        self.sevenClubs = Card(7, 46)
        self.eightClubs = Card(8, 47)
        self.nineClubs = Card(9, 48)
        self.tenClubs = Card(10, 49)
        self.jackClubs = Card(10, 50)
        self.queenClubs = Card(10, 51)
        self.kingClubs = Card(10, 52)
        self.jokerBlack = Card(0, 53)
        self.jokerRed = Card(0, 54)

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
        for i in range(53):
            self.cardFace.append(PhotoImage(file = "image/card/" + str(self.deck[i + 1].getImage()) + ".gif"))
        
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
'''
def blackJack():
    random.shuffle(deck)
    dealer = [deck[0], deck[1]]
    dealerValue = dealer[0].getValue() + dealer[1].getValue()
    
    print("Dealer drew", dealer[0].getValue(), dealer[1].getValue(), "\nDealer value is", dealerValue)

    playerDraw(deck)
    
def playerDraw(deck):
    i = 2
    player = [deck[i]]
    i += 1
    player.append(deck[i])

    print("You drew", player[0].getValue(), player[1].getValue())
'''

BlackJack()
