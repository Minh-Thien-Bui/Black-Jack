#include "Blackjack.h"

void Blackjack::CheckDoubles(shared_ptr<user> player) {
    if (player->hand[0]->rank == player->hand[1]->rank)
    {
        SplitPair(player);
    }
}

void Blackjack::SplitPair(shared_ptr<user> player) {
    ShowHand(player);
    int split;

    cout << "\nYou have a pair of "
        << player->hand[0]->rank << "'s\n"
        << "Enter 1 to split or 0 to keep current hand: ";

    cin >> split;
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    if (split != 0)
    {
        shared_ptr<user> temp_user = InitUser();

        temp_user->hand.push_back(player->hand.back());
        player->hand.pop_back();

        temp_user->hand.push_back(deck.front());
        deck.pop();

        player->hand.push_back(deck.front());
        deck.pop();

        table.insert(table.begin() + 1, temp_user);
        ShowTable();

        CheckDoubles(player);
        CheckDoubles(temp_user);
    }

    else
    {
        ShowTable();
    }
}