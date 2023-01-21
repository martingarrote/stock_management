from general.config import *
from models.permission import Permission

class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.Text, nullable = False)

    permission_id = db.Column(db.Integer, db.ForeignKey(Permission.id), nullable = False)
    permission = db.relationship("Permission")

    def __str__(self):
        return f"ID: {self.id} \nName: {self.name} \nEmail: {self.email} \
        \nPassword: {self.password} \nPermission: {self.permission.json()}"

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "permission_id": self.permission_id,
            "permission": self.permission.json()
        }