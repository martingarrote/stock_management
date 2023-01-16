from general.config import *

class Permission(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(20))
    description = db.Column(db.String(250))

    def __str__(self):
        return f"ID: {self.id} \nName: {self.name} \nDescription: {self.description}"

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }