from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    DB = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        print(query)
        results = connectToMySQL(cls.DB).query_db(query)
        print(results)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"

        return connectToMySQL(cls.DB).query_db(query, data)