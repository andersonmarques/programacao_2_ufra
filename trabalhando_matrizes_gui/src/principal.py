import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit

from controller.matriz_controle import Matriz_controle
from view.gui_matriz import Ui_MainWindow
from model.matriz import Matriz


class Principal (QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.init_components()
        self.gerente = Matriz_controle()

    def init_components(self):
        self.cor_sucesso = "background-color: rgb(209, 255, 209);"
        self.cor_erro = "background-color: rgb(250, 185, 185);"
        self.frame_msg.hide()
        #area referente a imagem da logo do projeto
        try:            
            logo = QPixmap('img/ufra_logo.png')
            logo = logo.scaled(self.label_logo.width(),self.label_logo.height(), Qt.AspectRatioMode.KeepAspectRatio)
            self.label_logo.setPixmap(logo)
            icon = QPixmap("img/icone.png");
            tmp = icon.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio);
            self.setWindowIcon(QIcon(tmp))
        except :
            print('Erro! Arquivo não encontrado!')
        self.push_button_fechar_msg.clicked.connect(lambda: self.frame_msg.hide())
        self.push_button_soma_diag_prin_A.clicked.connect(lambda : self.diagonal_prin_view('a'))
        self.push_button_soma_diag_prin_B.clicked.connect(lambda : self.diagonal_prin_view('b'))
        self.push_button_soma_diag_sec_A.clicked.connect(lambda : self.diagonal_sec_view('a'))
        self.push_button_soma_diag_sec_B.clicked.connect(lambda : self.diagonal_sec_view('b'))
        self.push_button_elem_matriz_produto.clicked.connect(self.elemento_matriz_produto_view)
        self.push_button_transposta_A.clicked.connect(lambda : self.transpor_view('a'))
        self.push_button_transposta_B.clicked.connect(lambda : self.transpor_view('b'))
        self.push_button_det_A.clicked.connect(lambda : self.det_laplace_view('a'))
        self.push_button_det_B.clicked.connect(lambda : self.det_laplace_view('b'))
        self.push_button_somar.clicked.connect(self.somar_view)
        self.push_button_subtratir.clicked.connect(self.subtrair_view)
        self.push_button_multiplicar.clicked.connect(self.multiplicar_view)
        # self.push_button_hungaro_A.clicked.connect(self.preparar_hungaro)
    
    def diagonal_prin_view(self, nome_matriz:str):
        resultado = ''
        if nome_matriz == 'a':        
            A = self.capturar_matriz_gui(self.text_edit_matriz_a)
            resultado = self.gerente.somar_diagonal_principal(A)
        else:
            B = self.capturar_matriz_gui(self.text_edit_matriz_b)
            resultado = self.gerente.somar_diagonal_principal(B)
        self.imprimir_saida(resultado)

    def diagonal_sec_view(self, nome_matriz:str):
        resultado = ''
        if nome_matriz == 'a':
            A = self.capturar_matriz_gui(self.text_edit_matriz_a)
            resultado = self.gerente.somar_diagonal_secundaria(A)
        else:
            B = self.capturar_matriz_gui(self.text_edit_matriz_b)
            resultado = self.gerente.somar_diagonal_secundaria(B)
        self.imprimir_saida(resultado)

    def elemento_matriz_produto_view(self):
        m,n = self.line_edit_posicao_mn.text().split(',')

        A = self.capturar_matriz_gui(self.text_edit_matriz_a)
        B = self.capturar_matriz_gui(self.text_edit_matriz_b)

        resultado = self.gerente.calcular_elemento_matriz_produto(int(m),int(n),A, B)
        if not self.gerente.erro:
            self.imprimir_saida(resultado)
        else:
            self.mostrar_msg_erro(self.gerente.erro)

    def subtrair_view(self):
        A = self.capturar_matriz_gui(self.text_edit_matriz_a)
        B = self.capturar_matriz_gui(self.text_edit_matriz_b)
        resultado = self.gerente.subtrair_matrizes(A, B).valores
        if not self.gerente.erro:
            #self.mostrar_msg_sucesso("Cálculo realizado com sucesso!")
            self.imprimir_saida(resultado)
        else:
            self.mostrar_msg_erro(self.gerente.erro)

    def somar_view(self):
        A = self.capturar_matriz_gui(self.text_edit_matriz_a)
        B = self.capturar_matriz_gui(self.text_edit_matriz_b)
        resultado = self.gerente.somar_matrizes(A, B).valores
        if not self.gerente.erro:
            #self.mostrar_msg_sucesso("Cálculo realizado com sucesso!")
            self.imprimir_saida(resultado)
        else:
            self.mostrar_msg_erro(self.gerente.erro)

    def transpor_view(self, nome_matriz:str):
        matriz_x = 0
        if nome_matriz == 'a':
            matriz_x = self.capturar_matriz_gui(self.text_edit_matriz_a)
        else:
            matriz_x = self.capturar_matriz_gui(self.text_edit_matriz_b)
        M_t = self.gerente.transpor_matriz(matriz_x)
        self.imprimir_saida(M_t.valores)

    def multiplicar_view(self):
        A = self.capturar_matriz_gui(self.text_edit_matriz_a)
        B = self.capturar_matriz_gui(self.text_edit_matriz_b)
        resultado = self.gerente.multiplicar_matrizes(A, B).valores
        if not self.gerente.erro:
            self.imprimir_saida(resultado)
        else:
            self.mostrar_msg_erro(self.gerente.erro)

    def capturar_matriz_gui(self, text_edit: QTextEdit) -> Matriz:
        matriz_gui_str = text_edit.toPlainText()
        matriz_x = self.gerente.converter_texto_para_matriz(matriz_gui_str)
        return matriz_x

    def mostrar_msg_erro(self, msg):
        self.frame_msg.show()
        self.label_msg.setText(msg)
        self.label_msg.setStyleSheet(self.cor_erro)
        self.gerente.falar_mensagem(msg)
        self.gerente.erro = ""
        self.text_edit_saida.setText("")

    # def mostrar_msg_sucesso(self, msg):
    #     self.frame_msg.show()#mostrar o frame
    #     self.label_msg.setText(msg)
    #     self.label_msg.setStyleSheet(self.cor_sucesso)
    #     self.gerente.falar_mensagem(msg)

    def det_laplace_view(self, nome_matriz: str):
        matriz_x = 0
        if nome_matriz == 'a':
            matriz_x = self.capturar_matriz_gui(self.text_edit_matriz_a)
        else:
            matriz_x = self.capturar_matriz_gui(self.text_edit_matriz_b)
        resultado = self.gerente.calcular_determinante(matriz_x)
        if self.gerente.erro:
            self.mostrar_msg_erro(self.gerente.erro)
            self.gerente.erro = ""
            self.imprimir_saida("")
        else: 
            self.imprimir_saida(resultado)

    def imprimir_saida(self, texto):
        self.text_edit_saida.setText("")
        self.text_edit_saida.setText(f'{texto}')
        self.frame_msg.hide()

    def preparar_hungaro(self):        
        A = self.capturar_matriz_gui(self.text_edit_matriz_a)
        m_saida = self.gerente.metodo_hungaro(A)
        if not self.gerente.erro :
            #self.mostrar_msg_sucesso("Cálculo realizado com sucesso!")
            self.imprimir_saida(m_saida.valores)
        else:
            self.gerente.erro = ""
            self.imprimir_saida("")
            self.mostrar_msg_erro(self.gerente.erro)

if __name__ == '__main__': 
    qt = QApplication(sys.argv)
    visao = Principal()
    visao.show()
    qt.exec()