from general.config import *
from models.product import *

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    p1 = Product(name = "water bottle", description = "bottle with 500ml water", is_perishable = False, freezable = False, price = 1.99, expired = False)
    p2 = Product(name = "apple", description = "good circle red fruit", is_perishable = True, freezable = False, price = 0.30, expired = False, validity = date(2023, 1, 17))
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    print(p1.json())
    print(p2.json())
