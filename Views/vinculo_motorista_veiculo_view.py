from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from services.db import session
from models.CtVinculo import CtVinculo
from models.Motorista import Motorista
from models.Funcionario import Funcionario
from models.Veiculo_model import Veiculo
<<<<<<< HEAD
=======
from sqlalchemy import func
>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6
import datetime

class DesvincularMotorista(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaCtDesvinculo.ui', self)
        self.botaoSalvar.clicked.connect(self.desvincular_motorista)
<<<<<<< HEAD
        self.nrFrota.textChanged.connect(self.preencher_placa)
        self.matriculaMotorista.textChanged.connect(self.preencher_motorista)
        self.show()

    def preencher_placa(self):
        nrFrota = self.nrFrota.text()
        response = session.query(Veiculo).filter(Veiculo.NRFROTA == nrFrota).first()
        if response is not None:
            self.nrPlacaFrota.setText(response.NRPLACA)
        else:
            self.nrPlacaFrota.clear()

    def preencher_motorista(self):
        matriculaMotorista = self.matriculaMotorista.text()
        response = session.query(Motorista).join(Funcionario,
                                                 Funcionario.NRMATRICULA == Motorista.FUNCIONARIO_NRMATRICULA).filter(
            Motorista.FUNCIONARIO_NRMATRICULA == matriculaMotorista ).first()
        if response is not None:
            self.nmMotorista.setText(response.NMMOTORISTA)
        else:
            self.nmMotorista.clear()

    def desvincular_motorista(self):
        try:
            dtDesvinculo = self.dtDesvinculo.date().toPyDate()
            nrMatricula  = self.matriculaMotorista.text()
            nrFrota      = self.nrFrota.text()
=======
        self.show()

    def desvincular_motorista(self):
        try:
            dtDesvinculo = self.dtDesvinculo.date().toPyDate()
            nrMatricula = self.matriculaMotorista.text()
            nrFrota = self.nrFrota.text()
>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6

            # Localize o ID do vinculo com os atributos fornecidos e DTDESVINCULO nulo
            idVinculo = self.localizar_id_vinculo(nrFrota, nrMatricula)
            if idVinculo is None:
                raise ValueError("Vinculo não encontrado ou já desvinculado.")

            if not self.dataDesvinculo(dtDesvinculo):
                raise ValueError("A data de desvinculo não pode ser superior e nem inferior a data atual")

            vinculo = session.query(CtVinculo).get(idVinculo)
            if dtDesvinculo < vinculo.DTVINCULO:
                raise ValueError("A data de desvinculo não pode ser inferior a data de vinculo")

            # Atualize o campo DTDESENGATE com a nova data
            vinculo = session.query(CtVinculo).get(idVinculo)
            vinculo.DTDESVINCULO = dtDesvinculo
            session.commit()

            QMessageBox.information(self, "Sucesso", "Data de desvinculo atualizada com sucesso!")
<<<<<<< HEAD
            self.limpar_campos()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao atualizar data de desvinculo: {str(e)}")

    def limpar_campos(self):  # Função para limpar a tela ao terminar o cadastro

        self.dtDesvinculo.clear()
        self.matriculaMotorista.clear()
        self.nrFrota.clear()

    #Verificando se possui mais de 1 vinculo por pessoa e/ou veiculo
    def localizar_id_vinculo(self, nrFrota, nrMatricula):
        veiculo   = session.query(Veiculo).filter(Veiculo.NRFROTA == nrFrota).first()
=======
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao atualizar data de desvinculo: {str(e)}")


    #Verificando se possui mais de 1 vinculo por pessoa e/ou veiculo
    def localizar_id_vinculo(self, nrFrota, nrMatricula):
        veiculo = session.query(Veiculo).filter(Veiculo.NRFROTA == nrFrota).first()
>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6
        motorista = session.query(Motorista).join(Funcionario,
                                                  Funcionario.NRMATRICULA == Motorista.FUNCIONARIO_NRMATRICULA).filter(
            Motorista.FUNCIONARIO_NRMATRICULA == nrMatricula).first()

        if veiculo is None or motorista is None:
            return None

        vinculos = session.query(CtVinculo).filter(
            CtVinculo.VEICULO_IDVEICULO == veiculo.IDVEICULO,
            CtVinculo.MOTORISTA_IDMOTORISTA == motorista.IDMOTORISTA,
            CtVinculo.DTDESVINCULO.is_(None)
        ).all()

        if len(vinculos) > 1:
            raise ValueError("Múltiplos vínculos ativos encontrados para o mesmo motorista e veículo.")
        elif len(vinculos) == 0:
            return None
        else:
            return vinculos[0].ID
    def dataDesvinculo(self, dtDesvinculo):
        diaDesvinculo = datetime.date.today()
        return diaDesvinculo == dtDesvinculo


class VincularMotorista(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaCtVinculo.ui', self)
        self.criando_novo_vinculo()
        self.botaoTelaDesvinculo.clicked.connect(self.chamar_tela_desvinculo)
<<<<<<< HEAD
        self.nrFrota.textChanged.connect(self.preencher_placa)
        self.matriculaMotorista.textChanged.connect(self.preencher_motorista)
        self.show()
        self.desvincula_view = None


    def preencher_placa(self):
        nrFrota = self.nrFrota.text()
        response = session.query(Veiculo).filter(Veiculo.NRFROTA == nrFrota).first()
        if response is not None:
            self.nrPlacaFrota.setText(response.NRPLACA)
        else:
            self.nrPlacaFrota.clear()

    def preencher_motorista(self):
        matriculaMotorista = self.matriculaMotorista.text()
        response = session.query(Motorista).join(Funcionario,
                                                 Funcionario.NRMATRICULA == Motorista.FUNCIONARIO_NRMATRICULA).filter(
            Motorista.FUNCIONARIO_NRMATRICULA == matriculaMotorista).first()
        if response is not None:
            self.nmMotorista.setText(response.NMMOTORISTA)
        else:
            self.nmMotorista.clear()

=======
        self.show()
        self.desvincula_view = None

>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6
    def criando_novo_vinculo(self):
        self.botaoSalvar.clicked.connect(self.criando_vinculo_motorista)

    #Procurando o id do motorista na tabela Motorista através do número de matricula fornecido pelo usuário
    @staticmethod
    def procurar_motorista(nrMatricula):
        response = session.query(Motorista).join(Funcionario,
                                                 Funcionario.NRMATRICULA == Motorista.FUNCIONARIO_NRMATRICULA).filter(
            Motorista.FUNCIONARIO_NRMATRICULA == nrMatricula).first()
        id_motorista = response.IDMOTORISTA

        return id_motorista

    #Procurando o id do veiculo atraves do número de frota informado
    @staticmethod
    def procurar_frota(nrFrota):
<<<<<<< HEAD
        response   = session.query(Veiculo).filter(Veiculo.NRFROTA == nrFrota).first()
=======
        response = session.query(Veiculo).filter(Veiculo.NRFROTA == nrFrota).first()
>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6
        id_veiculo = response.IDVEICULO
        return id_veiculo

    #Verificando se a frota informado passui vinculo ativo
    def vinculado_or_no_frota(self, nrFrota):
        id_veiculo = VincularMotorista.procurar_frota(nrFrota)

        vinculos = session.query(CtVinculo.ID).filter(
            CtVinculo.VEICULO_IDVEICULO == id_veiculo,
            CtVinculo.DTDESVINCULO == None
        ).all()

<<<<<<< HEAD
        print("Quantidade de Veículos: ", vinculos)
=======
        print("quantidade achada veiculos: ", vinculos)
>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6

        return len(vinculos)

    #Verificando se o motorista informado já possui vinculo ativo
    def vinculado_or_no_motorista(self, nrMatricula):
        id_motorista = int(VincularMotorista.procurar_motorista(nrMatricula))
        print(f"\n \n \n ID motorista {id_motorista}")
        print(f"ID's motorista banco {session.query(CtVinculo.MOTORISTA_IDMOTORISTA)}")

        vinculos = session.query(CtVinculo.ID).filter(
            CtVinculo.MOTORISTA_IDMOTORISTA == id_motorista,
            CtVinculo.DTDESVINCULO == None
        ).all()

<<<<<<< HEAD
        print("Quantidade achada motorista: ", len(vinculos))
=======
        print("quantidade achada motorista: ", len(vinculos))
>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6
        print("Lista de vinculos", vinculos)

        return len(vinculos)

    #Impedindo o vinculo com datas superior ou inferior ao dia atual
    def dataVinculo(self, dtVinculo):
        diaVinculo = datetime.date.today()
        return diaVinculo == dtVinculo

    def criando_vinculo_motorista(self):
        try:
            dtVinculo = self.dtVinculo.date().toPyDate()
            nrMatricula = self.matriculaMotorista.text()
            nrFrota = self.nrFrota.text()
            self.desvinculo_view = None

            id_motorista = VincularMotorista.procurar_motorista(nrMatricula)
            id_veiculo = VincularMotorista.procurar_frota(nrFrota)

            erros = []

            if self.vinculado_or_no_frota(nrFrota) > 0:
<<<<<<< HEAD
                erros.append("Veículo já vinculado")

            if self.vinculado_or_no_motorista(nrMatricula) > 0:
                erros.append("Motorista já vinculado")
            if not self.dataVinculo(dtVinculo):
                erros.append("A data de vínculo não pode ser superior e nem inferior a data atual")
=======
                erros.append("veiculo já vinculado")

            if self.vinculado_or_no_motorista(nrMatricula) > 0:
                erros.append("motorista já vinculado")
            if not self.dataVinculo(dtVinculo):
                erros.append("A data de vinculo não pode ser supeior e nem inferior a data atual")
>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6

            if erros:
                QMessageBox.critical(self, "Erro", "\n".join(erros))
                return

<<<<<<< HEAD
            print(f"Data vínculo: {dtVinculo} \n IDMOTORISTA: {id_motorista} \n IDVEICULO: {id_veiculo}")
=======
            print(f"Data vinculo: {dtVinculo} \n IDMOTORISTA: {id_motorista} \n IDVEICULO: {id_veiculo}")
>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6
            novo_vinculo = CtVinculo(DTVINCULO=dtVinculo, DTDESVINCULO=None,
                                     MOTORISTA_IDMOTORISTA=id_motorista, VEICULO_IDVEICULO=id_veiculo)
            session.add(novo_vinculo)
            session.commit()

            QMessageBox.information(self, "Sucesso", "Motorista vinculado!")
<<<<<<< HEAD

            self.limpar_campos()  # Função para limpar a tela ao terminar o cadastro

=======
>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao criar vínculo: {str(e)}")

    def limpar_campos(self):  # Função para limpar a tela ao terminar o cadastro

        self.dtVinculo.clear()
<<<<<<< HEAD
        self.matriculaMotorista.clear()
        self.nrFrota.clear()
=======
        self.nrMatricula.clear()
        self.nrFrota.clear()

    # def verificar_data(self, dtVinculo):

>>>>>>> a1c7f847f596861dbdff6cc5c5c8c5b943b76ba6
    def chamar_tela_desvinculo(self):
        if not self.desvincula_view:
            self.desvincula_view = DesvincularMotorista()
        self.desvincula_view.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = VincularMotorista()
    app.exec()
