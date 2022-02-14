
from art import logo
import random
import clear
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

deal_card()
def calculate_score(cards):


    if sum(cards)==21 and len ==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score,computer_score):
    if computer_score == user_score:
        return "draw"

    elif computer_score>21 and user_score>21:
        return "both loose "

    elif user_score>21:
        return "went over you loose"
    elif user_score >computer_score:
        return "user wins"
    elif computer_score==0:
        return "computer wins "

    elif user_score==0:
        return "computer wins "

    elif computer_score>21:
        return "computer went over you win hurray"

    else:
        return "you loose"



def play_game():
    print(logo)
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    is_game_over=False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"{user_cards} and total is {user_score}")
        print(f"{computer_cards} and total is {computer_score}")
        # print(user_cards)
        # print(computer_cards)
        if user_score==0 or computer_score ==0 or user_score>21:
            is_game_over=True

        else:
            user_should_deal=input("draw another? y or n")
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True


    while computer_score !=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"your final hand was {user_cards} and the computer's was {computer_cards}")
    print(f"your final score was {user_score} and the computer's was {computer_score}")
    print(compare(user_score,computer_score))

while input("wanna play a game of black jack y or n")=="y":
    # clear()
    play_game()