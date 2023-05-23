import random

from words import word_list
from art import logo, stages


print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display =[]
for underscore in range(word_length):
    display += "-"


print("Pssst, the solution is " + chosen_word)

entered_word = []
end_of_game = False
while not end_of_game:

    guess = input("Guess a letter: ").lower()

    if guess not in entered_word:
        entered_word +=guess

        for i in range(0,word_length):

            if chosen_word[i] == guess:
                display[i]=guess
            

        if guess not in chosen_word:
            print("You guessed "+ guess + " that's not in the word. You lose a life.")
            lives -=1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print("The word was: "+chosen_word)

        print(f"{' '.join(display)}")


        if "-" not in display:
            end_of_game = True
            print("Congratulations, you guessed the word!")
    
    else:
        print("You already pick " + guess + ". Try another one!")

    print(stages[lives])