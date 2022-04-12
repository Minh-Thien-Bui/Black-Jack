#include "Blackjack.h"

void Blackjack::ShowTable() {
    cout << "\nFull Table:";

    for (shared_ptr<user> it_player : table)
    {
        cout << '\n';

        for (shared_ptr<card> it_card : it_player->hand)
        {
            cout << it_card->title << '\n';
        }
    }
}

void Blackjack::ShowCasino() {
    cout << "\nDealer's hand contains:\n";

    for (shared_ptr<card> it : dealer->hand)
    {
        cout << it->title << '\n';
    }
}

void Blackjack::ShowHand(shared_ptr<user> player) {
    cout << "\nYour hand holds:\n";

    for (shared_ptr<card> it : player->hand)
    {
        cout << it->title << '\n';
    }
}

void Blackjack::EndGame(shared_ptr<user> player) {
    ShowHand(player);
    ShowCasino();

    if (player->exodia && dealer->exodia)
    {
        cout << "\nYou and the Dealer both got Blackjack\n"
            << "It's a Push\n";
    }

    else if (player->exodia && !dealer->exodia)
    {
        cout << "\nYour Blackjack beats Dealer's Hand\n"
            << "You Win\n";
    }

    else if (!player->exodia && dealer->exodia)
    {
        cout << "\nDealer's Blackjack beats Your Hand\n"
            << "The House Wins\n";
    }

    else if (player->score > 21)
    {
        cout << "\nYour Hand Busted\n"
            << "You Lose\n";
    }

    else if (dealer->score > 21)
    {
        cout << "\nDealer's Total: " << dealer->score
            << "\nDealer Busts\n"
            << "You Win\n";
    }

    else if (dealer->score > player->score)
    {
        cout << "\nDealer's Score: " << dealer->score
            << " beats Player's Score: " << player->score
            << "\nThe House Wins\n";
    }

    else if (dealer->score == player->score)
    {
        cout << "\nDealer's Score: " << dealer->score
            << " ties Player's Score: " << player->score
            << "\nIt's a Push\n";
    }

    else
    {
        cout << "\nPlayer's Score: " << player->score
            << " beats Dealer's Score: " << dealer->score
            << "\nYou Win\n";
    }
}