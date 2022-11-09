import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from gui_matriz import Ui_MainWindow
from controle.matriz_controle import Matriz_controle
from modelo.matriz import Matriz

class Main_view (QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.matriz_controle = Matriz_controle()
        self.push_button_soma_diag_prin.clicked.connect(self.preparar_calculo_diag_prin)
        
    def imprimir_saida(self, texto):
        self.text_edit_saida.setText("")
        self.text_edit_saida.setText(f"{texto}")

    def preparar_calculo_diag_prin(self):        
        #capturando a matriz do usuario
        matriz_gui = self.text_edit_matriz.toPlainText()
        matriz_x = self.matriz_controle.montar_matriz_usuario(matriz_gui)
        
        self.resultado = self.matriz_controle.somar_diagonal_principal(matriz_x)
        self.imprimir_saida(self.resultado)
        # #montando nosso obj matriz
        # matriz_M = Matriz(matriz_x.shape[0],matriz_x.shape[1])   
        # matriz_M.valores = matriz_x

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    visao = Main_view()
    visao.show()
    qt.exec()