import sys

from PyQt6.QtCore import Qt

from view.janela_principal import Ui_MainWindow
from model.usuario import Usuario
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets


class Principal(Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.push_button_salvar.clicked.connect(self.salvar)
        pixmap = QPixmap('img/logo.png')
        self.label_img_topo.setPixmap(pixmap.scaled(200,200, Qt.AspectRatioMode.KeepAspectRatio))
        self.lista_usuario = [] #banco de dados fake
        self.label_erro.hide()

    def salvar(self):
        nome = self.line_edit_nome.text()
        u = Usuario(nome)
        if not u.erro_gui:
            self.lista_usuario.append(u)
            #print(len(self.lista_usuario))
            #print(f'Nome: {nome}')
            self.enviar_dados_tabela()
            self.label_erro.hide()
        else:
            self.label_erro.setText(u.erro_gui)
            self.label_erro.show()
        
    def enviar_dados_tabela(self):
        linha_tabela = 0
        self.table_widget_nomes.setRowCount(len(self.lista_usuario))
        for user in self.lista_usuario:
            self.table_widget_nomes.setItem(linha_tabela, 0, QtWidgets.QTableWidgetItem(user.nome))
            linha_tabela += 1

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()