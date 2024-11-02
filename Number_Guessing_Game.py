import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.secret_number = random.randint(1, 100)
        self.attempts = 10
        
        self.label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=5)
        
        self.button = tk.Button(root, text="Guess", command=self.check_guess, font=("Arial", 14))
        self.button.pack(pady=5)
        
        self.feedback = tk.Label(root, text="", font=("Arial", 12))
        self.feedback.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.feedback.config(text="Please enter a valid integer.")
            self.entry.delete(0, tk.END)  # Clear input field
            return

        self.attempts -= 1
        
        if guess == self.secret_number:
            messagebox.showinfo("Result", f"Congratulations! You've guessed the number {self.secret_number} correctly.")
            self.reset_game()
        elif self.attempts == 0:
            messagebox.showinfo("Result", f"Sorry, you're out of attempts! The correct number was {self.secret_number}.")
            self.reset_game()
        elif guess < self.secret_number:
            self.feedback.config(text=f"Too low! You have {self.attempts} attempts left.")
        else:
            self.feedback.config(text=f"Too high! You have {self.attempts} attempts left.")
        
        self.entry.delete(0, tk.END)  # Clear input field after each guess
    
    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 10
        self.feedback.config(text="")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
