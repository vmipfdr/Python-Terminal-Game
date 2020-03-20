# Matt's Monty Python Flash Cards (well Terminal Trivia) with Python

I built out a Monty Python Bash/Terminal Trivia game using python and sql. Check it out!

## Requirements

Your project should meet the following requirements:

1. Run without errors
1. Built in Python, use a SQL database with PeeWee models
1. Include a README written in well formatted Markdown (_hint: look up a README
   template_)
1. Shows a good commit history with frequent commits. We're looking for lots of
   small commits

### Flash cards

A user should be able to create new cards. They should be able to set up
a training session, pick the number of cards they'd like to review and then see
that many cards. For each card, they should be presented with the "front" and
then asked for the "back". Keep track of how many times a card has been answered
correctly and incorrectly.

### Potentially Useful Python Features

- `print()`
- `input()`
- `for` loop
- `sorted()`
- `random.shuffle()`

#### Process

1. I first built out the questions and the structure of the models in the questions.py file.
1. Next I built out the database. To do this, inside your pipenv, run `psql`

- from there CREATE DATABASE questions;
- `\q` to get out of psql

1. After creating the database, I run `python questions.py` to seed the db
1. I go back to psql to check on my data by running the following:

- `\c questions`
- use `\d` to Lists all tables
- `SELECT \* FROM card;` to see all my cards
- `\q` to get out of psql

1.
