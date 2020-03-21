from peewee import *
from questions import Card
import random

db = PostgresqlDatabase(
    "questions", user="postgres", password="", host="localhost", port=5432
)


card = list(Card.select())

random.shuffle(card)
counter = 0

# print(card)
print(len(card))

welcome_message = "Welcome to the Monty Python Trivia Quiz"
correct_message = "that's right!"

# print(welcome_message)


def game(card):
    global counter
    print(welcome_message)
    print(f"\n{card[counter].front}")
    choice = input(" \nWhat's your answer \n")
    print("\n\n\n")
    if choice == card[counter].back:
        counter += 1
        print(correct_message)
        # print(counter)
        if counter < len(card):
            return game(card)
        else:
            print("Game Over")
    else:
        print(f"Wrong, the correct answer is {card[counter].back}")
        counter += 1
        # print(counter)
        if counter < len(card):
            return game(card)
        else:
            print("Game Over")


game(card)
