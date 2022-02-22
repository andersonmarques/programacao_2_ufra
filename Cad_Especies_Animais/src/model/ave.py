from model.animal import Animal


class Ave (Animal):

    def __init__(self, idade=None, especie=None, subespecie=None, quant_patas = None) -> None:
        super().__init__(idade, especie, subespecie)
        self.quant_patas = quant_patas

    @property
    def quant_patas(self):
        return self.__quant_patas

    @quant_patas.setter
    def quant_patas(self, value):
        self.__quant_patas = value

    def __str__(self):
        return f'{self.especie} : {self.subespecie} : {Ave.__class__}'
    

    