from tkinter import *
import random

class Card:
    def __init__(self, value = 14, image = 1):
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
        self.jackSpades = Card(11, 11)
        self.queenSpades = Card(12, 12)
        self.kingSpades = Card(13, 13)
        self.aceHearts = Card(14, 14)
        self.twoHearts = Card(2, 15)
        self.threeHearts = Card(3, 16)
        self.fourHearts = Card(4, 17)
        self.fiveHearts = Card(5, 18)
        self.sixHearts = Card(6, 19)
        self.sevenHearts = Card(7, 20)
        self.eightHearts = Card(8, 21)
        self.nineHearts = Card(9, 22)
        self.tenHearts = Card(10, 23)
        self.jackHearts = Card(11, 24)
        self.queenHearts = Card(12, 25)
        self.kingHearts = Card(13, 26)
        self.aceDiamonds = Card(14, 27)
        self.twoDiamonds = Card(2, 28)
        self.threeDiamonds = Card(3, 29)
        self.fourDiamonds = Card(4, 30)
        self.fiveDiamonds = Card(5, 31)
        self.sixDiamonds = Card(6, 32)
        self.sevenDiamonds = Card(7, 33)
        self.eightDiamonds = Card(8, 34)
        self.nineDiamonds = Card(9, 35)
        self.tenDiamonds = Card(10, 36)
        self.jackDiamonds = Card(11, 37)
        self.queenDiamonds = Card(12, 38)
        self.kingDiamonds = Card(13, 39)
        self.aceClubs = Card(14, 40)
        self.twoClubs = Card(2, 41)
        self.threeClubs = Card(3, 42)
        self.fourClubs = Card(4, 43)
        self.fiveClubs = Card(5, 44)
        self.sixClubs = Card(6, 45)
        self.sevenClubs = Card(7, 46)
        self.eightClubs = Card(8, 47)
        self.nineClubs = Card(9, 48)
        self.tenClubs = Card(10, 49)
        self.jackClubs = Card(11, 50)
        self.queenClubs = Card(12, 51)
        self.kingClubs = Card(13, 52)
        self.jokerBlack = Card(1, 53)
        self.jokerRed = Card(1, 54)

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

        random.shuffle(self.deck)

        self.cardFace = []
        for i in range(54):
            self.cardFace.append(PhotoImage(file = "image/card/" + str(self.deck[i].getImage()) + ".gif"))

        self.cardBack = PhotoImage(file = "image/card/b1fv.gif")
        
        dealerFrame = Frame(window)
        dealerFrame.pack()

        self.dealerHand = []
        self.dealerHand.append(Label(dealerFrame, image = self.cardFace[0]))
        self.dealerHand.append(Label(dealerFrame, image = self.cardBack))

        self.dealerHand[0].pack(side = LEFT)
        self.dealerHand[1].pack(side = LEFT)

        buttonFrame = Frame(window)
        buttonFrame.pack()
        
        self.high = Button(buttonFrame, text = "High", command = self.high)
        self.high.pack()
        self.low = Button(buttonFrame, text = "Low", command = self.low)
        self.low.pack()
        self.shuffle = Button(buttonFrame, text = "Shuffle", command = self.shuffle)

        textFrame = Frame(window)
        textFrame.pack()

        self.print = Text(textFrame)
        self.print.insert(INSERT, "Initial value is " + str(self.deck[0].getValue()))
        self.print.pack()
        
        window.mainloop()

    def high(self):
        self.high.pack_forget()
        self.low.pack_forget()
        self.shuffle.pack()
        
        self.print.delete('1.0', END)
        self.print.insert(INSERT, "Initial value is " + str(self.deck[0].getValue()))

        self.dealerHand[1]["image"] = self.cardFace[1]

        if self.deck[1].getValue() > self.deck[0].getValue():
            self.print.insert(INSERT, "\nYou drew a value of " + str(self.deck[1].getValue()) + "\nCard value is high\nYou win")

        elif self.deck[1].getValue() < self.deck[0].getValue():
            self.print.insert(INSERT, "\nYou drew a value of " + str(self.deck[1].getValue()) + "\nCard value is low\nYou lose")

        else:
            self.print.insert(INSERT, "\nYou drew a value of " + str(self.deck[1].getValue()) + "\nCard values are equal\nYou tied")

    def low(self):
        self.high.pack_forget()
        self.low.pack_forget()
        self.shuffle.pack()
        
        self.print.delete('1.0', END)
        self.print.insert(INSERT, "Initial value is " + str(self.deck[0].getValue()))

        self.dealerHand[1]["image"] = self.cardFace[1]

        if self.deck[1].getValue() > self.deck[0].getValue():
            self.print.insert(INSERT, "\nYou drew a value of " + str(self.deck[1].getValue()) + "\nCard value is high\nYou lose")

        elif self.deck[1].getValue() < self.deck[0].getValue():
            self.print.insert(INSERT, "\nYou drew a value of " + str(self.deck[1].getValue()) + "\nCard value is low\nYou win")

        else:
            self.print.insert(INSERT, "\nYou drew a value of " + str(self.deck[1].getValue()) + "\nCard values are equal\nYou tied")


    def shuffle(self):
        self.high.pack()
        self.low.pack()
        self.shuffle.pack_forget()
        
        self.deal()

        self.print.delete('1.0', END)
        self.print.insert(INSERT, "Initial value is " + str(self.deck[0].getValue()))


    def deal(self):
        random.shuffle(self.deck)

        for i in range(54):
            self.cardFace[i] = (PhotoImage(file = "image/card/" + str(self.deck[i].getImage()) + ".gif"))

        self.dealerHand[0]["image"] = self.cardFace[0]
        self.dealerHand[1]["image"] = self.cardBack
        
BlackJack()
