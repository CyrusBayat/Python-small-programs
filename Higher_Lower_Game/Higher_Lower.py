logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

from data import data 
import random
import os


def option():
    option = random.choice(data)
    return option


def items():
    item = option()
    name = item['name']
    description = item['description']
    country= item['country']
    global COUNT
    COUNT = item['follower_count']
    return (name + ", " + description + ", " +country )



def game():
    print(logo)
    
    item_A = items()
    print(f"Compare A: "+ item_A )
    count_A = COUNT
    print(vs)

    item_B = items()
    count_B = COUNT
    print (f"Against B: " + item_B)

    score =0
    game =True
    while game != False:
        type = input("Who has more followers? Type 'A' or 'B': ").lower()
        os.system('cls')
        print(logo)
        if type =='a' and count_A > count_B or type == 'b' and count_B > count_A:
            score = score + 1
            print (f"You're right! Current score: {score}.")
            item_A =item_B
            count_A = count_B
            print(f"Compare A: "+ item_A )
            print(vs)
            item_B = items()
            count_B = COUNT
            print (f"Against B: " + item_B)
            
            
        else:
            print (f"Sorry, that's wrong. final score: {score}")
            game = False




game()



