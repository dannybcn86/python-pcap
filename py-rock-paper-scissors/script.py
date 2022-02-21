import random
import os
import math


def main():
    os.system("cls")

    # Variables unicode (emoji)
    rock = "\u270A"
    paper = "\u270B"
    scissors = "\u270C"
    win = "\u2705"
    loses = "\u274C"

    print("*" * 150)
    print("*" * 150)
    title = f"R O C K ,  P A P E R  A N D  S C I S S O R S ( {rock} {paper} {scissors} ) V.10"
    print(f"{title:^150}")
    print("*" * 150)
    print("*" * 150)

    

    MAX_ROUNDS = 5
    player_name = None
    total_games = 0
    total_wins = 0
    total_losses = 0
    round_num = 0
    round_wins = 0
    round_drafts = 0
    round_losses = 0
    computer_move = None
    player_move = None
    player_option = None
    computer_option = None


    # Variables de joc
    end_game = False
    new_game = None
    good_option = False

    valid_options = "RPS"

    player_name = input("Hello! What's your name? ")
    print(f"Welcome, {player_name}! We will play the famous game rock, paper and scissors.")
    print(f"The winner will be the best of {MAX_ROUNDS} rounds. Are you ready?")

    while not end_game:
        total_games +=1
        round_num = 0
        round_wins = 0
        round_drafts = 0
        round_losses = 0
        good_option = False
        end_round = False
        
        while not end_round:
            round_num += 1

            print("-" * 100)
            print("1, 2, 3!!! Rock, paper and scissors...")
            print("-" * 150)
            
            
            while True:
                player_option = str.upper(input(f"Please, select a value ( R: {rock} | P: {paper} | S: {scissors}): ")) # Demanem a l'usuari que trïi una opció vàlida
                # Ternari per continuar amb el joc o preguntar de nou la opció si no has triat una opció vàlida
                if player_option in valid_options:
                    break

            # El ordinador tria de manera random una lletra del string 'valid_options' que hem definit amb les opcions possibles 'R,P o S'
            computer_option = random.choice(valid_options)
            # Comença la comparativa
            if player_option == computer_option:
                print("Heu empatat, la computadora ha triat la teva mateixa opció")
                round_drafts += 1
            elif player_option == "R":
                if computer_option == "P":
                    print(f"{loses} Has perdut, {rock} perd contra {paper}")
                    round_losses +=1
                else:
                    print(f"{win} Has guanyat, {rock} guanya a {scissors}")
                    round_wins += 1
            elif player_option == "P":
                if computer_option == "S" :
                    print(f"{loses} Has perdut, {paper} perd contra {scissors}")
                    round_losses +=1
                else:
                    print(f"{win} Has guanyat, {paper} guanya a {rock}")
                    round_wins += 1
            elif player_option == "S":
                if computer_option == "R" :
                    print(f"{loses}Has perdut, {scissors} perd contra {rock}")
                    round_losses +=1
                else:
                    print(f"{win} Has guanyat, {scissors} guanya a {paper}")
                    round_wins += 1

            # Càlcul de percentatges
            win_process_percent = round_wins/round_num*100
            losses_process_percent = round_losses/round_num*100
            drafts_process_percent = round_drafts/round_num*100
            win_round_percent = round_wins/MAX_ROUNDS*100
            losses_round_percent = round_losses/MAX_ROUNDS*100


            # Comprovem si ja hem arribat a les 5 victories o derrotes que fan que acabin les rondes
            if round_wins == MAX_ROUNDS:
                total_wins += 1
                end_round = True
            elif round_losses == MAX_ROUNDS:
                total_losses = total_games - total_wins
                end_round = True

            # Mostrem per pantalla el missatge de les estadístiques, possem aquesta secció just darrere de la comprovació del final de les rondes per què s'actualitzarà el valor de {total_wins} i {total_losses}
            print("-" * 100)
            print(f"- Game number:              {total_games} (Best of 5 rounds)")
            print("-" * 100)
            print(f"- Round number:             {round_num}")
            print(f"- Round player wins:        {round_wins} ({win_process_percent:8.2f}%) -> Win: {round_wins}/{MAX_ROUNDS} ({win_round_percent:8.2f}%)")
            print(f"- Round computer wins:      {round_losses} ({losses_process_percent:8.2f}%) -> Win: {round_losses}/{MAX_ROUNDS} ({losses_round_percent:8.2f}%)")
            print(f"- Round drafts:             {round_drafts} ({drafts_process_percent:8.2f}%)")
            print("-" * 100)
            print(f"- Total player wins:        {total_wins}")
            print(f"- Total computer wins:      {total_losses}")
            print("-" * 100)

        while not good_option:
            new_game = str.lower(input(f"Do you want to play again? (y/n): "))
            if new_game == "y":
                print(f"{player_name} Prepare for your next game")
                good_option = True
                end_game = False
                end_round = False
            elif new_game == "n":
                print(f"Good bye {player_name}, see you again")
                good_option = True
                end_game = True
            else:
                good_option = False
                print("You enter a invalid option, you have to enter (y/n)")


# Invocación del método de inicio del módulo
if __name__ == "__main__":
    main()