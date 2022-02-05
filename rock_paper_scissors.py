from multiprocessing import parent_process
import random
print()
print("Welcome!")

# Defining cases

'''if comp == user:
    print('Both, the computer and you have entered the same.')
    
elif comp == "rock" and user == "scissor":
    print('The computer has won. Better luck next time.')
    
elif comp == "rock" and user == "paper":
    print('You have won this round. Congratulations!')
    
elif comp == "paper" and user == "rock":
    print('The computer has won. Better luck next time.')
    
elif comp == "paper" and user == "scissor":
    print('You have won this round. Congratulations!')
        
elif comp == "scissor" and user == "paper":
    print('The computer has won. Better luck next time.')

elif comp == "scissor" and user == "rock":
    print('You have won this round. Congratulations!')'''

# Defining game if vs. computer


def computerGame():
    # User input
    answer = input("Please enter rock, paper or scissors.")
    user = answer.lower()
    print("You chose", answer)

    # Computer choices
    computerOptions = ["rock", "paper", "scissors"]
    computerChoice = random.choice(computerOptions)


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
