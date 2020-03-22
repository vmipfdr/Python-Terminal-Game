from peewee import *
from questions import Card
import random

db = PostgresqlDatabase(
    "questions", user="postgres", password="", host="localhost", port=5432
)


card = list(Card.select())

random.shuffle(card)
counter = 0
score = 0

# print(card)
print(len(card))

welcome_message = "Welcome to the Monty Python Trivia Quiz"
correct_message = "that's right!"
over_message = "\nGame Over!\n"
# print(welcome_message)

# I wonder if we can have the student set the counter to reduce cards shown

# have to create a new card, but don't let users do it
# input(" enter 'game' or 'create' \n")


def game(card):
    global counter
    global score
    print(welcome_message)
    print(f"\n{card[counter].front}")
    choice = input(" \nWhat's your answer? \n")
    print("\n\n\n")
    if choice == card[counter].back:
        counter += 1
        score += 1
        print(correct_message)
        # print(counter)
        print(f"{score} / {len(card)}")
        if counter < len(card):
            return game(card)
        else:
            print(over_message)
    else:
        print("\n\n\n")
        print(f"Wrong, the correct answer is {card[counter].back}")
        counter += 1
        # print(counter)
        print(f"{score} / {len(card)}")
        if counter < len(card):
            return game(card)
        else:
            print(over_message)


game(card)
