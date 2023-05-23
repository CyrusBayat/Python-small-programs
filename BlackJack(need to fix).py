import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dictionary = {
    "user":[],
    "computer": [],
}


def card():
    card = random.choice(cards)
    return card



user_score = 0
comp_score = 0
user_card = 0
comp_card = 0

def user_play():
    global user_score, user_card
    user_card = card()
    user_score += user_card
    dictionary["user"] +=[user_card]

def computer_play():
    global comp_score, comp_card
    comp_card = card()
    comp_score += comp_card
    dictionary["computer"] +=[comp_card]

def score_screen(screen):
    user_cards = dictionary["user"]
    computer_cards = dictionary["computer"]

    if screen == "start":
        print(f"Your cards: {user_cards} Your current score: {user_score}")
        print(f"Computer's first card: {comp_card}")
    else:
        print(f"Your cards: {user_cards} Your final score: {user_score}")
        print(f"Computer cards: {computer_cards} computer score: {comp_score}")



def game():
    
    for i in range (0,2):
        user_play()

    computer_play()
    score_screen("start")

    flag = True
    while flag == True:
        game_desision =  input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if game_desision == "y":
            user_play()
            computer_play()
            score_screen("")

            if user_score > 21:
                score_screen("")
                print("Computer Win!")
                flag = False
                start()
        elif game_desision == "n":
            computer_play()

            if comp_score > 21:
                score_screen("")
                print("You Win!")
                flag = False
                start()
            elif comp_score == 21 and user_score != 21:
                score_screen("")
                print("Computer Win!")
                flag = False
                start()
            


def start():
    start_desision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if start_desision == "n":
        exit()
    elif start_desision == "y":
        print (logo)
        print("Welcome to the game: \n\n")
        game()
    else:
        print("You Type a wronge char")


start()

