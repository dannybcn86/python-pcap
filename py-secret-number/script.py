'''
Main Module: The secret letter game
'''
import datetime
import random
import time
import string

print("*" * 150)
print("SECRET NUMBER GAME")
print("*" * 150)


player_name = input("Hello! What's your name? ")
MAX_VALUE = int(input("Please, select the maximum number: "))
print(f"Wellcome, {player_name}! I'm thinking of a number between 1 and {MAX_VALUE}. Can you guess it?")


secret_number = random.randint(a = 1, b = MAX_VALUE) # random.randranges és més potent 
# secret_number = random.randrange(start = 1, stop = MAX_VALUE +1, step = 2)

secret_letter = random.choice(string.ascii_uppercase)
num_attempts = 0
secret_found = False

while not secret_found:
    num_attempts += 1

    print("-" * 100)
    player_number = int(input(f"Attempt {num_attempts} > Please {player_name}, select a number between 1-{MAX_VALUE}: "))
    print("-" * 100)

    if player_number == secret_number:
        print(f"Congratulations, {player_name}! The secret number was {secret_number} and you guessed it!")
        secret_found = True
    elif player_number < secret_number:
        print(f"Sorry, {player_name}! Your guess is too low: The number {player_number} is not the secret number")
    elif player_number > secret_number:
        print(f"Sorry, {player_name}! Your guess is too hight: The number {player_number} is not the secret number")

print(f"Good job, {player_name}! Thanks for playing with us!")