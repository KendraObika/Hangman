#import modules
import re
import subprocess
import random
from WordBank import word_list



#################################################################################
#Helper Functions

def fill_in(correct, indexes, guess):
    '''
    Fills in all the correct guesses in the right indexes
    '''

    for i in indexes:
        n = len(guess)
        y = i
        while n > 0:
            for char in list(guess):
                correct[y] = char
                y = y+1
                n = n-1

def mesh(list):
    '''
    Meshes list in string
    '''
    result = ''
    for item in list:
        result = result + item
    return result



def display(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


#################################################################################


def play():


    tries = 6
    used = ''
    secret = random.choice(word_list)
    #print(secret)
    correct = [" "]*len(secret)


    #Introduce yourself and say what we're playing
    print("Hello! Welcome to Hangman, what's your name?")
    player = input("My name is: ")
    print("Hello " + player + " and good luck!")
    print(display(tries))


    while tries > 0 and mesh(correct) != secret:
        #Player guesses a letter
        guess = input("Your guess is: ").lower()

        #If they guess the same thing over and over
        while (guess in used or guess in correct):
            guess = input("You already guessed that, try again. Your new guess is: ").lower()

        while (not guess.isalpha()):
            guess = input("Please type letters only, try again. Your new guess is: ").lower()

        #If letter is in secret word
        if guess in secret:
            print (guess + " was a correct guess!")
            indexes = [m.start() for m in re.finditer(guess, secret)]
            fill_in(correct, indexes, guess)
            print(correct)

        #If letter is not in secret word
        if guess not in secret:
            used = used + guess
            tries = tries-1
            if tries == 1:
                print (guess + " was incorrect. You have 1 try left.")
            else:
                print (guess + " was incorrect. You have " + str(tries) + " tries left.")
            print(correct)
            print(display(tries))


    if tries == 0:
        print(display(tries))
        print("Sorry you lost, your word was " + secret + ". Want to play again?")

    if mesh(correct) == secret:
        print("You won Hangman, want to play again?")






if __name__ == '__main__':
    play()
    while input("Play Again? (y/n) ").lower() == "y":
        play()
