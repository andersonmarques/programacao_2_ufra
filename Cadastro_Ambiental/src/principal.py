import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow
from controller.gerenciador_projeto import Gerenciador_Projeto
from model.projeto import Projeto
from view.gui_qt import Ui_MainWindow

class Principal (QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self) 
        self.init_components()
        self.gerenciador = Gerenciador_Projeto()

    def init_components(self):
        self.frame_msg.hide()
        # self.label_logo.setPixmap(QPixmap('img/logo.png'))
        self.setWindowTitle('Cadastro de projetos')
        self.label_logo.setPixmap(QPixmap(r'img\logo.png'))
        self.setWindowIcon(QIcon(r'img\icone.png'))
        self.pushButton_msg.clicked.connect(lambda: self.frame_msg.hide())
        self.pushButton_cadastrar.clicked.connect(self.cadastrar_projeto)
        self.pushButton_retirar.clicked.connect(self.retirar_projeto)

    def cadastrar_projeto(self):
        p = Projeto()
        if not p.erro:
            p.identificacao = self.lineEdit_id.text()
            p.custo_obra = self.lineEdit_custo.text()
            msg = self.gerenciador.cadastrar_projeto(p)
            self.frame_msg.show()
            self.label_msg.setText(msg)
            self.listar_projetos()
        else:
            self.frame_msg.show()
            self.label_msg.setText(p.erro)

    def retirar_projeto(self):
        msg, validador = self.gerenciador.desempilhar_projeto()
        if validador:
            self.frame_msg.show()
            self.label_msg.setText(msg)
            self.listar_projetos()
        else:
            self.frame_msg.show()
            self.label_msg.setText(msg)

    def listar_projetos(self):
        linha_tabela = 0
        self.tableWidget_saida.setRowCount(len(self.gerenciador.pilha))
        for projeto in self.gerenciador.pilha:
            self.tableWidget_saida.
            setItem(linha_tabela, 0, QtWidgets.QTableWidgetItem(projeto.identificacao))
            self.tableWidget_saida.setItem(linha_tabela, 1, QtWidgets.QTableWidgetItem(projeto.custo_obra))
            linha_tabela += 1

if __name__ == '__main__':
    qt = QApplication(sys.argv)   
    principal = Principal()
    principal.show()
    qt.exec()