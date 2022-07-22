from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL("dojo_survey_schema").query_db(query, data)

    @classmethod
    def show(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojo_survey_schema").query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate(dojo):
        is_valid = True
        if len(dojo["name"]) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False

        if len(dojo["comment"]) < 3:
            flash("comment must be at least 3 characters.")
            is_valid = False

        return is_valid