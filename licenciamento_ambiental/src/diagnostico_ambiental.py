
class Diagnostico_Ambiental:
    def __init__(self, empreendimento = None, 
                 matricula = None,
                 area = None) -> None:
        self.empreendimento = empreendimento
        self.matricula = matricula
        self.area = area
        self.erro = ''

    #encapsulamento dos atributos
    # __ -> atributo privado
    # _ -> atributo protegido
    # sem nada -> atributo publico
    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        try:
            area = float(area)
            self.__area = area
        except:
            self.__area = 0
            self.erro = "Erro na conversão da área"

