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
        # self.conteudo_arquivo = self.gerenciador.ler_animais_arquivo()
        self.cor_sucesso = "background-color: rgb(209, 255, 209);"
        self.cor_erro = "background-color: rgb(250, 185, 185);"
        self.recriar_animais()
        
    def init_components(self): 
        self.frame_msg.hide() 
        self.comboBox_especies_animais.currentTextChanged.connect(self.atualizar_subespecies)
        self.pushButton_salvar.clicked.connect(self.salvar_animal)
        self.pushButton_msg.clicked.connect(lambda: self.frame_msg.hide())
        self.pushButton_Remover.clicked.connect(self.remover_animal)

    def recriar_animais(self):
        # self.vetor_linhas = self.conteudo_arquivo.split('\n')
        self.vetor_linhas, msg, erro = self.gerenciador.ler_animais_arquivo()
        if erro:
            self.atualizar_msg(msg, self.cor_erro)
        else:
            for linha in self.vetor_linhas:
                vetor_partes_animal = linha.split('|')
                if vetor_partes_animal[0] == '':
                    break
                else:
                    id = vetor_partes_animal[0]
                    nome = vetor_partes_animal[1]
                    idade = vetor_partes_animal[2]
                    especie = vetor_partes_animal[3]
                    subespecie = vetor_partes_animal[4]
                    classificacao = vetor_partes_animal[5]
                    habitat = vetor_partes_animal[6]
                    #criando um novo obj do tipo Animal
                    animal = Animal(id, nome, idade, especie, subespecie, classificacao, habitat)
                    #salvar o novo animal na lista
                    self.gerenciador.salvar_animal(animal)
        
            self.listar_animais()


    def remover_animal(self):
        msg = ''
        posicao = self.lineEdit_posicao.text()
        if not posicao:
            msg = self.gerenciador.remover_animal_lista()
        else:
            msg = self.gerenciador.remover_animal_lista(int(posicao))
        
        self.listar_animais()     
        self.atualizar_msg(msg, self.cor_sucesso)

    def salvar_animal(self):
        animal = Animal()
        animal.nome = self.lineEdit_nome.text()
        animal.idade = self.spinBox_idade.text()# tudo que o usuario digitar via GUI é uma String
        animal.especie = self.comboBox_especies_animais.currentText()
        animal.subespecie = self.comboBox_subespecies.currentText()
        animal.classificacao = self.comboBox_classificacao.currentText()
        animal.habitat = self.comboBox_habitat.currentText()
        if not animal.erro:# nao V = F; nao F = V
            self.cont_id = self.gerenciador.verificar_ultimo_id()
            self.cont_id += 1
            animal.id = self.cont_id
            msg = self.gerenciador.salvar_animal(animal)
            self.atualizar_msg(msg, self.cor_sucesso)
            self.listar_animais()                        
            self.gerenciador.salvar_animal_em_arquivo(animal)
        else:
            self.atualizar_msg(f'Ocorreu um erro: {animal.erro}', self.cor_erro)
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

    def atualizar_msg(self, msg, cor):
        self.frame_msg.show()
        self.label_msg.setText(msg)
        self.label_msg.setStyleSheet(cor)

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