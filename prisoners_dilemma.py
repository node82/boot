def prisoner_dilemma(player1, player2, iterations):
    player1_score = 0
    player2_score = 0

    for _ in range(iterations):
        decision1 = player1()
        decision2 = player2()

        if decision1 == 'cooperate' and decision2 == 'cooperate':
            player1_score += 3
            player2_score += 3
        elif decision1 == 'betray' and decision2 == 'cooperate':
            player1_score += 5
        elif decision1 == 'cooperate' and decision2 == 'betray':
            player2_score += 5
        elif decision1 == 'betray' and decision2 == 'betray':
            player1_score += 1
            player2_score += 1

    print(f"Player 1 score: {player1_score}")
    print(f"Player 2 score: {player2_score}")

# strategies
def always_cooperate():
    return 'cooperate'

def always_betray():
    return 'betray'

def random_strategy():
    import random
    return random.choice(['cooperate', 'betray'])

def generous_tit_for_tat(opponent_decision):
    return 'cooperate' if opponent_decision == 'cooperate' else 'cooperate'

def vengeful_tit_for_tat(opponent_decision):
    return 'betray' if opponent_decision == 'betray' else 'cooperate'

def tit_for_tat(opponent_decision):
    return 'cooperate' if opponent_decision == 'cooperate' else 'betray'

# play
# prisoner_dilemma(always_cooperate, always_betray, 10)
# prisoner_dilemma(always_cooperate, always_cooperate, 10)
# prisoner_dilemma(always_cooperate, tit_for_tat, 10)
#prisoner_dilemma(always_cooperate, generous_tit_for_tat, 10)
prisoner_dilemma(always_cooperate, vengeful_tit_for_tat, 10)
# prisoner_dilemma(always_cooperate, always_cooperate, 10)
