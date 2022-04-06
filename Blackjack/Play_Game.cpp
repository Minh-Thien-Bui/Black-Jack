#include "Blackjack.h"

int main()
{
	Blackjack cardgame;

	cout << fixed;
	cout.precision(2);

	cout << "Welcome to Blackjack\n";

	//cardgame.AceTest();
	//cardgame.ExodiaTest();
	//cardgame.TestPairs();

	cardgame.GameStart();

	cout << "\nGame Over\n";
	return 0;
}