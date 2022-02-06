import random
print()
print("Welcome!")

# Defining game if vs. computer
def computerGame():
    # User input
    answer = input("Please enter rock, paper or scissors.")
    user = answer.lower()
    print("You chose", answer)

    # Computer choices
    computerOptions = ["rock", "paper", "scissors"]
    computerChoice = random.choice(computerOptions)

    # Defining conditions
    if computerOptions == user:
        print("Draw!")
    elif computerOptions == "rock" and user == "scissor":
        print('Computer wins!')
    elif computerOptions == "rock" and user == "paper":
        print('You win!')
    elif computerOptions == "paper" and user == "rock":
        print('Computer wins!')
    elif computerOptions == "paper" and user == "scissor":
        print('You win!')
    elif computerOptions == "scissor" and user == "paper":
        print('Computer wins!')
    elif computerOptions == "scissor" and user == "rock":
        print('You win!')


# Defining game if vs. second player
def twoPlayerGame():
    # User 1 input
    answer = input("Please enter rock, paper or scissors.")
    user1 = answer.lower()
    print("User 1 chose", answer)

    # User 2 input
    answer = input("Please enter rock, paper or scissors.")
    user2 = answer.lower()
    print("User 2 chose", answer)

    # Defining conditions
    if user1 == user2:
        print("Draw!")
    elif user1 == "rock" and user2 == "scissor":
        print('User 1 wins!')
    elif user1 == "rock" and user2 == "paper":
        print('User 2 wins!')
    elif user1 == "paper" and user2 == "rock":
        print('User 1 wins!')
    elif user1 == "paper" and user2 == "scissor":
        print('User 2 wins!')
    elif user1 == "scissor" and user2 == "paper":
        print('User 1 wins!')
    elif user1 == "scissor" and user2 == "rock":
        print('User 2 wins!')


# Rules of the game
print("Ways of winning the game : \n" + "Rock vs Paper => Paper \n" +
      "Paper vs Scissors => Scissors \n" + "Scissors vs Rock => Rock \n")


# Check for vs. computer or 2nd player
userChoice = input(
    "Enter [1] to play vs. the computer, enter [2] to play with two players")

if userChoice == 2:
    twoPlayerGame()
else:
    computerGame()
