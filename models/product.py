from general.config import *

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(255))
    is_perishable = db.Column(db.Boolean, nullable = False)
    freezable = db.Column(db.Boolean, nullable = False)
    price = db.Column(db.Float, nullable = False)
    expired = db.Column(db.Boolean, nullable = False)
    validity = db.Column(db.Date, nullable = True)

    def __str__(self):
        exit = f"id: {self.id} \nname: {self.name} \ndescription: {self.description} \
            \nis_perishable: {self.is_perishable} \nfreezable: {self.freezable} \
            \nprice: {self.price} \nexpired: {self.expired}"
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
            "price": self.price,
            "expired": self.expired
        }
        if self.validity is not None:
            exit["validity"] = self.validity
        return exit