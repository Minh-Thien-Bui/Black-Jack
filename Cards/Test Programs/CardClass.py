from tkinter import *
import random

class Card:
    def __init__(self, value = 1, image = PhotoImage(file = "image/card/1.gif")):
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





def main():
    window = Tk()
    window.title("Blackjack")

    self.aceSpades = Card()
    self.twoSpades = Card(2, PhotoImage(file = "image/card/2.gif"))
    self.threeSpades = Card(3, PhotoImage(file = "image/card/3.gif"))
    self.fourSpades = Card(4, PhotoImage(file = "image/card/4.gif"))
    self.fiveSpades = Card(5, PhotoImage(file = "image/card/5.gif"))
    self.sixSpades = Card(6, PhotoImage(file = "image/card/6.gif"))
    self.sevenSpades = Card(7, PhotoImage(file = "image/card/7.gif"))
    self.eightSpades = Card(8, PhotoImage(file = "image/card/8.gif"))
    self.nineSpades = Card(9, PhotoImage(file = "image/card/9.gif"))
    self.tenSpades = Card(10, PhotoImage(file = "image/card/10.gif"))
    self.jackSpades = Card(10, PhotoImage(file = "image/card/11.gif"))
    self.queenSpades = Card(10, PhotoImage(file = "image/card/12.gif"))
    self.kingSpades = Card(10, PhotoImage(file = "image/card/13.gif"))
    self.aceHearts = Card(1, PhotoImage(file = "image/card/14.gif"))
    self.twoHearts = Card(2, PhotoImage(file = "image/card/15.gif"))
    self.threeHearts = Card(3, PhotoImage(file = "image/card/16.gif"))
    self.fourHearts = Card(4, PhotoImage(file = "image/card/17.gif"))
    self.fiveHearts = Card(5, PhotoImage(file = "image/card/18.gif"))
    self.sixHearts = Card(6, PhotoImage(file = "image/card/19.gif"))
    self.sevenHearts = Card(7, PhotoImage(file = "image/card/20.gif"))
    self.eightHearts = Card(8, PhotoImage(file = "image/card/21.gif"))
    self.nineHearts = Card(9, PhotoImage(file = "image/card/22.gif"))
    self.tenHearts = Card(10, PhotoImage(file = "image/card/23.gif"))
    self.jackHearts = Card(10, PhotoImage(file = "image/card/24.gif"))
    self.queenHearts = Card(10, PhotoImage(file = "image/card/25.gif"))
    self.kingHearts = Card(10, PhotoImage(file = "image/card/26.gif"))
    self.aceDiamonds = Card(1, PhotoImage(file = "image/card/27.gif"))
    self.twoDiamonds = Card(2, PhotoImage(file = "image/card/28.gif"))
    self.threeDiamonds = Card(3, PhotoImage(file = "image/card/29.gif"))
    self.fourDiamonds = Card(4, PhotoImage(file = "image/card/30.gif"))
    self.fiveDiamonds = Card(5, PhotoImage(file = "image/card/31.gif"))
    self.sixDiamonds = Card(6, PhotoImage(file = "image/card/32.gif"))
    self.sevenDiamonds = Card(7, PhotoImage(file = "image/card/33.gif"))
    self.eightDiamonds = Card(8, PhotoImage(file = "image/card/34.gif"))
    self.nineDiamonds = Card(9, PhotoImage(file = "image/card/35.gif"))
    self.tenDiamonds = Card(10, PhotoImage(file = "image/card/36.gif"))
    self.jackDiamonds = Card(10, PhotoImage(file = "image/card/37.gif"))
    self.queenDiamonds = Card(10, PhotoImage(file = "image/card/38.gif"))
    self.kingDiamonds = Card(10, PhotoImage(file = "image/card/39.gif"))
    self.aceClubs = Card(1, PhotoImage(file = "image/card/40.gif"))
    self.twoClubs = Card(2, PhotoImage(file = "image/card/41.gif"))
    self.threeClubs = Card(3, PhotoImage(file = "image/card/42.gif"))
    self.fourClubs = Card(4, PhotoImage(file = "image/card/43.gif"))
    self.fiveClubs = Card(5, PhotoImage(file = "image/card/44.gif"))
    self.sixClubs = Card(6, PhotoImage(file = "image/card/45.gif"))
    self.sevenClubs = Card(7, PhotoImage(file = "image/card/46.gif"))
    self.eightClubs = Card(8, PhotoImage(file = "image/card/47.gif"))
    self.nineClubs = Card(9, PhotoImage(file = "image/card/48.gif"))
    self.tenClubs = Card(10, PhotoImage(file = "image/card/49.gif"))
    self.jackClubs = Card(10, PhotoImage(file = "image/card/50.gif"))
    self.queenClubs = Card(10, PhotoImage(file = "image/card/51.gif"))
    self.kingClubs = Card(10, PhotoImage(file = "image/card/52.gif"))
    self.jokerBlack = Card(0, PhotoImage(file = "image/card/53.gif"))
    self.jokerRed = Card(0, PhotoImage(file = "image/card/54.gif"))
    
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

    frame = Frame(window)
    frame.pack()
    
    self.cardLabel = []
    for i in range(7):
        self.cardLabel.append(Label(frame, image = deck[i].getImage()))
        self.cardLabel[i].pack(side = LEFT)

    Button(window, text = "Hit", command = hit).pack()

    Button(window, text = "Stay", command = stay).pack()

    window.mainloop()

def hit():
    print("You Drew")

def stay():
    print("You Stayed")

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


main()
