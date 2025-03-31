import random

running = True
chances = 0
replay = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")

def difLevel():
    global chances
    global running
    difficulties = {
        "1" : 10,
        "2" : 5,
        "3" : 3
    }

    dif_names = {
        "10" : "Easy",
        "5" : "Medium",
        "3" : "Hard"
    }

    print("Please select the difficulty level:\n")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)\n")

    dif_choice = input("Enter your choice: ")
    valid_choice = False

    for dif_key, dif_value in difficulties.items():
        if dif_choice == dif_key:
            chances = dif_value
            for dif_name_key, dif_name in dif_names.items():
                if dif_name_key == str(dif_value):
                    print(f"Great! You have selected the {dif_name} difficulty level.\n")
                    valid_choice = True
                    break
            break
    if not valid_choice:
        print("Invalid command, please enter a valid number. \n")
    
    return chances

def numberGame():
    global chances
    print("Let's start the Game!\n")

    number = random.randrange(1, 100)
    attempts = 0

    while chances != 0:
        player_guess = input("Enter your guess: ")

        if int(player_guess) == number:
            attempts += 1
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif int(player_guess) > number:
            attempts += 1
            chances -= 1
            print(f"Incorrect! The number is less than {player_guess}.")
        elif int(player_guess) < number:
            attempts += 1
            chances -= 1
            print(f"Incorrect! The number is more than {player_guess}.")
    
    if chances == 0:
        print("You've used up all your chances, better luck next time!")
    
    while True:
        try_again = input("Want to play again? (Y/N): ")
        if try_again == "Y" or try_again == "y":
            replay = True
            break
        elif try_again == "N" or try_again == "n":
            print("Thanks for playing!")
            replay = False
            break
        else:
            print("Invalid command.")
    
    return replay




while running:
    difLevel()
    numberGame()
    if replay:
        numberGame()
    else:
        running = False