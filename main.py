from random import randint


rps = {1: 'rock', 2: 'paper', 3: 'scissor'}
computer_choice = int(randint(1, 3))
# print(computer_choice)
game_mode = input("Choose game more(r: Random, i: Impossible): ")
user_choice = int(input("Choose your move(1: Rock, 2: Paper, 3: Scissor): "))


if game_mode.lower() == "r":
    def normalcomputer(computer_input, user_input):
        if computer_input == user_input:
            return 'Tie'
        elif computer_input == 1 and user_input == 2 or computer_input == 2 and user_input == 1:
            return 'Paper'
        elif computer_input == 1 and user_input == 3 or computer_input == 3 and user_input == 1:
            return 'Rock'
        elif computer_input == 2 and user_input == 3 or computer_input == 3 and user_input == 2:
            return 'Scissor'

    if normalcomputer(computer_choice, user_choice).lower() == rps[user_choice].lower():
        print(f"Computer chose {rps[computer_choice]}  You win")
    elif normalcomputer(computer_choice, user_choice) == 'Tie':
        print('Tie')
    else:
        print(f"Computer chose {rps[computer_choice]} and won!")

elif game_mode.lower() == "i":
        if user_choice == 1:
            print("Computer chose Paper and Won")
        elif user_choice == 2:
            print("Computer chose Scissor and Won")
        elif user_choice == 3:
            print("Computer chose Rock and Won")



