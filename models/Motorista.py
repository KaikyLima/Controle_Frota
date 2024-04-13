from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, ForeignKey
from models.Base import Base
<<<<<<< HEAD
=======
from models.Pessoa import Pessoa
>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6
from models.Funcionario import Funcionario
class Motorista(Base):
    __tablename__ = "MOTORISTA"
    IDMOTORISTA:   Mapped[int]      = mapped_column(INTEGER,      nullable=False, primary_key=True)
    NMMOTORISTA:   Mapped[str]      = mapped_column(VARCHAR(100), nullable=False)
    TPSITUACAO:    Mapped[str]      = mapped_column(VARCHAR(100), nullable=False)
    FUNCIONARIO_NRMATRICULA:   Mapped[int]      = mapped_column(INTEGER, ForeignKey(Funcionario.NRMATRICULA), nullable=False)