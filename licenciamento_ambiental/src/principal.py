import sys
from tela_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from diagnostico_ambiental import Diagnostico_Ambiental

class Principal (QMainWindow, Ui_MainWindow):
    #inicializando o objeto da classe Principal
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.frame_msg.hide()
        logo = QPixmap('img/ufra_logo.png')#criando o obj da imagem
        logo = logo.scaled(self.label_logo_emp.width(),
                           self.label_logo_emp.height(), 
                           Qt.AspectRatioMode.KeepAspectRatio)
        self.label_logo_emp.setPixmap(logo)#enviando a imagem ao label
        self.push_button_salvar.clicked.connect(self.salvar_lista)
        self.push_button_fechar.clicked.connect(lambda : self.frame_msg.hide())
        self.lista = []
        
    def salvar_lista(self):
        empreendimento = self.line_edit_empreendimento.text()
        matricula = self.line_edit_area_matricula.text()
        area = self.line_edit_area.text()
        
        diagnostico = Diagnostico_Ambiental(empreendimento,
                                            matricula,
                                            area)        
        self.lista.append(diagnostico)
        #self.imprime_mensagem()
        self.atualizar_tabela()

    def atualizar_tabela(self):
        self.table_widget_saida.setRowCount(0)
        num_linhas = self.table_widget_saida.rowCount()
        for obj in self.lista:
            self.table_widget_saida.insertRow(num_linhas)
            self.table_widget_saida.setItem(num_linhas, 0, 
            QtWidgets.QTableWidgetItem(obj.empreendimento))
            self.table_widget_saida.setItem(num_linhas, 1, 
            QtWidgets.QTableWidgetItem(obj.matricula))
            self.table_widget_saida.setItem(num_linhas, 2, 
            QtWidgets.QTableWidgetItem(obj.area))
            num_linhas += 1


    def imprime_mensagem(self):
        saida = ""
        for d in self.lista:#varrendo a lista de diagnostico ambiental
            saida += f'{d.empreendimento}\n{d.matricula}\n{d.area}\n\n'
        
        #self.text_edit_saida.setText(saida)


if __name__ == '__main__': 
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()