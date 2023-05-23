import random


logo = """
                                                                                                                                                                                       
         ,--.                                                                                                                                                                          
       ,--.'|                       ____                                                     ,----..                                                                                   
   ,--,:  : |                     ,'  , `.  ,---,                                           /   /   \                                                   ,--,                           
,`--.'`|  ' :         ,--,     ,-+-,.' _ |,---.'|               __  ,-.                    |   :     :          ,--,                                  ,--.'|         ,---,             
|   :  :  | |       ,'_ /|  ,-+-. ;   , |||   | :             ,' ,'/ /|  .--.--.           .   |  ;. /        ,'_ /|             .--.--.    .--.--.   |  |,      ,-+-. /  |  ,----._,. 
:   |   \ | :  .--. |  | : ,--.'|'   |  ||:   : :      ,---.  '  | |' | /  /    '          .   ; /--`    .--. |  | :    ,---.   /  /    '  /  /    '  `--'_     ,--.'|'   | /   /  ' / 
|   : '  '; |,'_ /| :  . ||   |  ,', |  |,:     |,-.  /     \ |  |   ,'|  :  /`./          ;   | ;  __ ,'_ /| :  . |   /     \ |  :  /`./ |  :  /`./  ,' ,'|   |   |  ,"' ||   :     | 
'   ' ;.    ;|  ' | |  . .|   | /  | |--' |   : '  | /    /  |'  :  /  |  :  ;_            |   : |.' .'|  ' | |  . .  /    /  ||  :  ;_   |  :  ;_    '  | |   |   | /  | ||   | .\  . 
|   | | \   ||  | ' |  | ||   : |  | ,    |   |  / :.    ' / ||  | '    \  \    `.         .   | '_.' :|  | ' |  | | .    ' / | \  \    `. \  \    `. |  | :   |   | |  | |.   ; ';  | 
'   : |  ; .':  | : ;  ; ||   : |  |/     '   : |: |'   ;   /|;  : |     `----.   \        '   ; : \  |:  | : ;  ; | '   ;   /|  `----.   \ `----.   \'  : |__ |   | |  |/ '   .   . | 
|   | '`--'  '  :  `--'   \   | |`-'      |   | '/ :'   |  / ||  , ;    /  /`--'  /        '   | '/  .''  :  `--'   \'   |  / | /  /`--'  //  /`--'  /|  | '.'||   | |--'   `---`-'| | 
'   : |      :  ,      .-./   ;/          |   :    ||   :    | ---'    '--'.     /         |   :    /  :  ,      .-./|   :    |'--'.     /'--'.     / ;  :    ;|   |/       .'__/\_: | 
;   |.'       `--`----'   '---'           /    \  /  \   \  /            `--'---'           \   \ .'    `--`----'     \   \  /   `--'---'   `--'---'  |  ,   / '---'        |   :    : 
'---'                                     `-'----'    `----'                                 `---`                     `----'                          ---`-'                \   \  /  
                                                                                                                                                                              `--`-'   
"""

print(logo)
print("Welcome to the Number Guessing Game!")


def compare(target, level):

  for i in range (0, level):
    user_choice = int(input("Make a gues: "))
    
    if target < user_choice:
      print("Too high")
      print("Guess again.")
      level -=1
      print(f"You have {level} attempts to guess the number." )

    elif target > user_choice:
      print("Too low.")
      print("Guess again.")
      level -=1
      print(f"You have {level} attempts to guess the number." )

    else:
      print(f"You Win, the Number was {TARGET_NUMBER}\n")
      return
    
    if level == 0:
      print("You Lost!\n")


TARGET_NUMBER = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.\n")
level = input("Chose a difficulty. Type 'easy' or 'hard: ").lower()

if level == "easy":
  easy = 10
  print(f"Yoy have {easy} attemps remaining to guess the number.")
  compare(TARGET_NUMBER, easy)

elif level == "hard":
  hard = 5
  print(f"Yoy have {hard} attemps remaining to guess the number.")
  compare(TARGET_NUMBER, hard)
else:
  print("Please type only 'easy' or 'hard' to chossing the level.")



# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).



# enemies = 1

# def increase_enemies():
#   global enemies
#   enemies += 5
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")
