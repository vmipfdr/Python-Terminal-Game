# Matt's Monty Python Flash Cards (well Terminal Trivia) with Python

I built out a Monty Python Bash/Terminal Trivia game using python and sql. Check it out!

### Flash cards

- A user should be able to create new cards.
- They should be able to set up a training session
- Pick the number of cards they'd like to review and then seecthat many cards.
- For each card, they should be presented with the "front" and then asked for the "back".
- Keep track of how many times a card has been answered correctly and incorrectly.

### How to Play:

- Clone this repo
- run `pipenv shell`
- run `python script.py`
- answer the questions!p

#### The Process I used

1. I first built out the questions and the structure of the models in the questions.py file.
1. Next I built out the database. To do this, inside your pipenv, run `psql`

- from there CREATE DATABASE questions;
- `\q` to get out of psql

1. After creating the database, I run `python questions.py` to seed the db
1. I go back to psql to check on my data by running the following:

- `\l` to see a list of the databases
- `\c questions`
- use `\d` to Lists all tables
- `SELECT * FROM card;` to see all my cards
- `\q` to get out of psql

1. Once I had my SQL database seeded with the flashcards, I built out the MVP game execution. This consisted of:

- connecting to the database I created
- randomizing the list of "cards"
- creating a function that allows the user to see a flash card and answer
- creating a scorecard & a counter to move to the next card
- an if else statement that provides feedback for both correct or incorrect answers

1. Next I focused on building out how many cards the user wants to play

1. Finally I built out the ability for the user to build a new card
