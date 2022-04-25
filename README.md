# Project: Blackjack

<hr>

### Data Structure Implementation
Vectors are used to contain both the player's and dealer's hands.  Their hands, along with other game data like the hand's value, are nested in structures I created to represent the user and computer opponent.  I also wrote a simple structure for cards to contain the data of all 52 cards in a standard deck.  The deck itself is implemented as a queue because that makes it easier to draw cards from the top of the deck.  For simulations, the pool of facedown cards is implemented as a vector because it's easy to iterate through.  Vectors were also used to hold the theoretical outcomes of simulated card draws for either the player or dealer.  In case the player chooses to split a pair of doubles, a vector is implemented to contain all current hands in the game.

### Compilation Instructions
Go inside the solution folder and open the Blackjack.sln file with the Microsoft Visual Studio compiler.  If you don't have Visual Studio, you can download it here: https://visualstudio.microsoft.com/vs/features/cplusplus/

Once the Visual Studio IDE is installed on your computer, you still have to install the C++ package in order to compile the code.
