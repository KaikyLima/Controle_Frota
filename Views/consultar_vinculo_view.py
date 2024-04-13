from services.db import session
from models.CtVinculo import CtVinculo
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from models.Motorista import Motorista
from models.Veiculo_model import Veiculo

class ConsultarVinculos(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('telaConsultaVinculo.ui', self)
        self.show()

    def consultar(self):
        vinculos = session.query(CtVinculo).all()
        tabela = self.findChild(QtWidgets.QTableWidget, 'tabelaConsulta')
        tabela.setRowCount(len(vinculos))
        for i, vinculo in enumerate(vinculos):
            tabela.setItem(i, 0, QtWidgets.QTableWidgetItem(str(vinculo.DTVINCULO)))
            tabela.setItem(i, 1, QtWidgets.QTableWidgetItem(str(vinculo.DTDESVINCULO)))
            frota = session.query(Veiculo).filter_by(IDVEICULO=vinculo.VEICULO_IDVEICULO).first()
            tabela.setItem(i, 2, QtWidgets.QTableWidgetItem(str(frota.NRFROTA) if frota else ""))
            motorista = session.query(Motorista).filter_by(IDMOTORISTA=vinculo.MOTORISTA_IDMOTORISTA).first()
            tabela.setItem(i, 3, QtWidgets.QTableWidgetItem(str(motorista.NMMOTORISTA) if motorista else ""))
        print("tsstststs")




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ConsultarVinculos()
    window.consultar()
    app.exec()
