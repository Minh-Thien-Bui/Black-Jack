from tkinter import *
import random

class Card:
    def __init__(self, value = 14, image = "Image Directory"):
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
        self.jackSpades = Card(11)
        self.queenSpades = Card(12)
        self.kingSpades = Card(13)
        self.aceHearts = Card(14)
        self.twoHearts = Card(2)
        self.threeHearts = Card(3)
        self.fourHearts = Card(4)
        self.fiveHearts = Card(5)
        self.sixHearts = Card(6)
        self.sevenHearts = Card(7)
        self.eightHearts = Card(8)
        self.nineHearts = Card(9)
        self.tenHearts = Card(10)
        self.jackHearts = Card(11)
        self.queenHearts = Card(12)
        self.kingHearts = Card(13)
        self.aceDiamonds = Card(14)
        self.twoDiamonds = Card(2)
        self.threeDiamonds = Card(3)
        self.fourDiamonds = Card(4)
        self.fiveDiamonds = Card(5)
        self.sixDiamonds = Card(6)
        self.sevenDiamonds = Card(7)
        self.eightDiamonds = Card(8)
        self.nineDiamonds = Card(9)
        self.tenDiamonds = Card(10)
        self.jackDiamonds = Card(11)
        self.queenDiamonds = Card(12)
        self.kingDiamonds = Card(13)
        self.aceClubs = Card(14)
        self.twoClubs = Card(2)
        self.threeClubs = Card(3)
        self.fourClubs = Card(4)
        self.fiveClubs = Card(5)
        self.sixClubs = Card(6)
        self.sevenClubs = Card(7)
        self.eightClubs = Card(8)
        self.nineClubs = Card(9)
        self.tenClubs = Card(10)
        self.jackClubs = Card(11)
        self.queenClubs = Card(12)
        self.kingClubs = Card(13)
        self.jokerBlack = Card(1)
        self.jokerRed = Card(1)

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
            self.kingClubs,
            self.jokerBlack,
            self.jokerRed
        ]

        self.cardFace = []
        self.cardBack = PhotoImage(file = "image/card/b1fv.gif")
        
        for i in range(54):
            self.deck[i].setImage("image/card/" + str(i + 1) + ".gif")
            self.cardFace.append(PhotoImage(file = self.deck[i].getImage()))
        
        frame = Frame(window)
        frame.pack()

        self.dealerHand = [
            Label(frame, image = self.cardFace[0]),
            Label(frame, image = self.cardBack)
        ]

        self.shuffle()

        self.dealerHand[0].pack(side = LEFT)
        self.dealerHand[1].pack(side = LEFT)

        Button(window, text = "High", command = self.high).pack()
        Button(window, text = "Low", command = self.low).pack()
        Button(window, text = "Shuffle", command = self.shuffle).pack()

        window.mainloop()

    def high(self):
        self.dealerHand[1]["image"] = self.cardFace[1]

        if self.deck[1].getValue() > self.deck[0].getValue():
            print("Card is high, you win")

        elif self.deck[1].getValue() < self.deck[0].getValue():
            print("Card is low, you lose")

        else:
            print("Card values are equal, you tied")

    def low(self):
        self.dealerHand[1]["image"] = self.cardFace[1]

        if self.deck[1].getValue() > self.deck[0].getValue():
            print("Card is high, you lose")

        elif self.deck[1].getValue() < self.deck[0].getValue():
            print("Card is low, you win")

        else:
            print("Card values are equal, you tied")

    def shuffle(self):
        random.shuffle(self.deck)

        for i in range(54):
            self.cardFace[i] = (PhotoImage(file = self.deck[i].getImage()))

        self.dealerHand[0]["image"] = self.cardFace[0]
        self.dealerHand[1]["image"] = self.cardBack


BlackJack()
