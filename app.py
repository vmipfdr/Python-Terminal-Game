from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase(
    "people", user="postgres", password="", host="localhost", port=5423
)


class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    name = CharField()
    age = IntegerField()


db.connect()
db.drop_tables([Person])
db.create_tables([Person])

Person(name="Tyler", age=28).save()
Person(name="Zakk", age=29).save()

app = Flask(__name__)


@app.route("/person/", methods=["GET", "POST"])
@app.route("/person/<id>", methods=["GET", "PUT", "DELETE"])
def endpoint(id=None):
    if request.method == "GET":
        if id:
            return jsonify(model_to_dict(Person.get(Person.id == id)))
        else:
            peopleList = []
            for person in Person.select():
                peopleList.append(model_to_dict(person))
            return jsonify(peopleList)

    if request.method == "PUT":
        return "PUT request"

    if request.method == "POST":
        new_person = dict_to_model(Person, request.get_json())
        new_person.save()
        return jsonify({"success": True})

    if request.method == "DELETE":
        return "DELETE request"


app.run(debug=True, port=9000)
