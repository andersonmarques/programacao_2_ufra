class Animal:
    def __init__(self, genero = None, especie = None, subespecie = None) -> None:
        self.genero = genero
        self.especie = especie
        self.subespecie = subespecie

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        if genero is not None and not genero:
            self.__genero = genero
        else:
            self.erro = 'O campo genero é obrigatório.'

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, especie):               
        if especie == '---':
            self.erro = 'O campo especie é obrigatório.'
        else:
            self.__especie = especie
        
    @property
    def subespecie(self):
        return self.__subespecie

    @subespecie.setter
    def subespecie(self, subespecie):
        if subespecie == '---':
        # eh porque o ususario escolheu os '---'
            self.erro = 'O campo subespecie é obrigatório.'
        else:
            self.__subespecie = subespecie