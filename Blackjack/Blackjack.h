#ifndef BLACKJACK_H__
#define BLACKJACK_H__

#include <string>
#include <memory>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <random>
#include <iostream>

using namespace std;

#define MIN 21
#define MAX 16
#define OFFSET 6
#define SIMS 1000

struct card {
	string rank;
	string suit;
	string title;
	int value;
};

struct user {
	vector<shared_ptr<card>> hand;
	int score;
	bool exodia;
};

struct casino {
	vector<shared_ptr<card>> hand;
	int score;
	bool exodia;
	bool soft17;
};

class Blackjack {
public:
	// constructor
	Blackjack();

	// deconstructor
	~Blackjack();
	
	// Press Start
	void GameStart();

	// Test Functions
	void AceTest();
	void ExodiaTest();
	void TestPairs();
	
private:
	shared_ptr<card> InitCard(string rank, string suit, int value);
	shared_ptr<user> InitUser();
	shared_ptr<user> InitUser(vector<shared_ptr<card>> hand);
	shared_ptr<casino> InitCasino();

	void InitDeck();
	void InitGame();
	
	void ShowTable();
	void ShowHand(shared_ptr<user> player);

	void CheckDoubles(shared_ptr<user> player);
	void SplitPair(shared_ptr<user> player);

	void CalculateHand(shared_ptr<user> yugi);
	void CalculateHand(shared_ptr<casino> kaiba);

	void StayOrBust(shared_ptr<user> player);
	void Hit(shared_ptr<user> player);

	void DealersChoice(int player_total);
	void EndGame(shared_ptr<user> player);

	void CountingCards(shared_ptr<user> player);
	int HashCard(shared_ptr<user> sim_player);

	void RunSimulations(vector<shared_ptr<card>> unknown_cards, shared_ptr<user> player);
	float RunSimulations(vector<shared_ptr<card>> unknown_cards, int test_score);

	float SimulateGames(vector<shared_ptr<card>> unknown_cards, shared_ptr<user> player);
	float SimulateGames(vector<shared_ptr<card>> unknown_cards, int player_total);

	const string suits_list[4] = {
		"Clubs",
		"Diamonds",
		"Hearts",
		"Spades"
	};

	vector<shared_ptr<card>> card_list;
	queue<shared_ptr<card>> deck;

	vector<shared_ptr<user>> table;
	shared_ptr<casino> dealer;
};

#endif  // BLACKJACK_H__