import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 10  # Limit number of attempts
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it correctly.")
    
    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts -= 1
        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} correctly.")
            break
        elif guess < secret_number:
            print(f"Too low! You have {attempts} attempts left.")
        else:
            print(f"Too high! You have {attempts} attempts left.")
        
        if attempts == 0:
            print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
            
if __name__ == "__main__":
    number_guessing_game()
