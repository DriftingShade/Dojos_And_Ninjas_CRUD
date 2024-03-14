from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    DB = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.dojo_id = data["dojo_id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_dojo_ninjas(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        print(query)
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, 
        updated_at) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"""

        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results
