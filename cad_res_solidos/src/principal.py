import sys

from model.residuo_solido import Residuo_Solido

from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class Principal(Ui_MainWindow, QMainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.lista_residuos = []
        self.frame_erro_login.hide()
        self.frame_msg_erro.hide()
        self.line_edit_login.setFocus()#coloca o foco no line edit de login
        self.push_button_entrar.clicked.connect(self.realizar_login)
        self.pushButton_fechar_msg_login.clicked.connect(lambda : self.frame_erro_login.hide())
        self.push_button_logoff.clicked.connect(self.sair_sistema)
        self.push_button_cadastro.clicked.connect(self.abrir_tela_cadastro)
        self.push_button_salvar.clicked.connect(self.salvar_dados)
        img_login = self.recalcular_tam_imagem('img/icone_login.jpg'
                                               , self.label_icon_login.width(),
                                                self.label_img_logo.height()
                                   )
        img_logo = self.recalcular_tam_imagem('img/logo_empresa.png'
                                                  , self.label_img_logo.width(),
                                                    self.label_img_logo.height()
                                      )
        self.label_img_logo.setPixmap(img_logo)
        img_logo_princ = self.recalcular_tam_imagem('img/logo_empresa.png'
                                                    , self.label_logo_principal.width(),
                                                        self.label_logo_principal.height()
                                        )
        self.label_logo_principal.setPixmap(img_logo_princ)
        self.label_icon_login.setPixmap(img_login)
        icon = QIcon('img/shutdown.png')
        self.push_button_logoff.setIcon(icon)

    def salvar_dados(self):
        material = self.line_edit_material.text()
        quantidade = self.line_edit_quantidade.text()
        organico = True if self.radio_button_sim.isChecked() else False
        
        residuo = Residuo_Solido(material, int(quantidade), organico)
        if residuo.error != '':
            self.label_erro.setText(residuo.error)
            self.frame_msg_erro.show()
        else:
            self.lista_residuos.append(residuo)
            self.label_erro.setText('Dados salvos com sucesso!')
            self.frame_msg_erro.show()
            # self.limpar_campos()
            self.line_edit_material.setFocus()

    def recalcular_tam_imagem(self, end_imagem: str, w: int = 16, h: int = 16):
        '''Recalcula o tamanho da imagem para o tamanho do label, 
        com aspecto proporcional. Se nenhum tamanho for passado, serão 
        utilizados os valores 16x16'''
        logo = QPixmap(end_imagem)
        logo = logo.scaled(w, h, 
                           Qt.AspectRatioMode.KeepAspectRatio)
        return logo

    def sair_sistema(self):
        self.stacked_widget.setCurrentWidget(self.page_login)

    def abrir_tela_cadastro(self):
        self.stacked_widget.setCurrentWidget(self.page_cadastrar_materiais)

    def abrir_tela_listar_dados(self):
        pass

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