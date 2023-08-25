import sys

from model.residuo_solido import Residuo_Solido
from files.gerenciador_arq import Gerente_Arquivos

from gui_principal import Ui_MainWindow

from PyQt6.QtWidgets import QMainWindow,QApplication, QLabel, QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class Principal(Ui_MainWindow, QMainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.stacked_widget.setCurrentWidget(self.page_login)
        self.frame_erro_login.hide()
        self.frame_msg_erro.hide()
        self.line_edit_login.setFocus()#coloca o foco no line edit de login
        self.cor_sucesso = "background-color: rgb(209, 255, 209);"
        self.cor_erro = "background-color: rgb(250, 185, 185);"
        self.lista_residuos = []#banco fake
        self.lin_selecionada_tab = -1
        self.acoes = ['Cadastrar','Alterar']
        self.acao_tela_cadastro = -1
        ############## eventos ##############
        self.push_button_entrar.clicked.connect(self.realizar_login)
        self.push_button_logoff.clicked.connect(self.sair_sistema)
        self.push_button_salvar.clicked.connect(self.salvar_dados)
        self.pushButton_fechar_msg_login.clicked.connect(lambda : self.frame_erro_login.hide())
        self.table_widget_residuos.itemSelectionChanged.connect(self.atualizar_linha_selecionada)
        ############## paginação ##############
        self.push_button_cadastro.clicked.connect(self.paginar)
        self.push_button_listar.clicked.connect(self.paginar)
        self.push_button_voltar.clicked.connect(self.paginar)
        self.push_button_go_list.clicked.connect(self.paginar)
        self.push_button_voltar_pric.clicked.connect(self.paginar)
        self.push_button_alterar.clicked.connect(self.paginar)
        ############## definindo imagens aos labels ##############
        self.set_label_img(self.label_icon_login, 'img/icone_login.jpg')
        self.set_label_img(self.label_logo_principal, 'img/logo_empresa.png')
        self.set_label_img(self.label_img_logo,'img/logo_empresa.png')
        self.set_label_img(self.label_logo_page_listar, 'img/logo_empresa.png')
        ############## definindo icones para os botoes ##############
        self.push_button_logoff.setIcon(QIcon('img/shutdown.png'))
        self.push_button_alterar.setIcon(QIcon('img/edit.png'))
        self.push_button_deletar.setIcon(QIcon('img/delete.png'))
        self.push_button_voltar.setIcon(QIcon('img/home-button.png'))
        self.push_button_voltar_pric.setIcon(QIcon('img/home-button.png'))
        self.push_button_go_list.setIcon(QIcon('img/table.png'))

        # Definindo a tabela de materiais como não editavel
        self.table_widget_residuos.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.gerente_arquivos = Gerente_Arquivos()
        
    def paginar(self):
        obj = self.sender()
        if isinstance(obj, QPushButton):
            match obj.objectName():
                case 'push_button_cadastro':
                    #Saindo da page_principal -> page_cadastrar_materiais
                    self.limpar_campos()
                    self.frame_msg_erro.hide()
                    self.stacked_widget.setCurrentWidget(self.page_cadastrar_materiais)
                    self.acao_tela_cadastro = self.acoes[0]
                case 'push_button_listar':
                    #Saindo da page_principal -> page_listar_materiais
                    self.stacked_widget.setCurrentWidget(self.page_listar_materiais)
                case 'push_button_voltar':
                    # Saindo da page_listar_materiais -> page_principal
                    self.stacked_widget.setCurrentWidget(self.page_principal)
                case 'push_button_go_list':
                    # Saindo da page_cadastrar_materiais -> page_listar_materiais
                    self.stacked_widget.setCurrentWidget(self.page_listar_materiais)
                case 'push_button_voltar_pric':
                    # Saindo da page_cadastrar_materiais -> page_principal
                    self.stacked_widget.setCurrentWidget(self.page_principal)
                case 'push_button_alterar':
                    # Saindo da page_listar_materiais -> page_cadastrar_materiais
                    self.frame_msg_erro.hide()
                    item = self.lista_residuos[self.lin_selecionada_tab]
                    if isinstance(item, Residuo_Solido):
                        self.stacked_widget.setCurrentWidget(self.page_cadastrar_materiais)
                        self.acao_tela_cadastro = self.acoes[1]
                        self.line_edit_material.setText(item.material)
                        self.line_edit_quantidade.setText(str(item.quantidade))
                        if item.organico:
                            self.radio_button_sim.setChecked(item.organico)
                        else:
                            self.radio_button_nao.setChecked(not item.organico)


    def atualizar_linha_selecionada(self):
        selected_items = self.table_widget_residuos.selectedItems()
        if selected_items:
            self.lin_selecionada_tab = selected_items[0].row()
            print(f"Selected row: {self.lin_selecionada_tab}")

            # item_1 = self.table_widget_residuos.item(selected_row, 0).text()
            # item_2 = self.table_widget_residuos.item(selected_row, 1).text()
            # item_3 = self.table_widget_residuos.item(selected_row, 2).text()

    def salvar_dados(self):
        material   = self.line_edit_material.text()
        quantidade = self.line_edit_quantidade.text()
        if self.radio_button_sim.isChecked():
            organico = True
        elif self.radio_button_nao.isChecked():
            organico = False    
        else:
            organico = None

        if self.acao_tela_cadastro == self.acoes[0]:#Cadastrar
            residuo = Residuo_Solido(material, quantidade, organico)
            if not residuo.error:
                self.lista_residuos.append(residuo)
                self.gerente_arquivos.salvar_em_arquivo(residuo)
                self.mostrar_msg('Dados salvo com sucesso!', self.cor_sucesso)
                self.limpar_campos()
                self.line_edit_material.setFocus()
                self.enviar_dados_tabela()
        else:#Alterar
            residuo = self.lista_residuos[self.lin_selecionada_tab]
            residuo.material = material
            residuo.quantidade = quantidade
            residuo.organico = organico
            if not residuo.error:
                self.lista_residuos[self.lin_selecionada_tab] = residuo
                conteudo = ''.join([str(ref_obj)+'\n' for ref_obj in self.lista_residuos])
                self.gerente_arquivos.salvar_em_arquivo(conteudo, 'w')
                self.mostrar_msg('Dados alterado com sucesso!', self.cor_sucesso)
                self.line_edit_material.setFocus()
                self.enviar_dados_tabela()
        
        if residuo.error:
            self.mostrar_msg(residuo.error, self.cor_erro)


    def enviar_dados_tabela(self):
        cont_linhas = 0
        self.table_widget_residuos.setRowCount(len(self.lista_residuos))
        for ref_obj in self.lista_residuos:
            self.table_widget_residuos.setItem(cont_linhas, 0, QTableWidgetItem(ref_obj.material))
            self.table_widget_residuos.setItem(cont_linhas, 1, QTableWidgetItem(str(ref_obj.quantidade)))
            self.table_widget_residuos.setItem(cont_linhas, 2, QTableWidgetItem(str('Sim' if ref_obj.organico else 'Não')))
            cont_linhas += 1

    def set_label_img(self, label: QLabel, end_img: str):
        img = QPixmap(end_img)
        img = img.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(img)

    def mostrar_msg(self, msg: str, tipo_msg_css):
        self.frame_msg_erro.show()
        self.label_erro.setText(msg)
        self.label_erro.setStyleSheet(tipo_msg_css)

    def limpar_campos(self):
        self.line_edit_material.setText('')
        self.line_edit_quantidade.setText('')
        self.radio_button_sim.setAutoExclusive(False)
        self.radio_button_nao.setAutoExclusive(False)
        self.radio_button_sim.setChecked(False)
        self.radio_button_nao.setChecked(False)
        self.radio_button_sim.setAutoExclusive(True)
        self.radio_button_nao.setAutoExclusive(True)

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
            # self.label_erro_login.setText()
            self.mostrar_msg('Seu login ou senha estão incorretos!',self.cor_erro)
            self.frame_erro_login.show()

                  
if __name__ == '__main__':
    qt = QApplication(sys.argv)   
    principal = Principal()
    principal.show()
    qt.exec()