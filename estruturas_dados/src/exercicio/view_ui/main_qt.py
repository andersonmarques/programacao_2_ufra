# Form implementation generated from reading ui file 'main_qt.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 359)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 10, 880, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_conteudo_item = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_conteudo_item.setObjectName("lineEdit_conteudo_item")
        self.horizontalLayout.addWidget(self.lineEdit_conteudo_item)
        self.lineEdit_posicao_estrutura = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_posicao_estrutura.setObjectName("lineEdit_posicao_estrutura")
        self.horizontalLayout.addWidget(self.lineEdit_posicao_estrutura)
        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_inserir_lista = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_inserir_lista.setObjectName("pushButton_inserir_lista")
        self.verticalLayout_4.addWidget(self.pushButton_inserir_lista)
        self.pushButton_remover_lista = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_remover_lista.setObjectName("pushButton_remover_lista")
        self.verticalLayout_4.addWidget(self.pushButton_remover_lista)
        self.textEdit_saida_lista = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit_saida_lista.setReadOnly(True)
        self.textEdit_saida_lista.setObjectName("textEdit_saida_lista")
        self.verticalLayout_4.addWidget(self.textEdit_saida_lista)
        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_inserir_fila = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_inserir_fila.setObjectName("pushButton_inserir_fila")
        self.verticalLayout_2.addWidget(self.pushButton_inserir_fila)
        self.pushButton_remover_fila = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_remover_fila.setObjectName("pushButton_remover_fila")
        self.verticalLayout_2.addWidget(self.pushButton_remover_fila)
        self.textEdit_saida_fila = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_saida_fila.setReadOnly(True)
        self.textEdit_saida_fila.setObjectName("textEdit_saida_fila")
        self.verticalLayout_2.addWidget(self.textEdit_saida_fila)
        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_empilhar = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_empilhar.setObjectName("pushButton_empilhar")
        self.verticalLayout.addWidget(self.pushButton_empilhar)
        self.pushButton_desempilhar = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_desempilhar.setObjectName("pushButton_desempilhar")
        self.verticalLayout.addWidget(self.pushButton_desempilhar)
        self.textEdit_saida_pilha = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_saida_pilha.setReadOnly(True)
        self.textEdit_saida_pilha.setObjectName("textEdit_saida_pilha")
        self.verticalLayout.addWidget(self.textEdit_saida_pilha)
        self.gridLayout.addWidget(self.frame_2, 1, 2, 1, 1)
        self.frame_msg = QtWidgets.QFrame(self.frame)
        self.frame_msg.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_msg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_msg.setObjectName("frame_msg")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_msg)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_msg = QtWidgets.QLabel(self.frame_msg)
        self.label_msg.setText("")
        self.label_msg.setObjectName("label_msg")
        self.horizontalLayout_2.addWidget(self.label_msg)
        self.pushButton_fechar_msg = QtWidgets.QPushButton(self.frame_msg)
        self.pushButton_fechar_msg.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.pushButton_fechar_msg.setFont(font)
        self.pushButton_fechar_msg.setStyleSheet("font: 900 10pt \"Arial\";")
        self.pushButton_fechar_msg.setObjectName("pushButton_fechar_msg")
        self.horizontalLayout_2.addWidget(self.pushButton_fechar_msg)
        self.gridLayout.addWidget(self.frame_msg, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_conteudo_item.setPlaceholderText(_translate("MainWindow", "Conteudo do item"))
        self.lineEdit_posicao_estrutura.setPlaceholderText(_translate("MainWindow", "posicao da estrutura"))
        self.pushButton_inserir_lista.setText(_translate("MainWindow", "Inserir na lista"))
        self.pushButton_remover_lista.setText(_translate("MainWindow", "Remover da lista"))
        self.pushButton_inserir_fila.setText(_translate("MainWindow", "Inserir na fila"))
        self.pushButton_remover_fila.setText(_translate("MainWindow", "Remover da fila"))
        self.pushButton_empilhar.setText(_translate("MainWindow", "Empilhar"))
        self.pushButton_desempilhar.setText(_translate("MainWindow", "Desempilhar"))
        self.pushButton_fechar_msg.setText(_translate("MainWindow", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
