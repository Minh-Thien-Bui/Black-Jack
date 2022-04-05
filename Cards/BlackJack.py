from tkinter import *
import random

class Card:
    def __init__(self, title = "Ace of Spades", value = 1):
        self.__title = title
        self.__value = value

    def getTitle(self):
        return self.__title

    def getValue(self):
        return self.__value

    def setTitle(self, title):
        self.__title = title
        
    def setValue(self, value):
        self.__value = value
        

class FullDeck:
    def __init__(self, cardList):
        self.__cardList = cardList
        self.__cardCount = -1

    def getCard(self, index):
        return self.__cardList[index]

    def getLength(self):
        return len(self.__cardList)

    def shuffleDeck(self):
        random.shuffle(self.__cardList)

    def drawCard(self):
        self.__cardCount += 1
        return self.__cardList[self.__cardCount]


def sumHand(hand):
    sumTotal = 0
    
    for i in range(len(hand)):
        sumTotal += hand[i].getValue()

    return sumTotal


def aces(hand):
    for i in range(len(hand)):
        if "Ace" in hand[i].getTitle():
            if sumHand(hand) < 12:
                hand[i].setValue(11)
                
            else:
                hand[i].setValue(1)


def hardSeventeen(hand):
    aces(hand)
    
    if sumHand(hand) < 17:
        hardCap = False

    else:
        hardCap = True
        
        for i in range(len(hand)):
            if hand[i].getValue == 11:
                hardCap = False

    return hardCap


