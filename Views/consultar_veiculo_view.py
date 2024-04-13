from models.Veiculo_model import Veiculo
from services.db import session
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class ConsultarVeiculo(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaConsultaVeiculo.ui', self)
        self.show()

    def consultar(self):
        consulta = session.query(Veiculo).all()
        tabela = self.findChild(QtWidgets.QTableWidget, 'tabelaConsulta')
        tabela.setRowCount(len(consulta))

        for i, veiculos in enumerate(consulta):
            tabela.setItem(i, 0, QtWidgets.QTableWidgetItem(str(veiculos.NRPLACA)))
            tabela.setItem(i, 1, QtWidgets.QTableWidgetItem(str(veiculos.DSMODELO)))
            tabela.setItem(i, 2, QtWidgets.QTableWidgetItem(str(veiculos.TPTRACAO)))
            tabela.setItem(i, 3, QtWidgets.QTableWidgetItem(str(veiculos.NRRENAVAM)))
            tabela.setItem(i, 4, QtWidgets.QTableWidgetItem(str(veiculos.DTAQUISICAO)))
            tabela.setItem(i, 5, QtWidgets.QTableWidgetItem(str(veiculos.NRFROTA)))
            tabela.setItem(i, 6, QtWidgets.QTableWidgetItem(str(veiculos.NRCONJUNTO)))
            tabela.setItem(i, 7, QtWidgets.QTableWidgetItem(str(veiculos.NRCHASSI)))
            tabela.setItem(i, 8, QtWidgets.QTableWidgetItem(str(veiculos.TPCOMBUSTIVEL)))
            tabela.setItem(i, 9, QtWidgets.QTableWidgetItem(str(veiculos.ANOVEIC)))
            tabela.setItem(i, 10, QtWidgets.QTableWidgetItem(str(veiculos.DSMARCA)))
            tabela.setItem(i, 11, QtWidgets.QTableWidgetItem(str(veiculos.QTEIXO)))
            tabela.setItem(i, 12, QtWidgets.QTableWidgetItem(str(veiculos.TPVEICULO)))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ConsultarVeiculo()
    window.consultar()
    app.exec()