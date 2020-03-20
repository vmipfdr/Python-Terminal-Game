# an array of question dictionaries

from peewee import *

db = PostgresqlDatabase('questions', user='postgres',
                        password='', host='localhost', port=9000)


class BaseModel(Model):
    class Meta:
        database = db


class Card(BaseModel):
    front = CharField()
    back = CharField()
    wrong = IntegerField()


db.connect()
db.drop_tables([Card])
db.create_tables([Card])

Card(front="How many members were in the group known as Monty Python?  four, three, eight, six ",
    back="six", wrong=0).save()
Card(front="Who played the character of Arthur in the classic movie Monty Python and the Holy Grail?  Michael Palin, Graham Chapman, Eric Idle, Terry Jones",
    back="Graham Chapman", wrong=0).save()
Card(front="In the film Monty Python and the Holy Grail, how many questions does the Bridge Keeper ask?  three, one, none, four",
    back="three", wrong=0).save()
Card(front="WHich member of Monty Python appeared at the closing Olympic Ceremonies in London 2012?  Eric Idle, Terry Gilliam, Terry Jones, Michael Palin ",
    back="Eric Idle", wrong=0).save()
Card(front="Which member of Monty Python died in 1989?  Eric Idle, Terry Gilliam, Terry Jones, Michael Palin",
    back="Graham Chapman", wrong=0).save()
Card(front="When Monty Python needed funding, which famous rocker loaned them money?  George Harrison, Elton John, Eric Clapton, Rod Stewart",
    back="George Harrison", wrong=0).save()
Card(front="When did Monty Python's Flying Circus first air?  1969, 1975, 1982, 1978",
    back="1969", wrong=0).save()
Card(front="Which member of Monty Python created most of the sketches? Terry Gilliam, Terry Jones, Eric Idle, Michael Palin",
    back="Terry Gilliam", wrong=0).save()
Card(front="Which member of Monty Python is the shortest?  Eric Idle, Terry Jones, John Cleese, Terry Gilliam",
    back="Terry Jones", wrong=0).save()
Card(front="Eric Idle is the narrator on which of these films?  Ella Enchanted, Shawshank Redemption, The Princess Bride, The Thin Red Line",
    back="Ella Enchanted", wrong=0).save()
Card(front="When did the Meaning of Life Debut?  1983, 1976, 1972, 1986",
    back="1983", wrong=0).save()
Card(front="Which member of Monty Python was responsible for Spamalot?  Eric Idle, Terry Jones, John Cleese, Terry Gilliam",
    back="Eric Idle", wrong=0).save()
Card(front="Which North American network was the first to pick-up Monty Python's Flying Circus?  ABC, CBC, NBC, HBO",
    back="CBC", wrong=0).save()
Card(front="Who plays Brian in The Life of Brian?  Eric Idle, Graham Chapman, John Cleese, Terry Gilliam",
    back="Graham Chapman", wrong=0).save()
Card(front="What was Brian's last name in the classic film The Life of Brian?  Hoskins, Frisbee, Pilate, Cohen",
    back="Cohen", wrong=0).save()
Card(front="Ireland banned the film The Life of Brian. What other nation did the same?  Germany, Japan, South America, Norway",
    back="Norway", wrong=0).save()
Card(front="In Monty Python and the Holy Grail', what kind of shrubbery do the Knights Who Say Ni originally want?",
    back="a nice cheap one, a big wooden badger, a herring, a cat", wrong=0).save()
Card(front="What happens to the Black Beast of Aaaarrgghhh in Monty Python's 'Monty Python and the Holy Grail'?  Sir Lancelot kills it, Snuffed By The Holy Hand Grenade, Head Is Bitten Off By Killer Rabbit, Animator Suffers A Heart Attack",
    back="Animator Suffers A Heart Attack", wrong=0).save()
Card(front="In Monty Python's 'Life of Brian', what was Brian's original occupation? Selling Snacks At The Forum, He Didn't Have A Job, A Gladiator, A Carpenter",
    back="Selling Snacks At The Forum", wrong=0).save()
Card(front="hat did the old man in 'Monty Python and the Holy Grail' ask when knights tried to cross a bridge?  Do You Like Cheese?, What Is Your Favorite Color?, How Old Are You?, What Is Your Name?",
    back="What Is Your Name?", wrong=0).save()
Card(front="What was the name of the enchanter in 'Monty Python and the Holy Grail'?  He Didn't Have A Name, Brian, Arthur, Tim",
    back="Tim", wrong=0).save()
Card(front="On which day does the lumberjack have buttered scones in Monty Python's 'The Lumberjack Song'?  Every Day, Wednesday, Thursday, Sunday",
    back="Wednesday", wrong=0).save()



