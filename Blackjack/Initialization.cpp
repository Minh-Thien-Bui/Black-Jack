#include "Blackjack.h"

Blackjack::Blackjack() {
    map<string, int> card_dict;

    card_dict["Ace"] = 1;
    card_dict["Two"] = 2;
    card_dict["Three"] = 3;
    card_dict["Four"] = 4;
    card_dict["Five"] = 5;
    card_dict["Six"] = 6;
    card_dict["Seven"] = 7;
    card_dict["Eight"] = 8;
    card_dict["Nine"] = 9;
    card_dict["Ten"] = 10;
    card_dict["Jack"] = 10;
    card_dict["Queen"] = 10;
    card_dict["King"] = 10;

    for (auto rank_value : card_dict)
    {
        for (string suit : suits_list)
        {
            shared_ptr<card> temp = InitCard(
                rank_value.first, suit, rank_value.second
            );

            card_list.push_back(temp);
        }
    }
}

Blackjack::~Blackjack() {
    // deconstructor
}

void Blackjack::InitDeck() {
    while (!deck.empty())
    {
        deck.pop();
    }

    auto rng = default_random_engine(time(NULL));
    shuffle(begin(card_list), end(card_list), rng);

    for (shared_ptr<card> it : card_list)
    {
        deck.push(it);
    }
}

shared_ptr<card> Blackjack::InitCard(string rank, string suit, int value) {
    shared_ptr<card> ret(new card);

    ret->rank = rank;
    ret->suit = suit;
    ret->title = rank + " of " + suit;
    ret->value = value;

    return ret;
}

shared_ptr<user> Blackjack::InitUser() {
    shared_ptr<user> ret(new user);
    ret->exodia = false;
    return ret;
}

shared_ptr<user> Blackjack::InitUser(vector<shared_ptr<card>> hand) {
    shared_ptr<user> ret(InitUser());
    ret->hand = hand;
    return ret;
}

shared_ptr<casino> Blackjack::InitCasino() {
    shared_ptr<casino> ret(new casino);
    ret->exodia = false;
    ret->soft17 = false;
    return ret;
}