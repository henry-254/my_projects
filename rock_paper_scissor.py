import random
game = ["rock","paper","scissors"]

def RPS_game(round):
    user_wins = 0
    computer_wins = 0
    w = 1
    while w <= round:
        cpu_choice = random.choice(game)
        user_choice = str(input("please enter your choice: rock  paper scissors: ")).lower()
        print("\n your choice:", user_choice)
        print("computer choice:", cpu_choice)
        if user_choice == 'rock':
            if cpu_choice == 'rock':
                print("It's a tie!")
            elif cpu_choice == 'scissors':
                print("You win!")
                user_wins+=1
            elif cpu_choice == 'paper':
                print("You lose!")
                computer_wins+=1
        elif user_choice == 'paper':
            if cpu_choice == 'paper':
                print("It's a tie!")
            elif cpu_choice == 'rock':
                print("You win!")
                user_wins+=1
            elif cpu_choice == 'scissors':
                print("You lose!")
                computer_wins+=1
        elif user_choice == 'scissors':
            if cpu_choice == 'scissors':
                print("It's a tie!")
            elif cpu_choice == 'paper':
                print("You win!")
                user_wins+=1
            elif cpu_choice == 'rock':
                print("You lose!")
                computer_wins+=1
        print()
        print("You have "+str(user_wins)+" wins")
        print("The computer has "+str(computer_wins)+" wins")
        print()
    
        if w > round:
            break
    w += 1
    if user_wins > computer_wins:
            print("player wins")
    else:
            print("computer wins")

rounds = int(input("choose best of rounds: 3 or 5: "))

RPS_game(rounds)