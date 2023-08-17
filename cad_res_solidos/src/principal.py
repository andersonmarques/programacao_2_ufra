import sys

from model.residuo_solido import Residuo_Solido

from gui_principal import Ui_MainWindow

from PyQt6.QtWidgets import QMainWindow,QApplication, QLabel, QTableWidgetItem
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class Principal(Ui_MainWindow, QMainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.lista_residuos = []#banco fake
        self.stacked_widget.setCurrentWidget(self.page_login)
        self.frame_erro_login.hide()
        self.frame_msg_erro.hide()
        self.line_edit_login.setFocus()#coloca o foco no line edit de login
        self.push_button_entrar.clicked.connect(self.realizar_login)
        self.push_button_logoff.clicked.connect(self.sair_sistema)
        self.pushButton_fechar_msg_login.clicked.connect(lambda : self.frame_erro_login.hide())
        self.push_button_cadastro.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page_cadastrar_materiais))
        self.push_button_listar.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page_listar_materiais))
        self.push_button_voltar.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page_principal))
        self.push_button_go_list.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page_listar_materiais))
        self.push_button_voltar_pric.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page_principal))
        self.push_button_salvar.clicked.connect(self.salvar_dados)
        
        self.set_label_img(self.label_icon_login, 'img/icone_login.jpg')
        self.set_label_img(self.label_logo_principal, 'img/logo_empresa.png')
        self.set_label_img(self.label_img_logo,'img/logo_empresa.png')
        self.set_label_img(self.label_logo_page_listar, 'img/logo_empresa.png')

        self.push_button_logoff.setIcon(QIcon('img/shutdown.png'))
        self.push_button_alterar.setIcon(QIcon('img/edit.png'))
        self.push_button_deletar.setIcon(QIcon('img/delete.png'))
        self.push_button_voltar.setIcon(QIcon('img/home-button.png'))
        self.push_button_voltar_pric.setIcon(QIcon('img/home-button.png'))
        self.push_button_go_list.setIcon(QIcon('img/table.png'))
        
    
    def salvar_dados(self):
        material   = self.line_edit_material.text()
        quantidade = self.line_edit_quantidade.text()
        organico   = True if self.radio_button_sim.isChecked() else False

        residuo = Residuo_Solido(material, int(quantidade), organico)

        if residuo.error != '':
            self.label_erro.setText(residuo.error)
            self.frame_msg_erro.show()
        else:
            self.lista_residuos.append(residuo)
            self.label_erro.setText('Dados salvo com sucesso!')
            self.frame_msg_erro.show()
            # self.limpar_campos()
            self.line_edit_material.setFocus()
            self.enviar_dados_tabela()

    def enviar_dados_tabela(self):
        cont_linhas = 0
        self.table_widget_residuos.setRowCount(
            len(self.lista_residuos))
        for ref_obj in self.lista_residuos:
            self.table_widget_residuos.setItem(
                cont_linhas, 0, QTableWidgetItem(
                ref_obj.material) )
            self.table_widget_residuos.setItem(
                cont_linhas, 1, QTableWidgetItem(
                str(ref_obj.quantidade)) )
            self.table_widget_residuos.setItem(
                cont_linhas, 2, QTableWidgetItem(
                str('Sim' if ref_obj.organico else 'Não')) )
            cont_linhas += 1

    def set_label_img(self, label: QLabel, end_img: str):
        img = QPixmap(end_img)
        img = img.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(img)

    def sair_sistema(self):
        self.stacked_widget.setCurrentWidget(self.page_login)
       
    def realizar_login (self):
        '''Realizar o login do usuário'''
        login = self.line_edit_login.text()#recupera o texto do line edit
        senha = self.line_edit_senha.text()
        if login == 'admin' and senha == '12345':
            self.line_edit_login.setText('')
            self.line_edit_senha.setText('')
            self.frame_erro_login.hide()
            self.stacked_widget.setCurrentWidget(self.page_principal)
        else:
            self.label_erro_login.setText('Seu login ou senha estão incorretos!')
            self.frame_erro_login.show()

                  
if __name__ == '__main__':
    qt = QApplication(sys.argv)   
    principal = Principal()
    principal.show()
    qt.exec()