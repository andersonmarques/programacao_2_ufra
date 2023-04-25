
class Diagnostico_Ambiental:
    def __init__(self, empreendimento = '', 
                 matricula = "",
                 area = None) -> None:
        self.erro = ''
        self.empreendimento = empreendimento
        self.matricula = matricula
        self.area = area

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
            self.erro = "Erro, no campo área. Siga o modelo ex: 100.50"

    @property
    def empreendimento(self):
        return self.__empreendimento
    
    @empreendimento.setter
    def empreendimento(self, empreendimento):
        if empreendimento:
            self.__empreendimento = empreendimento
        else:
            self.__erro = 'O campo "empreendimento" é obrigatório!'

    @property
    def matricula(self):
        return self.__matricula 
    
    @matricula.setter
    def matricula(self, matricula):
        if matricula:
            self.__matricula = matricula
        else:
            self.__erro = 'O campo "matricula" é obrigatório!'


    @property
    def erro(self):
        return self.__erro
    
    @erro.setter
    def erro(self, e):
        self.__erro = e

