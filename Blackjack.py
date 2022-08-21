############### Blackjack Project #####################
import Art
import random
from replit import clear


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Take a list of cards and return the score calculated from the cards
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Loss, the opponent has Blackjack."
    elif user_score == 0:
        return "Win, with a Blackjack."
    elif user_score > 21:
        return "You went over. Loss."
    elif computer_score > 21:
        return "Opponent went over. Win."
    elif user_score > computer_score:
        return "Win."
    else:
        return "Loss."


############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def game():
    print(Art.logo)
    print("")

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Gives the user and the computer 2 cards each
    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    counter = 1

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score {user_score}")

        if counter == 1:
            print(f"Computer's first card {computer_cards[0]}")
            counter += 1

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass > ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True
            print("")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print()
    print('\033[1m' + compare(user_score, computer_score) + '\033[0m')


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' > ") == "y":
    print("______________________________________________________________________________")
    game()
