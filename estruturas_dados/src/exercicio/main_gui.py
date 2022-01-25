import sys

from PyQt6.QtWidgets import QMainWindow, QApplication
from controle.controle_lista import Controle_Lista
from controle.controle_fila import Controle_Fila
from controle.controle_pilha import Controle_Pilha
from modelo.nodo import Nodo
from view_ui.main_qt import Ui_MainWindow

class Main_view (QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self) 
        self.init_components()
        #na classe Controle_Listas tem as regras sobre listas
        self.controle_lista = Controle_Lista()
        self.controle_fila = Controle_Fila()
        self.controle_pilha = Controle_Pilha()

    def init_components(self):
        self.frame_msg.hide()#esconde o frame de msg
        self.pushButton_fechar_msg.clicked.connect(lambda: self.frame_msg.hide())
        self.pushButton_inserir_lista.clicked.connect(self.inserir_lista)
        self.pushButton_remover_lista.clicked.connect(self.remover_da_lista)
        self.pushButton_inserir_fila.clicked.connect(self.inserir_fila)
        self.pushButton_remover_fila.clicked.connect(self.tirar_fila)
        self.pushButton_empilhar.clicked.connect(self.inserir_pilha)
        self.pushButton_desempilhar.clicked.connect(self.remover_item_pilha)
        self.cor_sucesso = "background-color: rgb(209, 255, 209);"
        self.cor_erro = "background-color: rgb(250, 185, 185);"

    def inserir_pilha(self):
        conteudo = self.lineEdit_conteudo_item.text()
        item = Nodo()
        item.conteudo = conteudo
        msg = self.controle_pilha.empilhar(item)
        self.mostrar_msg_sucesso(msg)
        self.imprimir_pilha()

    def remover_item_pilha(self):
        msg, removeu = self.controle_pilha.desempilhar()
        if removeu:
            self.mostrar_msg_sucesso(msg)
        else:
            self.mostrar_msg_erro(msg)

        self.imprimir_pilha()

    def tirar_fila(self):
        msg, flag = self.controle_fila.sair_fila()
        if flag:
            self.mostrar_msg_sucesso(msg)
        else:
            self.mostrar_msg_erro(msg)
        
        self.imprimir_fila()

    def inserir_fila(self):
        conteudo = self.lineEdit_conteudo_item.text()
        item = Nodo()
        item.conteudo = conteudo
        if not item.msg:
            msg = self.controle_fila.entrar_fila(item)
            self.mostrar_msg_sucesso(msg)
            self.imprimir_fila()
        else:
            self.mostrar_msg_erro(item.msg)
            self.imprimir_fila()
        self.lineEdit_conteudo_item.setText('')

    def inserir_lista(self):
        conteudo = self.lineEdit_conteudo_item.text()
        posicao = self.lineEdit_posicao_estrutura.text()
        nodo = Nodo()#instanciando o obj Nodo
        nodo.conteudo = conteudo
        if not nodo.msg:
            if not posicao: #checa se a string esta vazia
                msg = self.controle_lista.inserir_final_lista(nodo)
                self.mostrar_msg_sucesso(msg)
                self.imprimir_lista()
            else:
                msg = self.controle_lista.inserir_posicao_lista(posicao, nodo)
                self.mostrar_msg_sucesso(msg)
                self.imprimir_lista()
        else:
            self.mostrar_msg_erro(nodo.msg)
        
        self.lineEdit_conteudo_item.setText('')

    def remover_da_lista(self):
        posicao = self.lineEdit_posicao_estrutura.text()
        if not posicao:#verifica se a string posicao esta vazia
            msg, flag = self.controle_lista.remover_da_lista()
            self.mostrar_msg_sucesso(msg)
        else:
            msg, flag = self.controle_lista.remover_da_lista(posicao)
            if flag:
                self.mostrar_msg_sucesso(msg)                       
            else:
                self.mostrar_msg_erro(msg)
        self.imprimir_lista()     

    def mostrar_msg_erro(self,msg):
        self.frame_msg.show()
        self.label_msg.setText(msg)
        self.label_msg.setStyleSheet(self.cor_erro)

    def mostrar_msg_sucesso(self, msg):
        self.frame_msg.show()#mostrar o frame
        self.label_msg.setText(msg)
        self.label_msg.setStyleSheet(self.cor_sucesso)

    def imprimir_lista(self):
        saida = 'L: ['     
        for nodo in self.controle_lista.lista:
            saida += f'{nodo.conteudo},'
        saida = saida.removesuffix(',')
        saida += ']'
        self.textEdit_saida_lista.setText(saida) 

    def imprimir_fila(self):
        saida = 'F: ['
        for item in self.controle_fila.fila:
            saida += f'{item.conteudo},'#F: [1,2,3]
        saida = saida.removesuffix(',')
        saida += ']'
        self.textEdit_saida_fila.setText(saida)

    def imprimir_pilha(self):
        saida = 'P: ['
        for item in self.controle_pilha.pilha:
            saida += f'{item.conteudo},'
        saida = saida.removesuffix(',')
        saida += ']'
        self.textEdit_saida_pilha.setText(saida)

if __name__ == '__main__':
    qt = QApplication(sys.argv)   
    view = Main_view()
    view.show()
    qt.exec()