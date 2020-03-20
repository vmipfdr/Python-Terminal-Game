# # # Import the 'Flask' class from the 'flask' library.
# # from flask import Flask

# # # Initialize Flask
# # # We'll use the pre-defined global '__name__' variable to tell Flask where it is.
# # app = Flask(__name__)

# # # Define our route
# # # This syntax is using a Python decorator, which is essentially a succinct way to wrap a function in another function.
# # @app.route('/')
# # def index():
# #     return "Hello, world!"


# # # Run our application, by default on port 5000
# # app.run()


# from flask import Flask, jsonify, request
# from peewee import *
# from playhouse.shortcuts import dict_to_model, model_to_dict
# db = PostgresqlDatabase('people', user='oob', password='',
#                         host='localhost', port=5432)


# class BaseModel(Model):
#     class Meta:
#         database = db


# class Person(BaseModel):
#     name = CharField()
#     age = IntegerField()


# db.connect()
# db.drop_tables([Person])
# db.create_tables([Person])
# Person(name='Tyler', age=28).save()
# Person(name='Zakk', age=29).save()
# Person(name='Levani', age=34).save()
# app = Flask(__name__)
# # Create Person
# @app.route('/person/', methods=['POST'])
# def create_person():
#     new_person = dict_to_model(Person, request.get_json())
#     new_person.save()
#     return jsonify({"success": True})
# # Get All
# @app.route('/person/', methods=['GET'])
# @app.route('/person/<id>', methods=['GET'])
# def get_person(id=None):
#     if id:
#         return jsonify(
#             model_to_dict(
#                 Person.get(Person.id == id)))
#     else:
#         people = []
#         for person in Person.select():
#             people.append(model_to_dict(person))
#         return jsonify(people)


# app.run(debug=True, port=9000)


