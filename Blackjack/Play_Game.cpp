#include "Blackjack.h"

void Blackjack::GameStart() {
    int play_again = 1;

    while (play_again)
    {
        InitGame();

        cout << "\nEnter 1 if you'd like to play again or 0 to quit: ";
        cin >> play_again;
    }
}

void Blackjack::InitGame() {
    if (deck.size() < MIN)
    {
        InitDeck();
    }

    shared_ptr<user> player = InitUser();
    dealer = InitCasino();
    table.clear();

    for (size_t i = 0; i < 2; i++)
    {
        player->hand.push_back(deck.front());
        deck.pop();

        dealer->hand.push_back(deck.front());
        deck.pop();
    }

    table.push_back(player);
    ShowTable();

    CheckDoubles(player);
    int high_score = 0;

    for (shared_ptr<user> it : table)
    {
        StayOrBust(it);

        if (it->score > high_score && it->score < 22)
        {
            high_score = it->score;
        }
    }
    
    DealersChoice(high_score);
    ShowTable();
    
    for (shared_ptr<user> it : table)
    {
        EndGame(it);
    }
}

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

        table.push_back(temp_user);

        ShowTable();
        CheckDoubles(player);
        CheckDoubles(temp_user);
    }

    else
    {
        ShowTable();
    }
}

void Blackjack::StayOrBust(shared_ptr<user> player) {
    cout << "\nDealer's hand contains:\n"
        << dealer->hand[0]->title << '\n';

    ShowHand(player);
    CalculateHand(player);
    cout << "Total Score: " << player->score;

    if (player->score > 21)
    {
        cout << "\n\nYou went over 21\n";
        return;
    }

    else if (player->score == 21)
    {
        if (player->exodia)
        {
            cout << "\n\nYou got Blackjack\n";
        }

        else
        {
            cout << "\n\nYou hit 21\n";
        }
        
        return;
    }

    CountingCards(player);
    int hit_stay;

    cout << "\nEnter 1 to Hit or 0 to Stay: ";
    cin >> hit_stay;
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    if (hit_stay != 0)
    {
        Hit(player);
    }
}

void Blackjack::Hit(shared_ptr<user> player) {
    player->hand.push_back(deck.front());
    deck.pop();
    StayOrBust(player);
}

void Blackjack::DealersChoice(int player_total) {
    CalculateHand(dealer);

    if (dealer->exodia)
    {
        return;
    }

    for (shared_ptr<user> player : table)
    {
        if (player->exodia)
        {
            return;
        }
    }

    while (dealer->score < player_total)
    {
        if (dealer->score >= 17 && !dealer->soft17)
        {
            return;
        }

        dealer->hand.push_back(deck.front());
        deck.pop();
        CalculateHand(dealer);
    }
}