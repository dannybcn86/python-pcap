import random
import os


def main():
    os.system("cls")

    print("*" * 150)
    print("*" * 150)
    title = "R O C K ,  P A P E R  A N D  S C I S S O R S ( \u270A \u2708 \u270C) V.10"
    print(f"{title:^150}")
    print("*" * 150)
    print("*" * 150)

    rock = "\u270A"
    paper = "\u2708"
    scissors = "\u270C"

    MAX_ROUNDS = 5
    player_name = None
    total_games = 0
    total_wins = 0
    round_num = 0
    round_wins = 0
    round_drafts = 0
    round_losses = 0
    computer_move = None
    player_move = None


    # Flags bool
    end_game = False
    end_round = False
    new_game = False
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
        
        while not end_round:
            round_num += 1

            print("-" * 100)
            print("1, 2, 3!!! Rock, paper and scissors...")
            print("-" * 150)
            
            
            while True:
                player_option = input(f"Please, select a value ( R: {rock} | P: {paper} | S: {scissors}): ") # Demanem a l'usuari que trïi una opció vàlida
                True if(player_option.find(valid_options) != -1) else False
                
                # item["comment"] if("comment" in item) else ""
                '''
                if player_option == "R":
                    good_option = True
                elif player_option == "P":
                    good_option = True
                elif player_option == "S":
                    good_option = True
                else:
                    good_option = False
                    print(f"This not is a valid option, select a value ( R: {rock} | P: {paper} | S: {scissors}): ")
                '''
            # El ordinador tria de manera random una lletra del string 'valid_options' que hem definit amb les opcions possibles 'R,P o S
            computer_option = random.choice(valid_options)
            if player_option == computer_option:
                print("Heu empatat, la computadora ha triat la teva mateixa opció")
            elif player_option == "R":
                if computer_option == "P":
                    print(f"Has perdut, {rock} perd contra {paper}")
                    round_losses +=1
                else:
                    print(f"Has guanyat, {rock} guanya a {scissors}")
                    round_wins += 1
            elif player_option == "P":
                if computer_option == "S" :
                    print(f"Has perdut, {paper} perd contra {scissors}")
                    round_losses +=1
                else:
                    print(f"Has guanyat, {paper} guanya a {rock}")
                    round_wins += 1
            elif player_option == "S":
                if computer_option == "R" :
                    print(f"Has perdut, {scissors} perd contra {rock}")
                    round_losses +=1
                else:
                    print(f"Has guanyat, {scissors} guanya a {paper}")
                    round_wins += 1


            # if(player_option in valid_options): True else:   valid_options.index(player_option)

            print("-" * 100)

        if round_num == MAX_ROUNDS:
            new_game = input(f"Do you want to play again? (y/n): ")
            while not good_option:
                if new_game == "y":
                    print(f"Good bye {player_name}, see you again")
                    good_option = True
                    end_game = True
                elif new_game == "n":
                    good_option = True
                else:
                    good_option = False
                    print("This not is a valid option, do you try (y/n)")


# Invocación del método de inicio del módulo
if __name__ == "__main__":
    main()