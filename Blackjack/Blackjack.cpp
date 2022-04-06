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

    string suits_list[4] = {
        "Clubs",
        "Diamonds",
        "Hearts",
        "Spades"
    };

    for (auto rank_value : card_dict)
    {
        for (string suit : suits_list)
        {
            shared_ptr<card> temp = InitCard(rank_value.first, suit, rank_value.second);
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
    
    for (shared_ptr<user> it : table)
    {
        EndGame(it);
    }
}

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

void Blackjack::ShowHand(shared_ptr<user> player) {
    cout << "\nYour hand holds:\n";

    for (shared_ptr<card> it : player->hand)
    {
        cout << it->title << '\n';
    }
}

void Blackjack::CheckDoubles(shared_ptr<user> player) {
    ShowTable();

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

        CheckDoubles(player);
        CheckDoubles(temp_user);
    }
}

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

void Blackjack::EndGame(shared_ptr<user> player) {
    ShowTable();
    ShowHand(player);

    cout << "\nDealer's hand contains:\n";

    for (shared_ptr<card> it : dealer->hand)
    {
        cout << it->title << '\n';
    }

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

void Blackjack::CountingCards(shared_ptr<user> player) {
    queue<shared_ptr<card>> clone_deck(deck);
    vector<shared_ptr<card>> unknown_cards;

    int card_counter[MAX + 1] = {};
    clone_deck.push(dealer->hand[1]);

    while (!clone_deck.empty())
    {
        shared_ptr<user> sim_player = InitUser(player->hand);
        sim_player->hand.push_back(clone_deck.front());

        unknown_cards.push_back(clone_deck.front());
        clone_deck.pop();

        int index = HashCard(sim_player);
        card_counter[index]++;
    }

    cout << "\n\nProbability of Next Draw:\n";

    for (size_t i = 0; i < size(card_counter); i++)
    {
        if (card_counter[i] > 0)
        {
            float chance = static_cast<float> (card_counter[i])
                / static_cast<float> (unknown_cards.size()) * 100;

            if (i < MAX)
            {
                int test_score = i + OFFSET;
                float win_rate = RunSimulations(unknown_cards, test_score);

                cout << test_score << ": "
                    << chance << "% Draw Chance\t"
                    << win_rate << "% Win Rate\n";
            }

            else
            {
                cout << "Bust: "
                    << chance << "% Chance of Losing\n";
            }
        }
    }

    RunSimulations(unknown_cards, player);
}

int Blackjack::HashCard(shared_ptr<user> sim_player) {
    CalculateHand(sim_player);
    int hash = sim_player->score - OFFSET;

    if (hash > MAX)
    {
        hash = MAX;
    }

    return hash;
}

void Blackjack::RunSimulations(vector<shared_ptr<card>> unknown_cards, shared_ptr<user> player) {
    float hit_wins = 0;
    float stay_wins = 0;
    CalculateHand(player);

    for (size_t i = 0; i < SIMS; i++)
    {
        auto rng = default_random_engine(i);
        shuffle(begin(unknown_cards), end(unknown_cards), rng);

        hit_wins += SimulateGames(unknown_cards, player);
        stay_wins += SimulateGames(unknown_cards, player->score);
    }

    float hit_odds = hit_wins / SIMS * 100;
    float stay_odds = stay_wins / SIMS * 100;

    cout << "\nOdds of Winning if You Hit: "
        << hit_odds << "%\n"
        << "Odds of Winning if You Stay: "
        << stay_odds << "%\n";
}

float Blackjack::RunSimulations(vector<shared_ptr<card>> unknown_cards, int test_score) {
    float wins = 0;

    for (size_t i = 0; i < SIMS; i++)
    {
        auto rng = default_random_engine(i);
        shuffle(begin(unknown_cards), end(unknown_cards), rng);
        wins += SimulateGames(unknown_cards, test_score);
    }

    return wins / SIMS * 100;
}

float Blackjack::SimulateGames(vector<shared_ptr<card>> unknown_cards, shared_ptr<user> player) {
    shared_ptr<user> sim_player = InitUser(player->hand);

    sim_player->hand.push_back(unknown_cards.back());
    unknown_cards.pop_back();

    CalculateHand(sim_player);

    if (sim_player->score > 21)
    {
        return 0;
    }

    else
    {
        return SimulateGames(unknown_cards, sim_player->score);
    }
}

float Blackjack::SimulateGames(vector<shared_ptr<card>> unknown_cards, int player_total) {
    shared_ptr<casino> sim_dealer = InitCasino();

    sim_dealer->hand.push_back(dealer->hand[0]);
    sim_dealer->hand.push_back(unknown_cards.back());
    unknown_cards.pop_back();

    CalculateHand(sim_dealer);

    while (sim_dealer->score < player_total && (sim_dealer->score < 17 || sim_dealer->soft17))
    {
        sim_dealer->hand.push_back(unknown_cards.back());
        unknown_cards.pop_back();
        CalculateHand(sim_dealer);
    }

    if (sim_dealer->score > 21  || sim_dealer->score < player_total)
    {
        return 1;
    }

    else
    {
        return 0;
    }
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

void Blackjack::TestPairs() {
    shared_ptr<user> temp_user = InitUser();
    table.clear();

    while (!deck.empty())
    {
        deck.pop();
    }

    string suits_list[4] = 
    {
        "Clubs",
        "Diamonds",
        "Hearts",
        "Spades"
    };

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
    CheckDoubles(temp_user);
    ShowTable();
}