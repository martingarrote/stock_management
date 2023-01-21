from general.config import *
from models.product import *
from models.permission import *
from models.person import *

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()