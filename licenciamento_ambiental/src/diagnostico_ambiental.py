
class Diagnostico_Ambiental:
    def __init__(self, empreendimento = None, 
                 matricula = None,
                 area = None) -> None:
        self.empreendimento = empreendimento
        self.matricula = matricula
        self.area = area

        #encapsulamento dos atributos
