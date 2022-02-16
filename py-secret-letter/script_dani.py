'''
Main Module: The secret letter game
'''
import datetime
import random
import time
import string

def main():
    print("*" * 150)
    print("SECRET LETTER GAME")
    print("*" * 150)


    player_name = input("Hello! What's your name? ")
    print(f"Wellcome, {player_name}! I'm thinking of a letter. Can you guess it?")

    # secret_number = random.randint(a = 1, b = MAX_VALUE) # random.randranges és més potent 
    # secret_number = random.randrange(start = 1, stop = MAX_VALUE +1, step = 2)

    secret_letter = random.choice(string.ascii_uppercase)
    num_attempts = 0
    secret_found = False

    while not secret_found:
        num_attempts += 1

        print("-" * 100)
        player_letter = input(f"Attempt {num_attempts} > Please {player_name}, select a letter in uppercase: ")
        print("-" * 100)

        if player_letter == secret_letter:
            print(f"Congratulations, {player_name}! The secret letter was {secret_letter} and you guessed it!")
            secret_found = True
        elif player_letter < secret_letter:
            print(f"Sorry, {player_name}! Your guess is too low: The letter {player_letter} is not the secret letter")
        elif player_letter > secret_letter:
            print(f"Sorry, {player_name}! Your guess is too hight: The letter {player_letter} is not the secret letter")

    print(f"Good job, {player_name}! Thanks for playing with us!")


# Invocación del método de inicio del módulo
if __name__ == "__main__":
    main()
