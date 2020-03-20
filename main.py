from peewee import *
from datetime import date
from questions.py import questions


db = PostgresqlDatabase('monty_python', user='postgres', password='',
                        host='localhost', port=9000)


# we are extending PeeWee's Model and building our own Model via BaseModel


class BaseModel(Model):
    class Meta:
        database = db

# so now we don't have to write class meta... yada yada yada every time we build a new model


class Person(BaseModel):
    name = CharField()
    birthday = DateField()


class Pet(BaseModel):
    name = CharField()
    animal_type = CharField()


# connect to the db
db.connect()
# drop the current db
db.drop_tables([Person, Pet])
# rebuild the db
db.create_tables([Person, Pet])


matt = Person(name='Matt', birthday=date(1984, 8, 18))
matt.save()
zakk = Person(name='Zakk', birthday=date(1990, 11, 18))
zakk.save()


cosmo = Pet(name='Cosmo', animal_type='dog')
cosmo.save()

hazel = Pet(name='Hazel', animal_type='dog')
hazel.save()

betsy = Pet(name='Betsy', animal_type='dog')
betsy.save()

goldie = Pet(name='Goldie', animal_type='fish')
goldie.save()

lucifer = Pet(name='Lucifer', animal_type='snake')
lucifer.save()

# Get (single record)
# person = Person.get(Person.name == 'Matt')
# print(person.name)
# print(person.birthday)

# Select (multiple records)
# people = Person.select().where(Person.birthday > date(1984, 1, 1))
# for person in list(people):
#     print(person.name)


# # updating
# person = Person.get(Person.name == 'Zakk')
# person.birthday = date(1989, 11, 18)
# person.name = 'Zachary'
# person.save()

# # deleting
# person = Person.get(Person.name == 'Zakk')
# person.delete_instance()
