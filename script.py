from peewee import *
from questions import Card
import random
import argparse

db = PostgresqlDatabase(
    "questions", user="postgres", password="", host="localhost", port=5432
)


parser = argparse.ArgumentParser(description="Play a game")
parser.add_argument("-c")
args = parser.parse_args()

if __name__ == "__main__":
    args = parser.parse_args()

card = list(Card.select())
random.shuffle(card)
counter = 0
score = 0
print(len(card))
correct_message = "that's right!"
over_message = "\nGame Over!\n"

in_book = True

while in_book == True:

    ui = """
  Welcome to the Monty Python Trivia Quiz 
  1. Add new trivia questions
  2. Play the Monty Python Trivia Quiz
  3. Exit application
  """
    print(ui)

    def add_card():
        add_card = Card(
            front=input("Write out the question and options: "),
            back=input("Enter the solution: "),
        )
        add_card.save()
        print(ui)

    def game(card):
        global counter
        global score
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

    user_select = int(input("Select: "))
    if user_select == 1:
        add_card()
    elif user_select == 2:
        game(card)
    elif user_select == 3:
        print("Thanks for playing")
