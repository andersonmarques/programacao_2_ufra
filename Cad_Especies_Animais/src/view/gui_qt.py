# Form implementation generated from reading ui file 'gui_qt.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1213, 496)
        MainWindow.setMinimumSize(QtCore.QSize(1213, 496))
        MainWindow.setMaximumSize(QtCore.QSize(1213, 496))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_fundo = QtWidgets.QFrame(self.centralwidget)
        self.frame_fundo.setGeometry(QtCore.QRect(0, 0, 1211, 491))
        self.frame_fundo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_fundo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_fundo.setObjectName("frame_fundo")
        self.frame_area_trabalho = QtWidgets.QFrame(self.frame_fundo)
        self.frame_area_trabalho.setGeometry(QtCore.QRect(0, 90, 1211, 401))
        self.frame_area_trabalho.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.frame_area_trabalho.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_area_trabalho.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_area_trabalho.setObjectName("frame_area_trabalho")
        self.frame_esq = QtWidgets.QFrame(self.frame_area_trabalho)
        self.frame_esq.setGeometry(QtCore.QRect(10, 20, 401, 361))
        self.frame_esq.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QFrame{\n"
"    background-color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QSpinBox{    \n"
"    background-color: rgb(255, 255, 255);    \n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(236, 236, 236);\n"
"}")
        self.frame_esq.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_esq.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_esq.setObjectName("frame_esq")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_esq)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_esq)
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.frame_esq)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame_esq)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.spinBox_idade = QtWidgets.QSpinBox(self.frame_esq)
        self.spinBox_idade.setMinimum(-1)
        self.spinBox_idade.setMaximum(100)
        self.spinBox_idade.setProperty("value", -1)
        self.spinBox_idade.setObjectName("spinBox_idade")
        self.gridLayout.addWidget(self.spinBox_idade, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_esq)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_especies_animais = QtWidgets.QComboBox(self.frame_esq)
        self.comboBox_especies_animais.setObjectName("comboBox_especies_animais")
        self.comboBox_especies_animais.addItem("")
        self.comboBox_especies_animais.addItem("")
        self.comboBox_especies_animais.addItem("")
        self.comboBox_especies_animais.addItem("")
        self.comboBox_especies_animais.addItem("")
        self.comboBox_especies_animais.addItem("")
        self.gridLayout.addWidget(self.comboBox_especies_animais, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.frame_esq)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox_subespecies = QtWidgets.QComboBox(self.frame_esq)
        self.comboBox_subespecies.setObjectName("comboBox_subespecies")
        self.comboBox_subespecies.addItem("")
        self.gridLayout.addWidget(self.comboBox_subespecies, 3, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.frame_esq)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBox_classificacao = QtWidgets.QComboBox(self.frame_esq)
        self.comboBox_classificacao.setObjectName("comboBox_classificacao")
        self.comboBox_classificacao.addItem("")
        self.comboBox_classificacao.addItem("")
        self.comboBox_classificacao.addItem("")
        self.gridLayout.addWidget(self.comboBox_classificacao, 4, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.frame_esq)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.comboBox_habitat = QtWidgets.QComboBox(self.frame_esq)
        self.comboBox_habitat.setObjectName("comboBox_habitat")
        self.comboBox_habitat.addItem("")
        self.comboBox_habitat.addItem("")
        self.comboBox_habitat.addItem("")
        self.comboBox_habitat.addItem("")
        self.gridLayout.addWidget(self.comboBox_habitat, 5, 1, 1, 2)
        self.pushButton_salvar = QtWidgets.QPushButton(self.frame_esq)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.gridLayout.addWidget(self.pushButton_salvar, 6, 2, 1, 2)
        self.frame_dir = QtWidgets.QFrame(self.frame_area_trabalho)
        self.frame_dir.setGeometry(QtCore.QRect(420, 20, 791, 371))
        self.frame_dir.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.frame_dir.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_dir.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_dir.setObjectName("frame_dir")
        self.tableWidget_saida = QtWidgets.QTableWidget(self.frame_dir)
        self.tableWidget_saida.setGeometry(QtCore.QRect(10, 20, 611, 341))
        self.tableWidget_saida.setStyleSheet("")
        self.tableWidget_saida.setObjectName("tableWidget_saida")
        self.tableWidget_saida.setColumnCount(6)
        self.tableWidget_saida.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_saida.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_saida.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_saida.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_saida.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_saida.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_saida.setHorizontalHeaderItem(5, item)
        self.frame_edicao_lista = QtWidgets.QFrame(self.frame_dir)
        self.frame_edicao_lista.setGeometry(QtCore.QRect(630, 20, 153, 341))
        self.frame_edicao_lista.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_edicao_lista.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_edicao_lista.setObjectName("frame_edicao_lista")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_edicao_lista)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_posicao = QtWidgets.QLineEdit(self.frame_edicao_lista)
        self.lineEdit_posicao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_posicao.setObjectName("lineEdit_posicao")
        self.verticalLayout.addWidget(self.lineEdit_posicao)
        self.pushButton_Remover = QtWidgets.QPushButton(self.frame_edicao_lista)
        self.pushButton_Remover.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.pushButton_Remover.setObjectName("pushButton_Remover")
        self.verticalLayout.addWidget(self.pushButton_Remover)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame_msg = QtWidgets.QFrame(self.frame_fundo)
        self.frame_msg.setGeometry(QtCore.QRect(0, -1, 1211, 91))
        self.frame_msg.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_msg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_msg.setObjectName("frame_msg")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_msg)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_msg = QtWidgets.QLabel(self.frame_msg)
        self.label_msg.setObjectName("label_msg")
        self.horizontalLayout.addWidget(self.label_msg)
        self.pushButton_msg = QtWidgets.QPushButton(self.frame_msg)
        self.pushButton_msg.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_msg.setObjectName("pushButton_msg")
        self.horizontalLayout.addWidget(self.pushButton_msg)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro de Animais"))
        self.label.setText(_translate("MainWindow", "Todos os campos são obrigatórios"))
        self.lineEdit_nome.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.label_2.setText(_translate("MainWindow", "Idade:"))
        self.label_3.setText(_translate("MainWindow", "Espécie:"))
        self.comboBox_especies_animais.setItemText(0, _translate("MainWindow", "---"))
        self.comboBox_especies_animais.setItemText(1, _translate("MainWindow", "Aves"))
        self.comboBox_especies_animais.setItemText(2, _translate("MainWindow", "Anfíbio"))
        self.comboBox_especies_animais.setItemText(3, _translate("MainWindow", "Mamífero"))
        self.comboBox_especies_animais.setItemText(4, _translate("MainWindow", "Peixe"))
        self.comboBox_especies_animais.setItemText(5, _translate("MainWindow", "Réptil"))
        self.label_4.setText(_translate("MainWindow", "Subespécie:"))
        self.comboBox_subespecies.setItemText(0, _translate("MainWindow", "---"))
        self.label_5.setText(_translate("MainWindow", "Classifícação:"))
        self.comboBox_classificacao.setItemText(0, _translate("MainWindow", "---"))
        self.comboBox_classificacao.setItemText(1, _translate("MainWindow", "Vertebrado"))
        self.comboBox_classificacao.setItemText(2, _translate("MainWindow", "Invertebrado"))
        self.label_6.setText(_translate("MainWindow", "Habitat:"))
        self.comboBox_habitat.setItemText(0, _translate("MainWindow", "---"))
        self.comboBox_habitat.setItemText(1, _translate("MainWindow", "Aereo"))
        self.comboBox_habitat.setItemText(2, _translate("MainWindow", "Marinho"))
        self.comboBox_habitat.setItemText(3, _translate("MainWindow", "Terrestre"))
        self.pushButton_salvar.setText(_translate("MainWindow", "Salvar"))
        item = self.tableWidget_saida.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_saida.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget_saida.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Espécie"))
        item = self.tableWidget_saida.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Subespécie"))
        item = self.tableWidget_saida.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Classificação"))
        item = self.tableWidget_saida.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Habitat"))
        self.lineEdit_posicao.setPlaceholderText(_translate("MainWindow", "Posicão"))
        self.pushButton_Remover.setText(_translate("MainWindow", "Remover"))
        self.label_msg.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_msg.setText(_translate("MainWindow", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
