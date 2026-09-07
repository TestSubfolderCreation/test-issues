import random

def guessing_game():
    secret = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10.")

    while True:
        guess = int(input("Your guess: "))
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print("Correct! 🎉")
            break

if __name__ == "__main__":
    guessing_game()
