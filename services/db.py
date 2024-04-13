from urllib.parse import quote
from sqlalchemy import create_engine, text
import cx_Oracle
from sqlalchemy.orm import sessionmaker

lib_dir = "C:\oracle\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)

USER = 'system'
PASSWD = quote('ksl1708')
HOST = 'localhost'
PORT = 1521
SID = "xe"

sid = cx_Oracle.makedsn(HOST, PORT, sid=SID)
instance = f"oracle+cx_oracle://{USER}:{PASSWD}@{sid}"

engine = create_engine(instance, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

usuario = "C##CTFROTA"
session.execute(text(f"ALTER SESSION SET CURRENT_SCHEMA = {usuario}"))

<<<<<<< HEAD
'''result = session.execute(text("SELECT * FROM C##CTFROTA.MOTORISTA"))
=======
'''result = session.execute(text("SELECT * FROM C##CTFROTA.veiculo"))
>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6
for row in result:
    print(row)'''
