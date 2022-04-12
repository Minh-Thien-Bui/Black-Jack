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

aceSpades = Card()
twoSpades = Card(2, 2)
threeSpades = Card(3, 3)
fourSpades = Card(4, 4)
fiveSpades = Card(5, 5)
sixSpades = Card(6, 6)
sevenSpades = Card(7, 7)
eightSpades = Card(8, 8)
nineSpades = Card(9, 9)
tenSpades = Card(10, 10)
jackSpades = Card(10, 11)
queenSpades = Card(10, 12)
kingSpades = Card(10, 13)
aceHearts = Card(1, 14)
twoHearts = Card(2, 15)
threeHearts = Card(3, 16)
fourHearts = Card(4, 17)
fiveHearts = Card(5, 18)
sixHearts = Card(6, 19)
sevenHearts = Card(7, 20)
eightHearts = Card(8, 21)
nineHearts = Card(9, 22)
tenHearts = Card(10, 23)
jackHearts = Card(10, 24)
queenHearts = Card(10, 25)
kingHearts = Card(10, 26)
aceDiamonds = Card(1, 27)
twoDiamonds = Card(2, 28)
threeDiamonds = Card(3, 29)
fourDiamonds = Card(4, 30)
fiveDiamonds = Card(5, 31)
sixDiamonds = Card(6, 32)
sevenDiamonds = Card(7, 33)
eightDiamonds = Card(8, 34)
nineDiamonds = Card(9, 35)
tenDiamonds = Card(10, 36)
jackDiamonds = Card(10, 37)
queenDiamonds = Card(10, 38)
kingDiamonds = Card(10, 39)
aceClubs = Card(1, 40)
twoClubs = Card(2, 41)
threeClubs = Card(3, 42)
fourClubs = Card(4, 43)
fiveClubs = Card(5, 44)
sixClubs = Card(6, 45)
sevenClubs = Card(7, 46)
eightClubs = Card(8, 47)
nineClubs = Card(9, 48)
tenClubs = Card(10, 49)
jackClubs = Card(10, 50)
queenClubs = Card(10, 51)
kingClubs = Card(10, 52)
jokerBlack = Card(0, 53)
jokerRed = Card(0, 54)

deck = [
    aceSpades,
    twoSpades,
    threeSpades,
    fourSpades,
    fiveSpades,
    sixSpades,
    sevenSpades,
    eightSpades,
    nineSpades,
    tenSpades,
    jackSpades,
    queenSpades,
    kingSpades,
    aceHearts,
    twoHearts,
    threeHearts,
    fourHearts,
    fiveHearts,
    sixHearts,
    sevenHearts,
    eightHearts,
    nineHearts,
    tenHearts,
    jackHearts,
    queenHearts,
    kingHearts,
    aceDiamonds,
    twoDiamonds,
    threeDiamonds,
    fourDiamonds,
    fiveDiamonds,
    sixDiamonds,
    sevenDiamonds,
    eightDiamonds,
    nineDiamonds,
    tenDiamonds,
    jackDiamonds,
    queenDiamonds,
    kingDiamonds,
    aceClubs,
    twoClubs,
    threeClubs,
    fourClubs,
    fiveClubs,
    sixClubs,
    sevenClubs,
    eightClubs,
    nineClubs,
    tenClubs,
    jackClubs,
    queenClubs,
    kingClubs,
    jokerBlack,
    jokerRed
]

def blackJack():
    random.shuffle(deck)
    
    dealer = [deck[0], deck[1]]
    dealerValue = dealer[0].getValue() + dealer[1].getValue()
    dealerBust = 0
    
    player = [deck[2], deck[3]]
    playerValue = player[0].getValue() + player[1].getValue()
    playerBust = 0
    cardDraw = 3
    
    print("Dealer drew", dealer[0].getValue())
    print("You drew", player[0].getValue())
    print("You drew", player[1].getValue())
    
    if player[0].getValue() == 0 or player[1].getValue() == 0:
        print("You drew the Joker, you lose HAHAHAHA")
        
    elif playerValue == 21 and dealerValue != 21:
        print("You got Blackjack, Winner Winner Chicken Dinner")
    
    print("Your value is", playerValue)
    
    hit = eval(input("Enter 1 to Hit or 0 to Stay: "))
    
    while hit == 1:
        cardDraw += 1
        player.append(deck[cardDraw])
        print("You drew", player[len(player) - 1].getValue())
        
        if player[len(player) - 1].getValue() == 0:
            print("You drew the Joker, you lose HAHAHAHA")
        
        playerValue += player[len(player) - 1].getValue()
        print("Your value is", playerValue)
        
        if playerValue == 21:
            break
        
        elif playerValue > 21:
            print("You busted, you lose")
            playerBust = 1
            break
        
        hit = eval(input("Enter 1 to Hit or 0 to Stay: "))
    
    if playerBust == 0:
        print("Dealer holds", dealer[0].getValue())
        print("Dealer holds", dealer[1].getValue())
        print("Dealer's value is", dealerValue)

        if dealerValue > playerValue:
            print("Dealer's hand wins, you lose")
            
        else:
            while dealerValue < 17 and dealerValue < playerValue:
                cardDraw += 1
                dealer.append(deck[cardDraw])
                print("Dealer drew", dealer[len(dealer) - 1].getValue())

                dealerValue += dealer[len(dealer) - 1].getValue()
                print("Dealer's value is", dealerValue)

                if dealerValue > 21:
                    print("Dealer busted, you win")
                    dealerBust = 1
                    break

            if dealerBust == 0:
                if playerValue > dealerValue:
                    print("Your value is", playerValue, "Dealer's value is", dealerValue)
                    print("Your hand wins")

                elif dealerValue > playerValue:
                    print("Dealer's value is", dealerValue, "Your value is", playerValue)
                    print("Dealer's hand wins, you lose")

                else:
                    print("Dealer's value is", dealerValue, "Your value is", playerValue)
                    print("Dealer's hand equals yours, you tied")
    
blackJack()
