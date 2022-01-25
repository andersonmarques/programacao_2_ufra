import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from model.animal import Animal
from view.gui_qt import Ui_MainWindow

class Principal(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.init_components()

    def init_components(self):
        self.contador = 0
        self.lista_subespecie = []
        self.frame_msg.hide()
        self.comboBox_especies_animais.currentTextChanged.connect(self.atualizar_subespecies)
        self.pushButton_salvar.clicked.connect(self.salvar_animal)

    def salvar_animal(self):
        animal = Animal()
        self.contador += 1
        animal.id = self.contador
        animal.nome = self.lineEdit_nome.text()
        animal.especie = self.comboBox_especies_animais.currentText()
        animal.subespecie = self.comboBox_subespecies.currentText()
        print(f"É para salvar o animal de id: {animal.id}| {animal.erro}")
        #salva o animal

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