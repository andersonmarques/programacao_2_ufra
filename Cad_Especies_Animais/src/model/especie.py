from model.genero import Genero
# class Genero:
#     def __init__(self, nome = None) -> None:
#         self.nome = nome



class Especie:
    def __init__(self, nome = None, genero = None) -> None:
        self.nome = nome
        self.genero = genero

    def __str__(self) -> str:
        genero = '___' if self.genero is None else self.genero
        especie = '___' if self.nome is None else self.nome
        return f'{genero} > Especie: {especie}'
        # return f''
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def genero(self) -> Genero: #indica que retornara um objeto Genero
        return self.__genero

    @genero.setter
    def genero(self, value):
        self.__genero = value

# def main():
#     a1 = Especie()
#     a2 = Especie('Anodorhynchus_hyacinthinus')
#     a3 = Especie('A. hyacinthinus', Genero())
#     a4 = Especie(None, Genero('Arinae'))

#     # print(a1)
#     # print(a2)
#     # print(a3)
#     print(Genero(nome='Arinae'))

# main()



