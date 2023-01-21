from general.config import *
from models.permission import *

def run():
    default_permission = Permission(name = "default", description = "Read products")
    worker_permission = Permission(name = "worker", description = "Create products, read products and update products")
    admin_permission = Permission(name = "admin", description = "Create products, read products, update products, delete produts and manage users")

    db.session.add_all([default_permission, worker_permission, admin_permission])
    db.session.commit()

    print("Permissions:\n")
    for i in range(1, 4):
        print(Permission.query.get(i), "\n")
    print()