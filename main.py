import random
import art

def deal_card():
    """Return a random card from the deck"""

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculator_score(list_of_cards):
    """Calcultate sum of cards"""

    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    elif 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    
    return sum(list_of_cards)

def compare(user_score, computer_score):
    """Compare sum of user and computer cards"""

    if user_score == computer_score:
        return "Draw!\nGame Over!"
    elif computer_score == 0:
        return "You Lose! Computer Win with a blackjack!"
    elif user_score == 0:
        return "You Win with a blackjack!"
    elif computer_score > 21:
        return "You Win!"
    elif user_score > 21:
        return "You Lose! Computer Win!"
    elif computer_score > user_score:
        return "You Lose! Computer Win!"
    else:
        return "You Win!"
    
    



def blackjack_game():
    print(art.logo)
    # game start with 2 cards each player
    user_cards = []
    computer_cards = []

    for i in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

    user_turn = True
    while user_turn:
        user_total = calculator_score(user_cards)
        computer_total = calculator_score(computer_cards)
        
        # print user cards and first card of computer
        print(f"Your cards: {user_cards}, your total: {user_total}")
        print(f"Computer first cards: {computer_cards[0]}")
        
        # game logic
        if user_total == 0 or computer_total == 0 or user_total >= 21:
            user_turn = False
        else:
            decision = input("\nType 'yes' to HIT 'no' to STAND: ").lower()
            if decision == 'yes':
                user_cards.append(deal_card())
                user_total = calculator_score(user_cards)
            else:
                user_turn = False

    if user_total <= 21 and computer_total != 0:  
        while computer_total < 17:
            computer_cards.append(deal_card())
            computer_total = calculator_score(computer_cards)

    print("\n")
    print("="*40)
    # Print the final cards and final total score
    print(f"Your final cards: {user_cards}, your final total: {user_total}")
    print(f"Computer final cards: {computer_cards}, computer final total: {computer_total}")

    #Compare the card
    result = compare(user_total, computer_total)
    print(result)


while input("Do you want to play blackjack?(yes or no)\n").lower() == 'yes':
    print("\n"*100)
    blackjack_game()