import random
from art import logo

randNumber = 0
guessNumber = 0

def generate_Number():
    number = random.randint(1,100)

    return number

def choose_Difficulty(diff):
    if diff == "easy":
        lives = 10
    elif diff == "hard":
        lives = 5
    else:
        print("You have selected an invalid option")
        lives = 0

    return lives

def Higher_or_Lower(randNumber, guessNumber, lives):

    if randNumber > guessNumber:
        print("Too low.")
        lives -= 1
        if lives == 0:
            print("You have ran out of guesses. You lost!")
            print(f"The answer was {randNumber}.")
        return lives
    elif randNumber < guessNumber:
        print("Too High.")
        lives -= 1
        if lives == 0:
            print("You have ran out of guesses. You lost!")
            print(f"The answer was {randNumber}.")
        return lives
    elif randNumber == guessNumber:
        print(f"You have won. The answer is {randNumber}")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

randNumber = generate_Number()

difficulty = input("Choose a difficulty. Type 'easy' or 'hard' \n")
lives = choose_Difficulty(difficulty)



while guessNumber != randNumber and lives != 0:
    print(f"You have {lives} attempts remaining to guess the number. ")
    guessNumber = int(input("Make a guess\n"))
    lives = Higher_or_Lower(randNumber, guessNumber, lives)


