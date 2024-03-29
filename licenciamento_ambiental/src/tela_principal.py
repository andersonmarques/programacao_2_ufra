# Form implementation generated from reading ui file 'tela_principal.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 631)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_fundo = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_fundo.setGeometry(QtCore.QRect(9, 9, 821, 621))
        self.frame_fundo.setStyleSheet("background-color: rgb(203, 255, 207);")
        self.frame_fundo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_fundo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_fundo.setObjectName("frame_fundo")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.frame_fundo)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 180, 821, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.table_widget_saida = QtWidgets.QTableWidget(parent=self.gridLayoutWidget)
        self.table_widget_saida.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_widget_saida.setObjectName("table_widget_saida")
        self.table_widget_saida.setColumnCount(3)
        self.table_widget_saida.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_saida.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_saida.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_saida.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.table_widget_saida, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.line_edit_area_matricula = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.line_edit_area_matricula.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_edit_area_matricula.setObjectName("line_edit_area_matricula")
        self.gridLayout.addWidget(self.line_edit_area_matricula, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.push_button_salvar = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.push_button_salvar.setFont(font)
        self.push_button_salvar.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.push_button_salvar.setObjectName("push_button_salvar")
        self.gridLayout.addWidget(self.push_button_salvar, 3, 1, 1, 1)
        self.line_edit_empreendimento = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.line_edit_empreendimento.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_edit_empreendimento.setObjectName("line_edit_empreendimento")
        self.gridLayout.addWidget(self.line_edit_empreendimento, 0, 1, 1, 1)
        self.line_edit_area = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_edit_area.setFont(font)
        self.line_edit_area.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_edit_area.setObjectName("line_edit_area")
        self.gridLayout.addWidget(self.line_edit_area, 2, 1, 1, 1)
        self.label_logo_emp = QtWidgets.QLabel(parent=self.frame_fundo)
        self.label_logo_emp.setGeometry(QtCore.QRect(10, 10, 111, 81))
        self.label_logo_emp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_logo_emp.setText("")
        self.label_logo_emp.setObjectName("label_logo_emp")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_fundo)
        self.label_5.setGeometry(QtCore.QRect(140, 0, 581, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.frame_msg = QtWidgets.QFrame(parent=self.frame_fundo)
        self.frame_msg.setGeometry(QtCore.QRect(0, 109, 811, 61))
        self.frame_msg.setStyleSheet("background-color: rgb(203, 255, 207);")
        self.frame_msg.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_msg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_msg.setObjectName("frame_msg")
        self.label_msg = QtWidgets.QLabel(parent=self.frame_msg)
        self.label_msg.setGeometry(QtCore.QRect(30, 20, 671, 31))
        self.label_msg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_msg.setText("")
        self.label_msg.setObjectName("label_msg")
        self.push_button_fechar = QtWidgets.QPushButton(parent=self.frame_msg)
        self.push_button_fechar.setGeometry(QtCore.QRect(762, 20, 41, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.push_button_fechar.setFont(font)
        self.push_button_fechar.setObjectName("push_button_fechar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table_widget_saida.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Empreendimento"))
        item = self.table_widget_saida.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Matrícula"))
        item = self.table_widget_saida.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Área"))
        self.label_3.setText(_translate("MainWindow", "Matrícula de operação:"))
        self.label_2.setText(_translate("MainWindow", "Tipo de empreendimento:"))
        self.label.setText(_translate("MainWindow", "Tamanho da Área:"))
        self.push_button_salvar.setText(_translate("MainWindow", "Salvar Licenciamento Ambiental"))
        self.line_edit_area.setPlaceholderText(_translate("MainWindow", "Digite a área em m² (ex: 75,5)"))
        self.label_5.setText(_translate("MainWindow", "Diagnostico ambiental"))
        self.push_button_fechar.setText(_translate("MainWindow", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
