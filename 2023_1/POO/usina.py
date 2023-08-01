class Usina:
    # Atributos ou características ou propriedades
    def __init__(self):
        self.nome: str = ''
        self.tipo: str = ''
        self.quant_turbinas: int = 0
        self.quant_vertedouros: int = 0
        self.quant_comportas: int = 0
        self.quant_energia: float = 0.0
        self.funcionando: bool = False
    # Métodos ou comportamentos ou ações ou funções
    def gerar_energia(self): pass
    def transformar_energia(self): pass
    def ativar_eclusas(self):pass
    def abrir_comportas(self):pass
    def ligar_turbinas(self, ligar:bool):
        if ligar == True:
            print('Ligando turbinas')
        else:
            print("Desligando turbinas")
            
    def distribuir_energia(self):pass



