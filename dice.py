#its a simple project for Dice Rolling Simulator Game in python
print("===Dice Rolling Simulator===")
# random module import kiya taake random number generate kar saken
import random

# loop ko chalane ke liye variable
again = True

# jab tak again True hai loop chalta rahega
while again:

    # 1 se 6 tak random dice number print karega
    print(random.randint(1, 6))

    # user se pooch raha hai dubara dice roll karna hai ya nahi
    another_roll = input("Want to roll the dice again? (Y/N): ")

    # user input ko lowercase mein convert karke check kar rahe hain
    if another_roll.lower() == "y":

        # loop ko dobara start karega
        continue

    else:

        # loop completely band ho jayega
        break