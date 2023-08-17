
class Residuo_Solido:
    def __init__(self, material = None, quant = None, organico = None) -> None:
        self.error = ''
        self.material = material
        self.quantidade = quant
        self.organico = organico

    @property
    def material(self):
        return self.__material
    
    @material.setter
    def material(self, material):
        if material != None and len(material) != 0:
            self.__material = material
        else:
            self.error = 'O "material" é obrigatório'

    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        if quantidade == 0:
            self.error = 'A "quantidade" é obrigatória!'
        else:
            self.__quantidade = quantidade

    @property
    def organico(self):
        return self.__organico
    
    @organico.setter
    def organico(self, organico):
        if organico == None or organico == '':
            self.error = 'O "campo orgânico" é obrigatório'
        else:
            self.__organico = organico

    def __str__(self) -> str:
        is_organico = 'sim' if self.organico else 'não'
        return f'Material: {self.material} | \
Quantidade: {self.quantidade} | \
É organico? {is_organico}'


# var_ref = Residuo_Solido('Papel', 10, False)
# print(var_ref)