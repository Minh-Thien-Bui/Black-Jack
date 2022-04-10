#include "Blackjack.h"

void Blackjack::AceTest() {
    table.clear();
    dealer = InitCasino();
    vector<shared_ptr<card>> aceHand;

    aceHand.push_back(
        InitCard("Six", "test", 6)
    );
    aceHand.push_back(
        InitCard("Ace", "test", 1)
    );

    while (!deck.empty())
    {
        deck.pop();
    }

    deck.push(InitCard("Two", "test", 2));
    deck.push(InitCard("Nine", "test", 9));
    deck.push(InitCard("Ace", "test", 1));

    shared_ptr<user> acePlayer = InitUser(aceHand);
    dealer->hand = aceHand;

    acePlayer->hand.push_back(
        InitCard("Ace", "test", 1)
    );

    CalculateHand(acePlayer);
    DealersChoice(acePlayer->score);
    EndGame(acePlayer);

    dealer->hand.pop_back();
    DealersChoice(acePlayer->score);
    EndGame(acePlayer);
}

void Blackjack::ExodiaTest() {
    table.clear();
    dealer = InitCasino();
    vector<shared_ptr<card>> perfectHand;

    perfectHand.push_back(
        InitCard("Ace", "Exodia", 1)
    );
    perfectHand.push_back(
        InitCard("King", "Obliterate", 10)
    );

    shared_ptr<user> test_player = InitUser(perfectHand);
    CalculateHand(test_player);
    table.push_back(test_player);

    dealer->hand.push_back(
        InitCard("Ace", "Blue Eyes", 1)
    );
    dealer->hand.push_back(
        InitCard("Six", "White Dragon", 6)
    );

    DealersChoice(test_player->score);
    EndGame(test_player);

    test_player->hand = dealer->hand;
    test_player->hand.push_back(
        InitCard("Four", "Kuriboh", 4)
    );

    dealer->hand = perfectHand;
    CalculateHand(test_player);
    DealersChoice(test_player->score);
    EndGame(test_player);

    test_player->hand = perfectHand;
    CalculateHand(test_player);
    EndGame(test_player);
}

void Blackjack::SimulatorTest() {
    table.clear();
    dealer = InitCasino();

    while (!deck.empty())
    {
        deck.pop();
    }

    vector<shared_ptr<card>> testCards;

    testCards.push_back(InitCard("Two", "test", 2));
    testCards.push_back(InitCard("Two", "test", 2));
    testCards.push_back(InitCard("Ten", "test", 10));
    testCards.push_back(InitCard("Ten", "test", 10));

    for (shared_ptr<card> it : testCards)
    {
        deck.push(it);
    }

    shared_ptr<user> simPlayer = InitUser();

    simPlayer->hand.push_back(
        InitCard("Ace", "test", 1)
    );
    simPlayer->hand.push_back(
        InitCard("Six", "test", 6)
    );

    ShowHand(simPlayer);

    dealer->hand.push_back(
        InitCard("Two", "test", 2)
    );
    dealer->hand.push_back(
        InitCard("Ace", "test", 1)
    );

    cout << "\nDealer's hand contains:\n"
        << dealer->hand[0]->title;

    cout << "\n\nFacedown Cards:\n"
        << dealer->hand[1]->title;

    for (shared_ptr<card> it : testCards)
    {
        cout << '\n' << it->title;
    }

    CountingCards(simPlayer);
}

void Blackjack::TestPairs() {
    shared_ptr<user> temp_user = InitUser();
    table.clear();

    while (!deck.empty())
    {
        deck.pop();
    }

    for (string suit : suits_list)
    {
        deck.push(InitCard("Ace", suit, 1));
    }

    for (string suit : suits_list)
    {
        deck.push(InitCard("King", suit, 10));
    }

    for (size_t i = 0; i < 2; i++)
    {
        temp_user->hand.push_back(deck.front());
        deck.pop();
    }

    table.push_back(temp_user);
    ShowTable();
    CheckDoubles(temp_user);
}