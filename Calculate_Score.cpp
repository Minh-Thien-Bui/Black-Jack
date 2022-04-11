#include "Blackjack.h"

void Blackjack::CalculateHand(shared_ptr<user> yugi) {
    int hand_sum = 0;
    bool aces = false;

    for (shared_ptr<card> it : yugi->hand)
    {
        hand_sum += it->value;

        if (it->rank == "Ace")
        {
            aces = true;
        }
    }

    if (aces && hand_sum < 12)
    {
        hand_sum += 10;
    }

    if (hand_sum == 21)
    {
        if (yugi->hand.size() == 2)
        {
            yugi->exodia = true;
        }

        else
        {
            yugi->exodia = false;
        }
    }

    yugi->score = hand_sum;
}

void Blackjack::CalculateHand(shared_ptr<casino> kaiba) {
    int hand_sum = 0;
    bool aces = false;

    for (shared_ptr<card> it : kaiba->hand)
    {
        hand_sum += it->value;

        if (it->rank == "Ace")
        {
            aces = true;
        }
    }

    if (aces && hand_sum < 12)
    {
        hand_sum += 10;

        if (hand_sum >= 17)
        {
            kaiba->soft17 = true;
        }
    }

    else
    {
        kaiba->soft17 = false;
    }

    if (hand_sum == 21)
    {
        if (kaiba->hand.size() == 2)
        {
            kaiba->exodia = true;
        }

        else
        {
            kaiba->exodia = false;
        }
    }

    kaiba->score = hand_sum;
}