from config import *

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(255))
    is_perishable = db.Column(db.Boolean, nullable = False)
    freezable = db.Column(db.Boolean, nullable = False)
    price = db.Column(db.Float, nullable = False)
    validity = db.Column(db.Date, nullable = True)

    def __str__(self):
        exit = f"id: {self.id} \nname: {self.name} \ndescription: {self.description} \
            \nis_perishable: {self.is_perishable} \nfreeazble: {self.freezable} \
            \nprice: {self.price}"
        if self.validity is not None:
            exit += f"\nvalidity: {self.validity}"
        return exit

    def json(self):
        exit = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_perishable": self.is_perishable,
            "freezable": self.freezable,
            "price": self.price
        }
        if self.validity is not None:
            exit["validity"] = self.validity
        return exit


if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    p1 = Product(name = "water bottle", description = "bottle with 500ml water", is_perishable = False, freezable = False, price = 1.99)
    p2 = Product(name = "apple", description = "good circle red fruit", is_perishable = True, freezable = False, price = 0.30, validity = date(2023, 1, 17))
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    print(p1.json())
    print(p2.json())
