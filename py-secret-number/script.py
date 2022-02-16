'''
Main Module: The secret letter game
'''
import datetime as dt
import random
import time

def main():
    print("*" * 150)
    print("SECRET NUMBER GAME")
    print("*" * 150)


    player_name = input("Hello! What's your name? ")
    MAX_VALUE = int(input("Please, select the maximum number: "))
    print(f"Wellcome, {player_name}! I'm thinking of a number between 1 and {MAX_VALUE}. Can you guess it?")

    print(f"We are preparing the game. Please wait {len(player_name)} seconds...")
    # 
    for t in range(1, len(player_name)):
        print(f"Waiting to start... Seconds: {t} s ")
        time.sleep(len(player_name))  # Dormirem el joc els segons de la longitut que tingui el nom del jugador

    secret_number = random.randint(a = 1, b = MAX_VALUE) # random.randranges és més potent 
    # secret_number = random.randrange(start = 1, stop = MAX_VALUE +1, step = 2)

    num_attempts = 0

    start_date = dt.datetime.now() # Estem cridant al mètode factory (mètode estàtic) now() de la class datetime del mòdul datetime i creem l'objecte de la data del moment en el s'arriba a aquesta execució
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


    end_date = dt.datetime.now()        # Cridem de nou al mètode factory now() de la class datetime del mòdul datetime i creem un nou objecte de la data del moment en el que s'arriba a aquesta execució
    duration = end_date - start_date    # Fem la resta de les dates start_date i end_date per tenir el temps que hem trigat en terminar el joc
    
    print(f"Total duration: {duration.total_seconds():8.2f} seconds")    # Mostrem la duració del nostre joc i li diem que ens mostri total_seconds() i formategem la variable duration per a que només mostri 2 decimals
    print(f"Good job, {player_name}! Thanks for playing with us!")


# Invocación del método de inicio del módulo
if __name__ == "__main__":
    main()
