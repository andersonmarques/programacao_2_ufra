# Form implementation generated from reading ui file 'gui_principal.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(921, 676)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stacked_widget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stacked_widget.setGeometry(QtCore.QRect(10, 10, 891, 631))
        self.stacked_widget.setObjectName("stacked_widget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.frame_2 = QtWidgets.QFrame(parent=self.page_login)
        self.frame_2.setGeometry(QtCore.QRect(200, 60, 461, 291))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line_edit_senha = QtWidgets.QLineEdit(parent=self.frame_2)
        self.line_edit_senha.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.line_edit_senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_edit_senha.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_edit_senha.setObjectName("line_edit_senha")
        self.gridLayout_3.addWidget(self.line_edit_senha, 2, 1, 1, 1)
        self.push_button_entrar = QtWidgets.QPushButton(parent=self.frame_2)
        self.push_button_entrar.setObjectName("push_button_entrar")
        self.gridLayout_3.addWidget(self.push_button_entrar, 4, 1, 1, 1)
        self.label_icon_login = QtWidgets.QLabel(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_icon_login.sizePolicy().hasHeightForWidth())
        self.label_icon_login.setSizePolicy(sizePolicy)
        self.label_icon_login.setMinimumSize(QtCore.QSize(141, 141))
        self.label_icon_login.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_icon_login.setText("")
        self.label_icon_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_icon_login.setObjectName("label_icon_login")
        self.gridLayout_3.addWidget(self.label_icon_login, 0, 1, 1, 1)
        self.line_edit_login = QtWidgets.QLineEdit(parent=self.frame_2)
        self.line_edit_login.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.line_edit_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_edit_login.setObjectName("line_edit_login")
        self.gridLayout_3.addWidget(self.line_edit_login, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.frame_erro_login = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_erro_login.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_erro_login.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_erro_login.setObjectName("frame_erro_login")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_erro_login)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_erro_login = QtWidgets.QLabel(parent=self.frame_erro_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_erro_login.sizePolicy().hasHeightForWidth())
        self.label_erro_login.setSizePolicy(sizePolicy)
        self.label_erro_login.setMinimumSize(QtCore.QSize(0, 25))
        self.label_erro_login.setStyleSheet("background-color: rgb(255, 96, 117);")
        self.label_erro_login.setObjectName("label_erro_login")
        self.horizontalLayout_2.addWidget(self.label_erro_login)
        self.pushButton_fechar_msg_login = QtWidgets.QPushButton(parent=self.frame_erro_login)
        self.pushButton_fechar_msg_login.setObjectName("pushButton_fechar_msg_login")
        self.horizontalLayout_2.addWidget(self.pushButton_fechar_msg_login)
        self.gridLayout_3.addWidget(self.frame_erro_login, 3, 0, 1, 3)
        self.stacked_widget.addWidget(self.page_login)
        self.page_principal = QtWidgets.QWidget()
        self.page_principal.setObjectName("page_principal")
        self.frame_4 = QtWidgets.QFrame(parent=self.page_principal)
        self.frame_4.setGeometry(QtCore.QRect(20, 90, 811, 281))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.push_button_cadastro = QtWidgets.QPushButton(parent=self.frame_4)
        self.push_button_cadastro.setGeometry(QtCore.QRect(340, 140, 91, 71))
        self.push_button_cadastro.setObjectName("push_button_cadastro")
        self.push_button_listar = QtWidgets.QPushButton(parent=self.frame_4)
        self.push_button_listar.setGeometry(QtCore.QRect(340, 60, 91, 71))
        self.push_button_listar.setObjectName("push_button_listar")
        self.push_button_logoff = QtWidgets.QPushButton(parent=self.frame_4)
        self.push_button_logoff.setGeometry(QtCore.QRect(680, 90, 91, 71))
        self.push_button_logoff.setObjectName("push_button_logoff")
        self.label_logo_principal = QtWidgets.QLabel(parent=self.frame_4)
        self.label_logo_principal.setGeometry(QtCore.QRect(40, 20, 101, 71))
        self.label_logo_principal.setObjectName("label_logo_principal")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(40, 110, 171, 16))
        self.label_5.setObjectName("label_5")
        self.stacked_widget.addWidget(self.page_principal)
        self.page_listar_materiais = QtWidgets.QWidget()
        self.page_listar_materiais.setObjectName("page_listar_materiais")
        self.frame_tabela = QtWidgets.QFrame(parent=self.page_listar_materiais)
        self.frame_tabela.setGeometry(QtCore.QRect(10, 20, 831, 431))
        self.frame_tabela.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tabela.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tabela.setObjectName("frame_tabela")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_tabela)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_acao = QtWidgets.QFrame(parent=self.frame_tabela)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_acao.sizePolicy().hasHeightForWidth())
        self.frame_acao.setSizePolicy(sizePolicy)
        self.frame_acao.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_acao.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_acao.setObjectName("frame_acao")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_acao)
        self.verticalLayout.setObjectName("verticalLayout")
        self.push_button_voltar = QtWidgets.QPushButton(parent=self.frame_acao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_voltar.sizePolicy().hasHeightForWidth())
        self.push_button_voltar.setSizePolicy(sizePolicy)
        self.push_button_voltar.setObjectName("push_button_voltar")
        self.verticalLayout.addWidget(self.push_button_voltar)
        self.push_button_alterar = QtWidgets.QPushButton(parent=self.frame_acao)
        self.push_button_alterar.setObjectName("push_button_alterar")
        self.verticalLayout.addWidget(self.push_button_alterar)
        self.push_button_deletar = QtWidgets.QPushButton(parent=self.frame_acao)
        self.push_button_deletar.setObjectName("push_button_deletar")
        self.verticalLayout.addWidget(self.push_button_deletar)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout_2.addWidget(self.frame_acao, 1, 2, 1, 1)
        self.label_topo_page_listar = QtWidgets.QLabel(parent=self.frame_tabela)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_topo_page_listar.sizePolicy().hasHeightForWidth())
        self.label_topo_page_listar.setSizePolicy(sizePolicy)
        self.label_topo_page_listar.setObjectName("label_topo_page_listar")
        self.gridLayout_2.addWidget(self.label_topo_page_listar, 0, 1, 1, 2)
        self.label_logo_page_listar = QtWidgets.QLabel(parent=self.frame_tabela)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.label_logo_page_listar.sizePolicy().hasHeightForWidth())
        self.label_logo_page_listar.setSizePolicy(sizePolicy)
        self.label_logo_page_listar.setMinimumSize(QtCore.QSize(70, 70))
        self.label_logo_page_listar.setObjectName("label_logo_page_listar")
        self.gridLayout_2.addWidget(self.label_logo_page_listar, 0, 0, 1, 1)
        self.table_widget_residuos = QtWidgets.QTableWidget(parent=self.frame_tabela)
        self.table_widget_residuos.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_widget_residuos.sizePolicy().hasHeightForWidth())
        self.table_widget_residuos.setSizePolicy(sizePolicy)
        self.table_widget_residuos.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_widget_residuos.setAlternatingRowColors(True)
        self.table_widget_residuos.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.table_widget_residuos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_widget_residuos.setObjectName("table_widget_residuos")
        self.table_widget_residuos.setColumnCount(3)
        self.table_widget_residuos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_residuos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_residuos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_residuos.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.table_widget_residuos, 1, 0, 1, 2)
        self.stacked_widget.addWidget(self.page_listar_materiais)
        self.page_cadastrar_materiais = QtWidgets.QWidget()
        self.page_cadastrar_materiais.setObjectName("page_cadastrar_materiais")
        self.frame_fundo = QtWidgets.QFrame(parent=self.page_cadastrar_materiais)
        self.frame_fundo.setGeometry(QtCore.QRect(30, 30, 861, 241))
        self.frame_fundo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_fundo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_fundo.setObjectName("frame_fundo")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.frame_fundo)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 90, 641, 150))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line_edit_material = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.line_edit_material.setObjectName("line_edit_material")
        self.gridLayout.addWidget(self.line_edit_material, 0, 1, 1, 2)
        self.line_edit_quantidade = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.line_edit_quantidade.setObjectName("line_edit_quantidade")
        self.gridLayout.addWidget(self.line_edit_quantidade, 1, 1, 1, 2)
        self.radio_button_sim = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radio_button_sim.setObjectName("radio_button_sim")
        self.gridLayout.addWidget(self.radio_button_sim, 2, 1, 1, 1)
        self.radio_button_nao = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radio_button_nao.setObjectName("radio_button_nao")
        self.gridLayout.addWidget(self.radio_button_nao, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.push_button_salvar = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.push_button_salvar.setObjectName("push_button_salvar")
        self.gridLayout.addWidget(self.push_button_salvar, 5, 1, 1, 2)
        self.label_img_logo = QtWidgets.QLabel(parent=self.frame_fundo)
        self.label_img_logo.setGeometry(QtCore.QRect(10, 0, 91, 81))
        self.label_img_logo.setObjectName("label_img_logo")
        self.frame_msg_erro = QtWidgets.QFrame(parent=self.frame_fundo)
        self.frame_msg_erro.setGeometry(QtCore.QRect(130, 0, 651, 80))
        self.frame_msg_erro.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_msg_erro.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_msg_erro.setObjectName("frame_msg_erro")
        self.push_button_msg_fechar = QtWidgets.QPushButton(parent=self.frame_msg_erro)
        self.push_button_msg_fechar.setGeometry(QtCore.QRect(590, 20, 41, 41))
        self.push_button_msg_fechar.setObjectName("push_button_msg_fechar")
        self.label_erro = QtWidgets.QLabel(parent=self.frame_msg_erro)
        self.label_erro.setGeometry(QtCore.QRect(10, 30, 551, 20))
        self.label_erro.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.label_erro.setObjectName("label_erro")
        self.layoutWidget = QtWidgets.QWidget(parent=self.frame_fundo)
        self.layoutWidget.setGeometry(QtCore.QRect(660, 90, 192, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.push_button_voltar_pric = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_voltar_pric.sizePolicy().hasHeightForWidth())
        self.push_button_voltar_pric.setSizePolicy(sizePolicy)
        self.push_button_voltar_pric.setMinimumSize(QtCore.QSize(190, 0))
        self.push_button_voltar_pric.setObjectName("push_button_voltar_pric")
        self.verticalLayout_2.addWidget(self.push_button_voltar_pric)
        self.push_button_go_list = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_go_list.sizePolicy().hasHeightForWidth())
        self.push_button_go_list.setSizePolicy(sizePolicy)
        self.push_button_go_list.setMinimumSize(QtCore.QSize(190, 0))
        self.push_button_go_list.setObjectName("push_button_go_list")
        self.verticalLayout_2.addWidget(self.push_button_go_list)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.stacked_widget.addWidget(self.page_cadastrar_materiais)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stacked_widget.setCurrentIndex(2)
        self.push_button_msg_fechar.clicked.connect(self.frame_msg_erro.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.line_edit_login, self.line_edit_senha)
        MainWindow.setTabOrder(self.line_edit_senha, self.push_button_entrar)
        MainWindow.setTabOrder(self.push_button_entrar, self.pushButton_fechar_msg_login)
        MainWindow.setTabOrder(self.pushButton_fechar_msg_login, self.push_button_listar)
        MainWindow.setTabOrder(self.push_button_listar, self.push_button_cadastro)
        MainWindow.setTabOrder(self.push_button_cadastro, self.push_button_logoff)
        MainWindow.setTabOrder(self.push_button_logoff, self.push_button_alterar)
        MainWindow.setTabOrder(self.push_button_alterar, self.push_button_deletar)
        MainWindow.setTabOrder(self.push_button_deletar, self.table_widget_residuos)
        MainWindow.setTabOrder(self.table_widget_residuos, self.line_edit_material)
        MainWindow.setTabOrder(self.line_edit_material, self.line_edit_quantidade)
        MainWindow.setTabOrder(self.line_edit_quantidade, self.radio_button_sim)
        MainWindow.setTabOrder(self.radio_button_sim, self.radio_button_nao)
        MainWindow.setTabOrder(self.radio_button_nao, self.push_button_msg_fechar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.line_edit_senha.setPlaceholderText(_translate("MainWindow", "Insira sua senha"))
        self.push_button_entrar.setText(_translate("MainWindow", "Entrar"))
        self.line_edit_login.setPlaceholderText(_translate("MainWindow", "Inseria seu login"))
        self.label_erro_login.setText(_translate("MainWindow", "Login ou senha incorretos!"))
        self.pushButton_fechar_msg_login.setText(_translate("MainWindow", "X"))
        self.push_button_cadastro.setText(_translate("MainWindow", "Cadastrar"))
        self.push_button_listar.setText(_translate("MainWindow", "Listar"))
        self.push_button_logoff.setText(_translate("MainWindow", "Sair"))
        self.label_logo_principal.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.push_button_voltar.setText(_translate("MainWindow", "Home"))
        self.push_button_alterar.setText(_translate("MainWindow", "Alterar"))
        self.push_button_deletar.setText(_translate("MainWindow", "Excluir"))
        self.label_topo_page_listar.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Resíduos Sólidos Cadastrados</span></p></body></html>"))
        self.label_logo_page_listar.setText(_translate("MainWindow", "TextLabel"))
        item = self.table_widget_residuos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Material"))
        item = self.table_widget_residuos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantidade (kg)"))
        item = self.table_widget_residuos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Organico"))
        self.radio_button_sim.setText(_translate("MainWindow", "Sim"))
        self.radio_button_nao.setText(_translate("MainWindow", "Não"))
        self.label_4.setText(_translate("MainWindow", "Quantidade (kg):"))
        self.label_2.setText(_translate("MainWindow", "Organico?"))
        self.label_3.setText(_translate("MainWindow", "Material:"))
        self.push_button_salvar.setText(_translate("MainWindow", "Salvar"))
        self.label_img_logo.setText(_translate("MainWindow", "Logo empresa"))
        self.push_button_msg_fechar.setText(_translate("MainWindow", "x"))
        self.label_erro.setText(_translate("MainWindow", "Erros de cadastro"))
        self.push_button_voltar_pric.setText(_translate("MainWindow", "Home"))
        self.push_button_go_list.setText(_translate("MainWindow", "Ver dados já cadastrados"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
