<<<<<<< HEAD
from utils.create_db import create_db
from services.db import session

if __name__ == "__main__":
    """create_db()"""
    print("Teste")


=======
from models.Classificacao import Classificacao
from utils.create_db import create_db
from services.db import session

if __name__ == "__main__":
    """create_db()"""
    print("Teste")

    response = session.query(Classificacao)

    for classificacao in response:
        print(classificacao.IDCLASSIFICACAO)
        print(classificacao.DSCLASSIFICACAO)
>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6
