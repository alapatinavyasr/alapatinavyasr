import tkinter as tk
import random


class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0e68c")
        self.root.resizable(False, False)

        # Initialize scores
        self.user_score = 0
        self.computer_score = 0

        # Header Section
        title_frame = tk.Frame(self.root, bg="#4682b4", height=100)
        title_frame.pack(fill=tk.X)
        title_label = tk.Label(
            title_frame,
            text="Rock, Paper, Scissors",
            font=("Helvetica", 20, "bold"),
            fg="white",
            bg="#4682b4",
        )
        title_label.pack(pady=20)

        # Instruction Label
        instructions = tk.Label(
            self.root,
            text="Choose your move:",
            font=("Helvetica", 16),
            bg="#f0e68c",
            fg="#2f4f4f",
        )
        instructions.pack(pady=20)

        # Buttons for Choices
        button_frame = tk.Frame(self.root, bg="#f0e68c")
        button_frame.pack(pady=10)

        self.rock_button = tk.Button(
            button_frame,
            text="Rock",
            command=lambda: self.play_game("Rock"),
            font=("Helvetica", 14),
            bg="#ff6347",
            fg="white",
            activebackground="#cd5c5c",
            width=10,
        )
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(
            button_frame,
            text="Paper",
            command=lambda: self.play_game("Paper"),
            font=("Helvetica", 14),
            bg="#32cd32",
            fg="white",
            activebackground="#228b22",
            width=10,
        )
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(
            button_frame,
            text="Scissors",
            command=lambda: self.play_game("Scissors"),
            font=("Helvetica", 14),
            bg="#1e90ff",
            fg="white",
            activebackground="#104e8b",
            width=10,
        )
        self.scissors_button.grid(row=0, column=2, padx=10)

        # Result Display
        self.result_label = tk.Label(
            self.root,
            text="Make your move!",
            font=("Helvetica", 16, "bold"),
            bg="#f0e68c",
            fg="#2e8b57",
            wraplength=400,
        )
        self.result_label.pack(pady=20)

        # Score Display
        self.score_label = tk.Label(
            self.root,
            text=f"Your Score: {self.user_score}  |  Computer Score: {self.computer_score}",
            font=("Helvetica", 14),
            bg="#f0e68c",
            fg="#2f4f4f",
        )
        self.score_label.pack(pady=10)

        # Play Again Button
        self.play_again_button = tk.Button(
            self.root,
            text="Play Again",
            command=self.reset_game,
            font=("Helvetica", 14),
            bg="#ffa500",
            fg="white",
            activebackground="#ff8c00",
            width=15,
        )
        self.play_again_button.pack(pady=20)

    def play_game(self, user_choice):
        # Computer's random choice
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        # Determine the result
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        # Update result label and score
        self.result_label.config(
            text=f"You chose {user_choice}. Computer chose {computer_choice}.\n{result}"
        )
        self.score_label.config(
            text=f"Your Score: {self.user_score}  |  Computer Score: {self.computer_score}"
        )

    def reset_game(self):
        # Reset scores and labels
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="Make your move!")
        self.score_label.config(
            text=f"Your Score: {self.user_score}  |  Computer Score: {self.computer_score}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
