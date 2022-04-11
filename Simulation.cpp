#include "Blackjack.h"

void Blackjack::CountingCards(shared_ptr<user> player) {
    queue<shared_ptr<card>> clone_deck(deck);
    vector<shared_ptr<card>> unknown_cards;

    vector<shared_ptr<card>> card_buckets[MAX + 1];
    clone_deck.push(dealer->hand[1]);

    while (!clone_deck.empty())
    {
        shared_ptr<user> sim_player = InitUser(player->hand);
        sim_player->hand.push_back(clone_deck.front());
        unknown_cards.push_back(clone_deck.front());

        int index = HashCard(sim_player);
        card_buckets[index].push_back(clone_deck.front());
        clone_deck.pop();
    }

    cout << "\n\nProbability of Next Draw:\n";

    for (size_t i = 0; i <= MAX; i++)
    {
        if (card_buckets[i].size() > 0)
        {
            float chance = static_cast<float> (card_buckets[i].size())
                / static_cast<float> (unknown_cards.size()) * 100;

            if (i < MAX)
            {
                int test_score = i + OFFSET;
                float win_rate = 0;

                for (shared_ptr<card> bucket : card_buckets[i])
                {
                    win_rate += RunSimulations(unknown_cards, bucket, test_score);
                }

                float wining_odds = win_rate / card_buckets[i].size();

                cout << test_score << ": "
                    << chance << "% Draw Chance\t"
                    << wining_odds << "% Win Rate\n";
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

float Blackjack::RunSimulations(vector<shared_ptr<card>> unknown_cards, shared_ptr<card> card_drawn, int test_score) {
    float wins = 0;

    for (auto it = unknown_cards.begin(); it != unknown_cards.end(); it++)
    {
        if (it->get()->title == card_drawn->title)
        {
            unknown_cards.erase(it);
            break;
        }
    }

    for (size_t i = 0; i < SIMS; i++)
    {
        int seed = time(NULL) * (i + 1);
        auto rng = default_random_engine(seed);

        shuffle(begin(unknown_cards), end(unknown_cards), rng);
        wins += SimulateGames(unknown_cards, test_score);
    }

    return wins / SIMS * 100;
}

void Blackjack::RunSimulations(vector<shared_ptr<card>> unknown_cards, shared_ptr<user> player) {
    float hit_wins = 0;
    float stay_wins = 0;
    CalculateHand(player);

    for (size_t i = 0; i < SIMS * 10; i++)
    {
        int seed = time(NULL) * (i + 1);
        auto rng = default_random_engine(seed);
        shuffle(begin(unknown_cards), end(unknown_cards), rng);

        hit_wins += SimulateGames(unknown_cards, player);
        stay_wins += SimulateGames(unknown_cards, player->score);
    }

    float hit_odds = hit_wins / SIMS * 10;
    float stay_odds = stay_wins / SIMS * 10;

    cout << "\nOdds of Winning if You Hit: "
        << hit_odds << "%\n"
        << "Odds of Winning if You Stay: "
        << stay_odds << "%\n";
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

    if (sim_dealer->score > 21 || sim_dealer->score < player_total)
    {
        return 1;
    }

    else
    {
        return 0;
    }
}