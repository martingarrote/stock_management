from general.config import *
from general.tools import *
from models.permission import *
from models.person import *

def run():

    default_permission = Permission.query.get(1)
    worker_permission = Permission.query.get(2)
    admin_permission = Permission.query.get(3)

    admin = Person(name = "admin", email = "admin@gmail.com", password = encrypt("312"), permission = admin_permission)
    worker = Person(name = "worker", email = "worker@gmail.com", password = encrypt("worker"), permission = worker_permission)
    person = Person(name = "person", email = "person@gmail.com", password = encrypt("person"), permission = default_permission)

    db.session.add_all([admin, worker, person])
    db.session.commit()

    print("Persons:\n")
    for i in range(1, 4):
        print(Person.query.get(i), "\n")
    print()