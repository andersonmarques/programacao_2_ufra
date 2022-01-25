class Projeto:
    
    def __init__(self, identificacao = None, custo_obra = None, area_desmatada = None, 
    impacto_ambiental = None, status_obra = None, reducao_imp_amb = None) -> None:
        self.identificacao = identificacao
        self.custo_obra = custo_obra
        self.area_destada = area_desmatada
        self.impacto_ambiental = impacto_ambiental
        self.status_obra = status_obra
        self.reducao_imp_amb = reducao_imp_amb
        self.erro = ''

    @property
    def identificacao(self):
        return self.__identificacao

    @identificacao.setter
    def identificacao(self, id):
        if id != None and len(id) != 0:
            self.__identificacao = id
        else:
            self.erro = 'O campo \"id\" é obrigatório!'

    @property
    def custo_obra(self):
        return self.__custo_obra

    @custo_obra.setter
    def custo_obra(self, custo_obra):
        if custo_obra != None and len(custo_obra) != 0:
            self.__custo_obra = custo_obra
        else:
            self.erro = 'O campo \"custo da obra\" é obrigatório!'

    @property
    def area_destada(self):
        return self.__area_destada

    @area_destada.setter
    def area_destada(self, area_destada):
        self.__area_destada = area_destada

    @property
    def impacto_ambiental(self):
        return self.__impacto_ambiental

    @impacto_ambiental.setter
    def impacto_ambiental(self, impacto_ambiental):
        self.__impacto_ambiental = impacto_ambiental

    @property
    def status_obra(self):
        return self.__status_obra

    @status_obra.setter
    def status_obra(self, status_obra):
        self.__status_obra = status_obra

    @property
    def reducao_imp_amb(self):
        return self.__reducao_imp_amb

    @reducao_imp_amb.setter
    def reducao_imp_amb(self, reducao_imp_amb):
        self.__reducao_imp_amb = reducao_imp_amb