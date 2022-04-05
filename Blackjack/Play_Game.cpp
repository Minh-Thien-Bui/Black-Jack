#include "Blackjack.h"

int main()
{
	Blackjack cardgame;
	int play_again = 1;

	cout << fixed;
	cout.precision(2);

	cout << "Welcome to Blackjack\n";

	//cardgame.TestPairs();

	while (play_again)
	{
		cardgame.InitGame();

		cout << "\nEnter 1 if you'd like to play again or 0 to quit: ";
		cin >> play_again;
	}

	cout << "\nGame Over\n";
	return 0;
}