from mae import Mae

class Filho (Mae):
    def __init__(self, nome='', alt=170):
        super().__init__(alt = alt)
        self.__nome = nome
        self.sexo = ''
        