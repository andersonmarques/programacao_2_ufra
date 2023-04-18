# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 516)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_background = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_background.setGeometry(QtCore.QRect(0, 0, 811, 491))
        self.frame_background.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_background.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_background.setObjectName("frame_background")
        self.frame = QtWidgets.QFrame(parent=self.frame_background)
        self.frame.setGeometry(QtCore.QRect(20, 100, 781, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.table_widget_tabela = QtWidgets.QTableWidget(parent=self.frame)
        self.table_widget_tabela.setObjectName("table_widget_tabela")
        self.table_widget_tabela.setColumnCount(5)
        self.table_widget_tabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_tabela.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_tabela.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_tabela.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_tabela.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.table_widget_tabela, 0, 0, 1, 1)
        self.frame_menu = QtWidgets.QFrame(parent=self.frame)
        self.frame_menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_menu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.push_button_nova_linha = QtWidgets.QPushButton(parent=self.frame_menu)
        self.push_button_nova_linha.setObjectName("push_button_nova_linha")
        self.verticalLayout.addWidget(self.push_button_nova_linha)
        self.push_button_remover_linha = QtWidgets.QPushButton(parent=self.frame_menu)
        self.push_button_remover_linha.setObjectName("push_button_remover_linha")
        self.verticalLayout.addWidget(self.push_button_remover_linha)
        self.radio_button_max = QtWidgets.QRadioButton(parent=self.frame_menu)
        self.radio_button_max.setObjectName("radio_button_max")
        self.verticalLayout.addWidget(self.radio_button_max)
        self.radio_button_min = QtWidgets.QRadioButton(parent=self.frame_menu)
        self.radio_button_min.setObjectName("radio_button_min")
        self.verticalLayout.addWidget(self.radio_button_min)
        self.push_button_otimizar = QtWidgets.QPushButton(parent=self.frame_menu)
        self.push_button_otimizar.setObjectName("push_button_otimizar")
        self.verticalLayout.addWidget(self.push_button_otimizar)
        self.gridLayout.addWidget(self.frame_menu, 0, 1, 1, 1)
        self.label_logo = QtWidgets.QLabel(parent=self.frame_background)
        self.label_logo.setGeometry(QtCore.QRect(30, 10, 151, 71))
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table_widget_tabela.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ingredientes"))
        item = self.table_widget_tabela.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "% da MS"))
        item = self.table_widget_tabela.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "NDT, %MS"))
        item = self.table_widget_tabela.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PB, %MS"))
        item = self.table_widget_tabela.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "R$/t MS"))
        self.push_button_nova_linha.setText(_translate("MainWindow", "+"))
        self.push_button_remover_linha.setText(_translate("MainWindow", "-"))
        self.radio_button_max.setText(_translate("MainWindow", "Máximo"))
        self.radio_button_min.setText(_translate("MainWindow", "Mínimo"))
        self.push_button_otimizar.setText(_translate("MainWindow", "Otimizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
