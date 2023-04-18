import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from main_gui import Ui_MainWindow
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
# from pulp import *
from scipy.optimize import minimize

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.init_components()

    def init_components(self):
        logo = QPixmap(r'img\ufra_logo.png')
        logo = logo.scaled(self.label_logo.width(),self.label_logo.height(), Qt.AspectRatioMode.KeepAspectRatio)
        self.label_logo.setPixmap(logo)
        self.push_button_nova_linha.clicked.connect(self.criar_nova_linha_tabela)
        self.push_button_remover_linha.clicked.connect(lambda: self.table_widget_tabela.removeRow(self.table_widget_tabela.currentRow()))
        self.preencher_tabela()
        self.calcular_soma_coluna(1)
        self.total_2 = self.somaproduto_colunas(2)
        self.total_3 = self.somaproduto_colunas(3)
        self.total_4 = self.somaproduto_colunas(4)
        # self.push_button_otimizar.clicked.connect(lambda: self.otimizar_quantidades('min'))
        self.push_button_otimizar.clicked.connect(lambda: self.executar_otimizacao('min'))

    def otimizar_scipy(self, qtd_alimentos, alimentos, restricoes):
        def funcao_objetivo(qtds):
            return sum([qtds[i] * alimentos[i]['preco'] for i in range(len(alimentos))])

        def funcao_restricao_NDT(qtds):
            return sum([qtds[i] * alimentos[i]['ndt'] for i in range(len(alimentos))]) - restricoes[0]['value']

        def funcao_restricao_PB(qtds):
            return sum([qtds[i] * alimentos[i]['pb'] for i in range(len(alimentos))]) - restricoes[1]['value']

        restricoes_scipy = [{'type': restricao['type'], 'fun': restricao['fun']} for restricao in restricoes]

        resultado = minimize(funcao_objetivo, qtd_alimentos, constraints=restricoes_scipy, method='SLSQP', bounds=[(0, None)] * len(alimentos))

        return resultado.fun#, resultado.x

    def executar_otimizacao(self, tipo_otimizacao):
        # Ler os dados da tabela e preparar os argumentos para a função otimizar_scipy()
        # resultado = []
        alimentos = []
        qtds = []
        for linha in range(self.table_widget_tabela.rowCount()-1):
            alimento = {
                'nome': self.table_widget_tabela.item(linha, 0).text(),
                'ndt': float(self.table_widget_tabela.item(linha, 1).text()),
                'pb': float(self.table_widget_tabela.item(linha, 2).text()),
                'preco': float(self.table_widget_tabela.item(linha, 3).text())
            }
            alimentos.append(alimento)
            qtds.append(min(1.0, float(self.table_widget_tabela.item(linha, 4).text())/100))
            
        restricoes = [
           {'type': 'ineq', 'fun': lambda qtds: 0.9 - sum([qtds[i] * alimentos[i]['ndt'] for i in range(len(alimentos))]), 'value': 0},
            {'type': 'ineq', 'fun': lambda qtds: sum([qtds[i] * alimentos[i]['ndt'] for i in range(len(alimentos))]) - 0.6, 'value': 0},
            {'type': 'ineq', 'fun': lambda qtds: 0.9 - sum([qtds[i] * alimentos[i]['pb'] for i in range(len(alimentos))]), 'value':0},
            {'type': 'ineq', 'fun': lambda qtds: sum([qtds[i] * alimentos[i]['pb'] for i in range(len(alimentos))]) - 0.1, 'value':0},
        ]

        #if tipo_otimizacao == 'min':
        resultado = minimize(self.otimizar_scipy, qtds, args=(alimentos, restricoes), method='SLSQP')
       
        # Atualizar a tabela com os resultados da otimização
        for linha, qtd in enumerate(resultado.x):
            self.table_widget_tabela.setItem(linha, 4, QTableWidgetItem('{:.2f}'.format(qtd * 100)))

        self.somaproduto_colunas(2)
        self.somaproduto_colunas(3)
        self.somaproduto_colunas(4)


    def criar_nova_linha_tabela(self):
        ultima_linha = self.table_widget_tabela.rowCount()
        self.table_widget_tabela.insertRow(ultima_linha)
        self.table_widget_tabela.setItem(ultima_linha, 0, QTableWidgetItem(''))
        
    def preencher_tabela(self):
        dados = [
            ('Milho', '20', '90', '9.4', '450'),
            ('Casca de soja', '20', '67.3', '13.9', '300'),
            ('Farelo de soja', '20', '81', '49.9', '1000'),
            ('Ureia', '20', '0', '270', '1500'),
            ('Sal', '20', '0', '0', '1200')
        ]
        self.table_widget_tabela.setRowCount(len(dados))
        for linha, valores in enumerate(dados):
            for coluna, valor in enumerate(valores):
                item = QTableWidgetItem(valor)
                self.table_widget_tabela.setItem(linha, coluna, item)


    def calcular_soma_coluna(self, coluna):
        soma = 0
        num_linhas = self.table_widget_tabela.rowCount()

        # Itera sobre as linhas da tabela e soma os valores da coluna selecionada
        for linha in range(num_linhas):
            item = self.table_widget_tabela.item(linha, coluna)
            if item is not None:
                valor = float(item.text())
                soma += valor

        # Adiciona uma nova linha à tabela com o resultado da soma
        nova_linha = self.table_widget_tabela.rowCount()
        self.table_widget_tabela.insertRow(nova_linha)
        self.table_widget_tabela.setItem(nova_linha, 0, QTableWidgetItem('Total'))
        self.table_widget_tabela.setItem(nova_linha, coluna, QTableWidgetItem(str(soma)))

    def somaproduto_colunas(self, coluna:int):
        n_linhas = self.table_widget_tabela.rowCount() - 1
        soma_produto = 0.0
        percent_soma_produto = 0.0
        for i in range(n_linhas):
            percent_ms = float(self.table_widget_tabela.item(i, 1).text())
            percent_coluna = float(self.table_widget_tabela.item(i, coluna).text())
            soma_produto += percent_ms * percent_coluna
            percent_soma_produto = soma_produto/100

        # Adiciona o resultado na linha "Total" da coluna especificada
        self.table_widget_tabela.setItem(n_linhas, coluna, QTableWidgetItem(str(percent_soma_produto)))


    # def otimizar_quantidades(self, objetivo):
    #     alimentos = [
    #         {'nome': 'Milho', 'ndt': 90, 'pb': 9.4, 'preco': 450},
    #         {'nome': 'Casca de soja', 'ndt': 67.3, 'pb': 13.9, 'preco': 300},
    #         {'nome': 'Farelo de soja', 'ndt': 81, 'pb': 49.9, 'preco': 1000},
    #         {'nome': 'Ureia', 'ndt': 0, 'pb': 270, 'preco': 1500},
    #         {'nome': 'Sal', 'ndt': 0, 'pb': 0, 'preco': 1200},
    #     ]
    #     # cria o modelo de otimização
    #     prob = LpProblem("Problema de dieta", LpMinimize)

    #     # cria as variáveis de decisão
    #     qtds = LpVariable.dicts("qtd", range(len(alimentos)), lowBound=0)

    #     # cria a função objetivo
    #     prob += lpSum([qtds[i] * alimentos[i]['preco'] for i in range(len(alimentos))])

    #     # cria as restrições
    #     prob += lpSum([qtds[i] * alimentos[i]['ndt'] for i in range(len(alimentos))]) >= self.total_2
    #     prob += lpSum([qtds[i] * alimentos[i]['pb'] for i in range(len(alimentos))]) >= self.total_3
    #     prob += lpSum([qtds[i] for i in range(len(alimentos))]) == 100

    #     # resolve o problema de otimização
    #     prob.solve()

    #     # adiciona as quantidades calculadas na tabela
    #     if objetivo == "min":
    #         row = self.table_widget_tabela.rowCount()
    #         self.table_widget_tabela.insertRow(row)
    #         self.table_widget_tabela.setItem(row, 0, QTableWidgetItem("Quantidade mínima"))
    #     else:
    #         row = self.table_widget_tabela.rowCount() - 1
    #     for i in range(len(alimentos)):
    #         qtd = qtds[i].varValue
    #         self.table_widget_tabela.setItem(row, i+1, QTableWidgetItem(f"{qtd:.2f}"))

    #     # atualiza a soma dos produtos e o somaproduto de cada coluna
    #     self.calcular_soma_coluna(1)
    #     self.somaproduto_colunas(2)
    #     self.somaproduto_colunas(3)
    #     self.somaproduto_colunas(4)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    main = Main()
    main.show()
    qt.exec()