class BlackJack():
    def __init__(self):
        self.window = Tk()
        self.window.title("Blackjack")
        
        self.aceSpades = Card()
        self.twoSpades = Card("Two of Spades", 2)
        self.threeSpades = Card("Three of Spades", 3)
        self.fourSpades = Card("Four of Spades", 4)
        self.fiveSpades = Card("Five of Spades", 5)
        self.sixSpades = Card("Six of Spades", 6)
        self.sevenSpades = Card("Seven of Spades", 7)
        self.eightSpades = Card("Eight of Spades", 8)
        self.nineSpades = Card("Nine of Spades", 9)
        self.tenSpades = Card("Ten of Spades", 10)
        self.jackSpades = Card("Jack of Spades", 10)
        self.queenSpades = Card("Queen of Spades", 10)
        self.kingSpades = Card("King of Spades", 10)
        self.aceHearts = Card("Ace of Hearts")
        self.twoHearts = Card("Two of Hearts", 2)
        self.threeHearts = Card("Three of Hearts", 3)
        self.fourHearts = Card("Four of Hearts", 4)
        self.fiveHearts = Card("Five of Hearts", 5)
        self.sixHearts = Card("Six of Hearts", 6)
        self.sevenHearts = Card("Seven of Hearts", 7)
        self.eightHearts = Card("Eight of Hearts", 8)
        self.nineHearts = Card("Nine of Hearts", 9)
        self.tenHearts = Card("Ten of Hearts", 10)
        self.jackHearts = Card("Jack of Hearts", 10)
        self.queenHearts = Card("Queen of Hearts", 10)
        self.kingHearts = Card("King of Hearts", 10)
        self.aceDiamonds = Card("Ace of Diamonds")
        self.twoDiamonds = Card("Two of Diamonds", 2)
        self.threeDiamonds = Card("Three of Diamonds", 3)
        self.fourDiamonds = Card("Four of Diamonds", 4)
        self.fiveDiamonds = Card("Five of Diamonds", 5)
        self.sixDiamonds = Card("Six of Diamonds", 6)
        self.sevenDiamonds = Card("Seven of Diamonds", 7)
        self.eightDiamonds = Card("Eight of Diamonds", 8)
        self.nineDiamonds = Card("Nine of Diamonds", 9)
        self.tenDiamonds = Card("Ten of Diamonds", 10)
        self.jackDiamonds = Card("Jack of Diamonds", 10)
        self.queenDiamonds = Card("Queen of Diamonds", 10)
        self.kingDiamonds = Card("King of Diamonds", 10)
        self.aceClubs = Card("Ace of Clubs")
        self.twoClubs = Card("Two of Clubs", 2)
        self.threeClubs = Card("Three of Clubs", 3)
        self.fourClubs = Card("Four of Clubs", 4)
        self.fiveClubs = Card("Five of Clubs", 5)
        self.sixClubs = Card("Six of Clubs", 6)
        self.sevenClubs = Card("Seven of Clubs", 7)
        self.eightClubs = Card("Eight of Clubs", 8)
        self.nineClubs = Card("Nine of Clubs", 9)
        self.tenClubs = Card("Ten of Clubs", 10)
        self.jackClubs = Card("Jack of Clubs", 10)
        self.queenClubs = Card("Queen of Clubs", 10)
        self.kingClubs = Card("King of Clubs", 10)
        self.jokerBlack = Card("Black Joker", 0)
        self.jokerRed = Card("Red Joker", 0)

        self.deck = FullDeck([
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
        ])
        
        self.cardFace = {"cardback" : PhotoImage(file = "image/card/b1fv.gif")}

        for i in range(self.deck.getLength()):
            self.cardFace[self.deck.getCard(i)] = PhotoImage(file = "image/card/" + str(i + 1) + ".gif")

        self.deck.shuffleDeck()

        self.dealerFrame = Frame(self.window)
        self.dealerFrame.pack()

        self.dealerHand = []

        self.dealerLabel = [
            Label(self.dealerFrame, image = self.cardFace[self.deck.getCard(0)]),
            Label(self.dealerFrame, image = self.cardFace["cardback"])
        ]
        
        for i in range(2):
            self.dealerHand.append(self.deck.drawCard())
            self.dealerLabel[i].pack(side = LEFT)
        
        self.playerFrame = Frame(self.window)
        self.playerFrame.pack()

        self.playerHand = []
        self.playerLabel = []

        for i in range(2):
            self.playerHand.append(self.deck.drawCard())
            self.playerLabel.append(Label(self.playerFrame, image = self.cardFace[self.playerHand[i]]))
            self.playerLabel[i].pack(side = LEFT)

        aces(self.dealerHand)
        aces(self.playerHand)

        buttonFrame = Frame(self.window)
        buttonFrame.pack()
        
        self.hit = Button(buttonFrame, text = "Hit", command = self.hit)
        self.stay = Button(buttonFrame, text = "Stay", command = self.stay)
        self.shuffle = Button(buttonFrame, text = "Shuffle", command = self.shuffle)

        self.hit.pack()
        self.stay.pack()
        
        textFrame = Frame(self.window)
        textFrame.pack()

        self.print = Text(textFrame)
        self.print.insert(INSERT, "Dealer drew the " + self.dealerHand[0].getTitle() + "\nDealer's known value is " + str(self.dealerHand[0].getValue()) + "\n\nPlayer drew the " + self.playerHand[0].getTitle() + " and the " + self.playerHand[1].getTitle() + "\nPlayer's initial value is " + str(sumHand(self.playerHand)))
        self.print.pack()
        
        if sumHand(self.playerHand) == 21:
            self.gameOver()
        
        self.window.mainloop()


    def hit(self):
        self.playerHand.append(self.deck.drawCard())

        self.playerLabel.append(Label(self.playerFrame, image = self.cardFace[self.playerHand[-1]]))
        self.playerLabel[-1].pack(side = LEFT)

        aces(self.playerHand)

        self.print.insert(INSERT, "\n\nPlayer drew the " + self.playerHand[-1].getTitle() + "\nPlayer's current value is " + str(sumHand(self.playerHand)))

        if sumHand(self.playerHand) > 21:
            self.gameOver()

        elif sumHand(self.playerHand) == 21:
            self.hit.pack_forget()


    def stay(self):
        if sumHand(self.dealerHand) >= sumHand(self.playerHand):
            self.gameOver()

        elif hardSeventeen(self.dealerHand):
            self.gameOver()

        else:
            self.houseDraws()

        
    def houseDraws(self):
        self.dealerHand.append(self.deck.drawCard())

        self.dealerLabel.append(Label(self.dealerFrame, image = self.cardFace[self.dealerHand[-1]]))
        self.dealerLabel[-1].pack(side = LEFT)

        aces(self.dealerHand)

        if sumHand(self.dealerHand) >= sumHand(self.playerHand):
            self.gameOver()

        elif hardSeventeen(self.dealerHand):
            self.gameOver()

        else:
            self.houseDraws()
                

    def gameOver(self):
        self.hit.pack_forget()
        self.stay.pack_forget()
        self.shuffle.pack()

        self.dealerLabel[1]["image"] = self.cardFace[self.dealerHand[1]]

        self.print.insert(INSERT, "\n\nDealer's hand contains:")

        for i in range(len(self.dealerHand)):
            self.print.insert(INSERT, "\n" + self.dealerHand[i].getTitle())
        
        self.print.insert(INSERT, "\n\nDealer's final value is " + str(sumHand(self.dealerHand)))

        if sumHand(self.playerHand) == 21 and sumHand(self.dealerHand) == 21:
            self.print.insert(INSERT, "\n\nPlayer and Dealer both hit Blackjack\nYou Tied")

        elif sumHand(self.playerHand) == 21:
            self.print.insert(INSERT, "\n\nPlayer hit Blackjack\nYou Won")

        elif sumHand(self.dealerHand) == 21:
            self.print.insert(INSERT, "\n\nDealer hit Blackjack\nYou Lost")

        elif sumHand(self.playerHand) > 21:
            self.print.insert(INSERT, "\n\nPlayer's hand busted\nYou Lost")

        elif sumHand(self.dealerHand) > 21:
            self.print.insert(INSERT, "\n\nDealer's hand busted\nYou Won")
            
        elif sumHand(self.dealerHand) > sumHand(self.playerHand):
            self.print.insert(INSERT, "\n\nDealer's hand wins\nYou Lost")

        elif sumHand(self.dealerHand) < sumHand(self.playerHand):
            self.print.insert(INSERT, "\n\nPlayer's hand wins\nYou Won")

        else:
            self.print.insert(INSERT, "\n\nPlayer's hand equals Dealer's hand\nYou Tied")


    def shuffle(self):
        self.window.destroy()
        BlackJack()

BlackJack()
