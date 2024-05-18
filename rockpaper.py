import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()
        self.result = tk.StringVar()

        self.user_choice.set("rock")  # Default choice for user

        # Label and OptionMenu for user to select choice
        tk.Label(root, text="Select your choice:").pack()
        choices = ["rock", "paper", "scissors"]
        self.user_choice_menu = tk.OptionMenu(root, self.user_choice, *choices)
        self.user_choice_menu.pack()

        # Button to play the game
        tk.Button(root, text="Play", command=self.play_game).pack()

        # Label to display computer's choice
        tk.Label(root, text="Computer's choice:").pack()
        self.computer_choice_label = tk.Label(root, textvariable=self.computer_choice)
        self.computer_choice_label.pack()

        # Label to display the result
        tk.Label(root, text="Result:").pack()
        self.result_label = tk.Label(root, textvariable=self.result)
        self.result_label.pack()

        # Button to play again
        tk.Button(root, text="Play Again", command=self.play_again).pack()

    def play_game(self):
        # Get user's choice
        user_choice = self.user_choice.get()

        # Generate random choice for computer
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Update computer's choice label
        self.computer_choice.set(computer_choice)

        # Determine the winner
        if user_choice == computer_choice:
            self.result.set("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.result.set("You win!")
        else:
            self.result.set("Computer wins!")

    def play_again(self):
        # Reset labels and option menu
        self.computer_choice.set("")
        self.result.set("")
        self.user_choice.set("rock")  # Default choice for user

root = tk.Tk()
app = RockPaperScissorsApp(root)
root.mainloop()
