class Mae:
    def __init__(self, nome = 'Maria', alt = 170):
        self.__nome = nome
        self.cor_olhos = 'Preto'
        self.cor_cabelo = 'Castanho claro'
        self.altura = alt
        self.cor_pele = 'Pardo'
        self._glicose = 120.0
        self.__roupas_intimas = ''
        self.time_coracao = 'paysandu'
        self.__idade = 40

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade > self.__idade:
            self.__idade = nova_idade
        else:
            print("Idade informada é inferior a idade atual.")

    