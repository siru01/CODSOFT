from tkinter import *
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def player_choice(choice):
    computer_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_choices)

    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

def play_again():
    result_label.config(text="")
    player_choice_var.set("")

root = Tk()
root.geometry("450x400")  
root.resizable(0, 0)
root.title("Rock, Paper, Scissors")

result_label = Label(root, text="", font=('Arial Rounded MT Bold', 16))
result_label.pack(pady=20)

player_choice_var = StringVar()

choices = ["Rock", "Paper", "Scissors"]
for choice in choices:
    Button(root, text=choice, padx=20, pady=10, font=('Arial Rounded MT Bold', 12),
              command=lambda choice=choice: player_choice(choice)).pack()

play_again_button = Button(root, text="Play Again", padx=10, pady=5, font=('Arial Rounded MT Bold', 12), command=play_again)
play_again_button.pack(pady=20)

root.mainloop()
