from general.config import *
from general.tools import *

# all products
@app.route("/products")
def list_products():
    products = db.session.query(Product).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

#by id
@app.route("/products/search/id/<int:id>")
def searchby_id(id):
    products = Product.query.get(id)
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# by name
@app.route("/products/search/name/<string:product_name>")
def searchby_name(product_name):
    products = Product.query.filter(Product.name.contains(product_name)).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# by price
@app.route("/products/search/price/<float:wanted_price>")
def searchby_price(wanted_price):
    products = Product.query.filter(Product.price.like(wanted_price)).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# max price
@app.route("/products/search/max_price/<float:max_price>")
def searchby_maxprice(max_price):
    products = Product.query.filter(Product.price < max_price).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# min price
@app.route("/products/search/min_price/<float:min_price>")
def searchby_minprice(min_price):
    products = Product.query.filter(Product.price > min_price).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# perishable
@app.route("/products/search/perishable/<int:value>")
def searchby_perishable(value):
    if value:
        products = Product.query.filter(Product.is_perishable == True).all()
    else:
        products = Product.query.filter(Product.is_perishable == False).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# freezable
@app.route("/products/search/freezable/<int:value>")
def searchby_freezable(value):
    if value:
        products = Product.query.filter(Product.freezable == True).all()
    else:
        products = Product.query.filter(Product.freezable == False).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# validity
@app.route("/products/search/validity/<int:days_to_expire>")
def searchby_validity(days_to_expire):
    due_date = date.today() + timedelta(days=days_to_expire)
    products = Product.query.filter(Product.validity <= due_date).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# expired
@app.route("/products/search/expired")
def searchby_expired():
    products = Product.query.filter(Product.expired == True).all()
    result = result_generator(to_json(products))
    result.headers.add("Access-Control-Allow-Origin", "*")
    return result

# CURL requests

# curl localhost:5000/products
# curl localhost:5000/products/search/id/1
# curl localhost:5000/products/search/name/"ap"
# curl localhost:5000/products/search/price/1.99
# curl localhost:5000/products/search/max_price/1.0
# curl localhost:5000/products/search/min_price/1.0
# curl localhost:5000/products/search/perishable/0
# curl localhost:5000/products/search/perishable/1
# curl localhost:5000/products/search/freezable/0
# curl localhost:5000/products/search/freezable/1
# curl localhost:5000/products/search/validity/15
# curl localhost:5000/products/search/expired