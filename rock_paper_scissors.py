import random
print()
print("Welcome!")

# Defining game if vs. computer


def computerGame():
    # User input
    print()
    answer = input("Please enter rock, paper or scissors.  ")
    user = answer.lower()
    if user not in ["rock", "paper", "scissors"]:
        while user not in ["rock", "paper", "scissors"]:
            print("Invalid input.  Please try again.")
            answer = input("Please enter rock, paper or scissors.  ")
            user = answer.lower()
    print()
    print("You chose", answer)

    # Computer choices
    computerOptions = ["rock", "paper", "scissors"]
    computerChoice = random.choice(computerOptions)
    print("Computer chose", computerChoice)

    # Defining conditions
    print()
    if computerChoice == user:
        print("Draw!")
    elif computerChoice == "rock" and user == "scissors":
        print('Computer wins!')
    elif computerChoice == "rock" and user == "paper":
        print('You win!')
    elif computerChoice == "paper" and user == "rock":
        print('Computer wins!')
    elif computerChoice == "paper" and user == "scissors":
        print('You win!')
    elif computerChoice == "scissors" and user == "paper":
        print('Computer wins!')
    elif computerChoice == "scissors" and user == "rock":
        print('You win!')

    print()

    playAgain = input("Enter [1] to play again, enter [2] to exit ")
    if playAgain == "1":
        computerGame()
    elif playAgain == "2":
        print("Thank you for playing!")
    else:
        print("Invalid input")
        while playAgain != "1" and userChoice != "2":
            playAgain = input(
                "Enter [1] to play again, enter [2] to exit  ")
            if playAgain == "1":
                computerGame()
            elif playAgain == "2":
                print("Thank you for playing!")
                return
            else:
                print("Invalid input")

# Defining game if vs. second player


def twoPlayerGame():
    print()
    # User 1 input
    answer1 = input("User 1 please enter rock, paper or scissors.  ")
    user1 = answer1.lower()
    if user1 not in ["rock", "paper", "scissors"]:
        while user1 not in ["rock", "paper", "scissors"]:
            print("Invalid input.  Please try again.")
            answer1 = input("User 1 please enter rock, paper or scissors.  ")
            user1 = answer1.lower()

    print()
    # User 2 input
    answer2 = input("User 2 please enter rock, paper or scissors.  ")
    user2 = answer2.lower()
    if user2 not in ["rock", "paper", "scissors"]:
        while user2 not in ["rock", "paper", "scissors"]:
            print("Invalid input.  Please try again.")
            answer2 = input("User 2 please enter rock, paper or scissors.  ")
            user2 = answer2.lower()

    print()
    print("User 1 chose", answer1)
    print("User 2 chose", answer2)
    print()

    # Defining conditions
    if user1 == user2:
        print("Draw!")
    elif user1 == "rock" and user2 == "scissors":
        print('User 1 wins!')
    elif user1 == "rock" and user2 == "paper":
        print('User 2 wins!')
    elif user1 == "paper" and user2 == "rock":
        print('User 1 wins!')
    elif user1 == "paper" and user2 == "scissors":
        print('User 2 wins!')
    elif user1 == "scissors" and user2 == "paper":
        print('User 1 wins!')
    elif user1 == "scissors" and user2 == "rock":
        print('User 2 wins!')

    print()

    playAgain = input("Enter [1] to play again, enter [2] to exit  ")
    if playAgain == "1":
        twoPlayerGame()
    elif playAgain == "2":
        print("Thank you for playing!")
    else:
        print("Invalid input")
        while playAgain != "1" and playAgain != "2":
            playAgain = input(
                "Enter [1] to play again, enter [2] to exit  ")
            if playAgain == "1":
                twoPlayerGame()
            elif playAgain == "2":
                print("Thank you for playing!")
                return
            else:
                print("Invalid input")


# Rules of the game
print("Ways of winning the game : \n" + "Rock vs Paper => Paper \n" +
      "Paper vs Scissors => Scissors \n" + "Scissors vs Rock => Rock \n")
# Check for vs. computer or 2nd player
userChoice = input(
    "Enter [1] to play vs. the computer, enter [2] to play with two players  ")
if userChoice == "1":
    computerGame()
elif userChoice == "2":
    twoPlayerGame()
else:
    print("Invalid input")
    while userChoice != "1" and userChoice != "2":
        userChoice = input(
            "Enter [1] to play vs. the computer, enter [2] to play with two players  ")
        if userChoice == "1":
            computerGame()
        elif userChoice == "2":
            twoPlayerGame()
        else:
            print("Invalid input")
