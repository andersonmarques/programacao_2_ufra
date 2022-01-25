import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap

from PyQt6.QtWidgets import QMainWindow, QApplication
from controle.produto_control import Produto_Control
from entidades.produto import Produto
from principal import Ui_MainWindow
from entidades.cliente import Cliente
from controle.cliente_control import Cliente_Control

class GUI_cont(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self) 
        self.init_components()
        self.controle_cliente = Cliente_Control()
        self.controle_produto = Produto_Control()
        self.cor_sucesso = "background-color: rgb(209, 255, 209);"
        self.cor_erro = "background-color: rgb(250, 185, 185);"

    def init_components(self):
        self.label_logo.setPixmap(QPixmap('./img/logo_ufra.png'))
        self.pushButton_area_clientes.clicked.connect(lambda: self.stackedWidget_paginas.setCurrentWidget(self.page_clientes))
        self.pushButton_area_produtos.clicked.connect(lambda: self.stackedWidget_paginas.setCurrentWidget(self.page_produtos))
        self.pushButton_salvar_cliente.clicked.connect(self.salvar_cliente)
        self.pushButton_excluir_cliente.clicked.connect(self.excluir_cliente)
        self.pushButton_salvar_produto.clicked.connect(self.salvar_produto) 
        self.frame_msg_bar.hide()
        self.pushButton_fechar_msg.clicked.connect(lambda: self.frame_msg_bar.hide())

    def listar_clientes_tabela(self):
        cont_linhas = 0
        self.tableWidget_clientes.clearContents()
        self.tableWidget_clientes.setRowCount(len(self.controle_cliente.lista_clientes))
        for cliente in self.controle_cliente.lista_clientes:
            self.tableWidget_clientes.setItem(cont_linhas, 0, QtWidgets.QTableWidgetItem(cliente.nome))
            self.tableWidget_clientes.setItem(cont_linhas, 1, QtWidgets.QTableWidgetItem(cliente.cpf))
            self.tableWidget_clientes.setItem(cont_linhas, 2, QtWidgets.QTableWidgetItem(cliente.bairro))
            self.tableWidget_clientes.setItem(cont_linhas, 3, QtWidgets.QTableWidgetItem(cliente.email))
            self.tableWidget_clientes.setItem(cont_linhas, 4, QtWidgets.QTableWidgetItem(cliente.categoria))
            cont_linhas += 1


    def listar_produtos_tabela(self):
        cont_linhas = 0
        self.tableWidget__produtos.setRowCount(10)
        for produto in self.controle_produto.lista_produtos:
            self.tableWidget__produtos.setItem(cont_linhas, 0, QtWidgets.QTableWidgetItem(produto.nome))
            self.tableWidget__produtos.setItem(cont_linhas, 1, QtWidgets.QTableWidgetItem(produto.codigo))
            self.tableWidget__produtos.setItem(cont_linhas, 2, QtWidgets.QTableWidgetItem(str(produto.preco)))
            self.tableWidget__produtos.setItem(cont_linhas, 3, QtWidgets.QTableWidgetItem(str(produto.quant_estoque)))
            cont_linhas += 1


    def salvar_cliente(self):
        cliente = Cliente()
        cliente.nome = self.lineEdit_nome_cliente.text()#ira capturar a entrada de dados do usuario como string
        cliente.cpf = self.lineEdit_cpf.text()
        cliente.bairro = self.lineEdit_bairro.text()
        cliente.email = self.lineEdit_email.text()
        cliente.fone = self.lineEdit_fone.text()
        cliente.categoria = self.comboBox_categoria_cliente.currentText()
        if len(cliente.erro_validacao) != 0:
            self.label_msg.setText(cliente.erro_validacao)
            self.frame_msg_bar.show()
            self.label_msg.setStyleSheet(self.cor_erro)
        else:#cliente salvo com sucesso
            msg = self.controle_cliente.salvar_cliente(cliente)
            self.label_msg.setText(msg)
            self.frame_msg_bar.show()
            self.label_msg.setStyleSheet(self.cor_sucesso)
            self.listar_clientes_tabela()

    def excluir_cliente(self):
        indice = self.tableWidget_clientes.currentRow()
        msg = self.controle_cliente.excluir_cliente(indice)
        self.label_msg.setText(msg)
        self.frame_msg_bar.show()
        self.label_msg.setStyleSheet(self.cor_sucesso)
        self.listar_clientes_tabela()

    def salvar_produto(self):
        produto = Produto()
        produto.nome = self.lineEdit_nome_produto.text()
        produto.codigo = self.lineEdit_codigo_produto.text()
        produto.preco = self.lineEdit_preco.text()
        produto.quant_estoque = self.lineEdit_quant_estoque.text()
        if len(produto.erro_validacao) != 0:
            self.label_msg.setText(produto.erro_validacao)
            self.frame_msg_bar.show()
            self.label_msg.setStyleSheet(self.cor_erro)
        else:
            msg = self.controle_produto.salvar_produto(produto)
            self.label_msg.setText(msg)
            self.frame_msg_bar.show()
            self.label_msg.setStyleSheet(self.cor_sucesso)
            self.listar_produtos_tabela()
    
    

if __name__ == '__main__':
    qt = QApplication(sys.argv)   
    view = GUI_cont()
    view.show()
    qt.exec()