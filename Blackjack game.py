#========Blackjack game=======
#========Import libraries=======
import random

#========Functions=======
# Function to randomly select cards from a deck
def draw_card(cards):
    random_card = random.choice(cards)
    return random_card

# Function to display game results
def game_results(dealer, player):
    print(f"Dealer's hand: {dealer}")
    print(f"Player's hand: {player}")


# Initialise the different card types that can be drawn
Ace = 1
J = 10
Q = 10
K = 10
cards = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, J, Q, K]

# Dealer gameplay
d_card_1 = draw_card(cards)
d_card_2 = draw_card(cards)
print(f"Dealer's first card is: {d_card_1}")

# Player gameplay
p_card_1 = draw_card(cards)
p_card_2 = draw_card(cards)
print(f"Player's cards are: {p_card_1} and {p_card_2}\n")
play_list = []
player_hand = p_card_1 + p_card_2
dealer_hand = d_card_1 + d_card_2
player_total = player_hand

while True:
    player_choice = input("Draw another card? (Y or N): ")
    if player_choice.upper() == "Y":
        extra_card = draw_card(cards)
        print(f"New card drawn: {extra_card}")
        play_list.append(extra_card)
        player_total = player_hand + sum(play_list)
        print(f"Current total = {player_total}")
        if player_total == 21:
            print("Congratualtions! You win.\n")
            break
        elif player_total > 21:
            print("Player Bust!")
            exit()
        continue

    elif player_choice.upper() == "N":
        # If dealer's total is less than 17, they need to draw another card
        if dealer_hand < 17:
            d_card_3 = draw_card(cards)
            dealer_hand = dealer_hand + d_card_3
            if dealer_hand > 21: 
                print(f"Dealer's hand: {dealer_hand}")
                print("Dealer bust! You win!")
                exit()
        break

    else:
        print("Invalid input. Please try again\n")

# Results
dealer_win = 21 - dealer_hand
player_win = 21 - player_total
if player_win < dealer_win:
    game_results(dealer_hand, player_total)
    print("Congratualtions! You win!")
elif player_win == dealer_win:
    game_results(dealer_hand, player_total)
    print("Draw!")
else:
    game_results(dealer_hand, player_total)
    print("Sorry, you lose.")

