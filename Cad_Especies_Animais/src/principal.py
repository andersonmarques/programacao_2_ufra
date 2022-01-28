import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from controller.gerenciador_animais import Gerenciador_Animais
from model.animal import Animal
from view.gui_qt import Ui_MainWindow

class Principal(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.init_components()
        self.cont_id = 0
        self.lista_subespecie = []
        self.gerenciador = Gerenciador_Animais()
        self.conteudo_arquivo = self.gerenciador.ler_animais_arquivo()
        print(self.conteudo_arquivo)
        self.vetor_linhas = self.conteudo_arquivo.split('\n')        
        print(self.vetor_linhas)

    def init_components(self): 
        self.frame_msg.hide() 
        self.comboBox_especies_animais.currentTextChanged.connect(self.atualizar_subespecies)
        self.pushButton_salvar.clicked.connect(self.salvar_animal)
        self.pushButton_msg.clicked.connect(lambda: self.frame_msg.hide())

    def salvar_animal(self):
        animal = Animal()
        animal.nome = self.lineEdit_nome.text()
        animal.idade = self.spinBox_idade.text()# tudo que o usuario digitar via GUI é uma String
        animal.especie = self.comboBox_especies_animais.currentText()
        animal.subespecie = self.comboBox_subespecies.currentText()
        animal.classificacao = self.comboBox_classificacao.currentText()
        animal.habitat = self.comboBox_habitat.currentText()
        if not animal.erro:
            self.cont_id += 1
            animal.id = self.cont_id
            msg = self.gerenciador.salvar_animal(animal)
            self.atualizar_msg(msg)
            self.listar_animais()                        
            self.gerenciador.salvar_animal_em_arquivo()
        else:
            self.atualizar_msg(f'Ocorreu um erro: {animal.erro}')
        # self.gerenciador_Animais.salvar_arquivo(f"Animal id: {animal.id}\nEnviando msg da GUI\n para o arquivo TXT.")        
        
    def listar_animais(self):
        linha_tabela = 0
        self.tableWidget_saida.setRowCount(len(self.gerenciador.lista_animais))
        for animal in self.gerenciador.lista_animais:
            self.tableWidget_saida.setItem(linha_tabela, 0, QtWidgets.QTableWidgetItem(str(animal.id)))
            self.tableWidget_saida.setItem(linha_tabela, 1, QtWidgets.QTableWidgetItem(animal.nome))
            self.tableWidget_saida.setItem(linha_tabela, 2, QtWidgets.QTableWidgetItem(animal.especie))
            self.tableWidget_saida.setItem(linha_tabela, 3, QtWidgets.QTableWidgetItem(animal.subespecie))
            self.tableWidget_saida.setItem(linha_tabela, 4, QtWidgets.QTableWidgetItem(animal.classificacao))
            self.tableWidget_saida.setItem(linha_tabela, 5, QtWidgets.QTableWidgetItem(animal.habitat))
            linha_tabela += 1

    def atualizar_msg(self, msg):
        self.frame_msg.show()
        self.label_msg.setText(msg)

    def atualizar_subespecies(self, especie):
        self.comboBox_subespecies.clear()
        if especie == 'Aves':
            self.lista_subespecie = ['Gaivota', 'Andorinha', 'Gavião']            
        elif especie == 'Anfíbio':
            self.lista_subespecie = ['Salamandra', 'Sapo', 'Perereca']
        elif especie == 'Mamífero':
            self.lista_subespecie = ['Vaca', 'Porco', 'Cachorro']
        elif especie == 'Peixe':
            self.lista_subespecie = ['Tamuata', 'Pirarucu','Pescada Amarela']
        elif especie == 'Réptil':
            self.lista_subespecie = ['Jacaré', 'Crocodilo','Cobra']
        
        self.lista_subespecie.insert(0, '---')
        self.comboBox_subespecies.addItems(self.lista_subespecie)

if __name__ == '__main__':
    qt = QApplication(sys.argv)   
    principal = Principal()
    principal.show()
    qt.exec()