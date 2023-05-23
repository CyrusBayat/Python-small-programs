import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Hello to my game")

option = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
    

computer_choice = random.randint(0,2)

if user_choice == 0:
    print("User:" +option[0])
    print("computer: "+ option[computer_choice])

    if computer_choice == 0:
        print("Both chose Rock......draw..........")
    elif computer_choice ==1:
        print("Paper cover Rock.....Computer Win.......")
    else:
        print("Rock breaks Scissors .....You Win.......")
elif user_choice == 1 :
    print("User:" +option[1])
    print("computer: "+ option[computer_choice])
    if computer_choice == 1:
        print("Both chose Paper......draw..........")
    elif computer_choice ==0:
        print("Paper cover Rock.....You Win.......")
    else:
        print("Scissors cuts paper.....Computer Win.......")
elif user_choice == 2:
    print("User:" +option[2])
    print("computer: "+ option[computer_choice])
    if computer_choice == 2:
        print("Both chose Scissors......draw..........")
    elif computer_choice ==1:
        print("Scissors cuts paper.....You Win.......")
    else:
        print("Rock breaks Sccissors.....Computer Win.......")
else:
    print("You Enter a wrong number please try again.\n")
    print("Error: Tray again")


