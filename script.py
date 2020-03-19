from questions import questions
import random

# - Your program should prompt the user to identify the capital associated with a
# given state.
# - There should be running tallies on the number of correct and incorrect answers
# for each state
# - After getting through all 50 states one time, users should be asked whether or
# not they want to play again.

# print(states)
# Make sure the states don't appear in alphabetical order in the prompts.
random.shuffle(questions)

# print(states)

# Provide a welcome message to introduce the player to the game.

welcome_message = "Welcome to the Monty Python Trivia Quiz"

# print(welcome_message)s

for i in questions:
    i['correct'] = 0
    i['incorrect'] = 0
print(welcome_message)

# print(len(states))


def play_game():
    total_correct = 0
    total_incorrect = 0
    for x in questions:
        user_input = input(f"{x['question']}{x['options']}")
        if user_input == x['answer']:
            x['correct'] += 1
            total_correct += 1
            print(
                f'Correct. {total_correct} correct. {total_incorrect} incorrect.')
        else:
            x['incorrect'] += 1
            total_incorrect += 1
            print(
                f'Wrong. {x["answer"]} is the answer. {total_correct} correct. {total_incorrect} incorrect.')
    user_input = input('Another round?')
    if user_input == 'yes':
        play_game()


play_game()
