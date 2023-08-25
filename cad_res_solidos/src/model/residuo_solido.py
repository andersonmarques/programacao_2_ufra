
class Residuo_Solido:
    def __init__(self, material = None, quant = None, organico = None) -> None:
        self.error = ''
        self.material = material
        self.quantidade = quant
        self.organico = organico

    @property
    def material(self) -> str:
        return self.__material
    
    @material.setter
    def material(self, material):
        if material != None and len(material) != 0:
            self.__material = material
            self.error = ''
        else:
            self.error = 'O "material" é obrigatório'

    @property
    def quantidade(self) -> int:
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        try:
            if quantidade == '0':             
                raise Exception('A "quantidade" deve ser um valor maior que zero!')
            self.__quantidade = int(quantidade)
            self.error = ''
        except ValueError:
            self.error = 'A "quantidade" é obrigatória e deve ser um valor numérico!'        
        except Exception as e:
            self.error = f'{e.__str__()}'

    @property
    def organico(self) -> bool:
        return self.__organico
    
    @organico.setter
    def organico(self, organico):
        if organico == None:
            self.error = 'O "campo orgânico" é obrigatório'
            self.error = ''
        else:
            self.__organico = organico

    def __str__(self) -> str:
        is_organico = 'sim' if self.organico else 'não'
        return f'{self.material}\t \
{self.quantidade}\t \
{is_organico}'


# var_ref = Residuo_Solido('Papel', 10, False)
# print(var_ref)
