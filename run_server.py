from general.config import *
from models.product import *
from general.tools import *
from routes.read_product import *

@app.route("/")
def server():
    return "Stock management is working"

app.run(debug = True)