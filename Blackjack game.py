#========Blackjack game=======
#========Import libraries=======
import random

#========Functions=======
# Function to randomly select cards from a deck
def draw_card(cards):
    random_card = random.choice(cards)
    return random_card

# Initialise the different card types that can be drawn
Ace = 1
J = 10
Q = 10
K = 10
cards = [Ace, 1, 2, 3, 4, 5, 6, 7, 8, 9, J, Q, K]

# Dealer gameplay
d_card_1 = draw_card(cards)
d_card_2 = draw_card(cards)
print(f"Dealer's first card is: {d_card_1}")

# Player gameplay
p_card_1 = draw_card(cards)
p_card_2 = draw_card(cards)
print(f"Player's cards are: {p_card_1} and {p_card_2}")
play_list = []

while True:
    player_choice = input("Draw another card? (Y or N): ")

    if player_choice == "Y":
        extra_card = draw_card(cards)
        print(f"New card drawn: {extra_card}")
        play_list.append(extra_card)
        print(play_list)
        player_hand = p_card_1 + p_card_2 + sum(play_list)
        print(player_hand)
        if player_hand == 21:
            print("Congratualtions! You win.")
            break
        elif player_hand >> 21:
            print("Bust! You lose.")
            break
        continue

    elif player_choice == "N":
        dealer_hand = d_card_1 + d_card_2
        if dealer_hand << 17:
            d_card_3 = draw_card(cards)
            dealer_hand = dealer_hand + d_card_3
            if dealer_hand >> 21:
                print("Dealer bust! You win.")
                exit()
        dealer_win = 21 - dealer_hand
        player_win = 21 - player_hand
        break

    else:
        print("Invalid input. Please try again")

# Results
if player_win << dealer_win:
    print("Congratualtions! You win.")
elif player_win == dealer_win:
    print("Draw!")
else:
    print("Sorry, you lose.")


