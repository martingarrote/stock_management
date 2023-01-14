from general.config import *
from models.product import *

def run():
    p1 = Product(
        name = "water bottle",
        description = "bottle with 500ml water",
        is_perishable = False,
        freezable = False, 
        price = 1.99, 
        expired = False
    )
    p2 = Product(
        name = "apple", 
        description = "good circle red fruit", 
        is_perishable = True, 
        freezable = False, 
        price = 0.30, 
        expired = False, 
        validity = date(2023, 1, 17)
    )
    p3 = Product(
        name = "Hamburguer", 
        description = "no words needed beyond hamburguer", 
        is_perishable = True, 
        freezable = True, 
        price = 9.99, 
        expired = False, 
        validity = date(2023, 3, 14)
    )
    p4 = Product(
        name = "Ice",
        description = "ice cubes to freeze things without freezer",
        is_perishable = False,
        freezable = True,
        price = 1.0,
        expired = False
    )
    db.session.add_all([p1, p2, p3, p4])
    db.session.commit()
    
    print("Products:\n")
    for i in range(1, 5):
        print(Product.query.get(i), "\n")
    print()
