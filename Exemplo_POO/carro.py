class Carro:
    def __init__(self) -> None:
        self.velocidade             :float  = 0
        self.cor                    :str    = 'vermelho'
        self.quant_cintos_seguranca :int    = 4
        self.quant_portas           :int    = 4
        self.potencia               :int    = 105
        self.tracao                 :str    = '4x4'
        self.quant_passageiros      :int    = 0
        self.marcha_atual           :int    = 0 #0-neutro
        self.quant_marchas          :int    = 6 #6-ré
    
    def acelerar(self, velocidade_atual) -> str:
        self.velocidade = velocidade_atual+1
        return f'Acelerando....{self.velocidade}'
    
    def freiar(self, velocidade_atual) -> str:
        self.velocidade = velocidade_atual - 1
        return f'Freiando....{self.velocidade}'

    def ligar(self, virar_chave:bool) -> str:
        if virar_chave == True:
             return 'Ligando o carro'
        else:
            return 'Desligando o carro'
        
    def tocar_musica(self, start_radio: bool, nome_musica:str):
        if start_radio == True:
            return f"Tocar musica: {nome_musica}"
        else:
            return 'Desligando player de musica'

    def assistir_filme(self, start_player, nome_filme):
        if start_player == True:
            return f"Reproduzir filme: {nome_filme}"
        else:
            return 'Desligando player de filme'
    
    def transportar_pessoas(self, embarcou):
        if embarcou == True:
            return self.quant_passageiros + 1
        else:
            return self.quant_passageiros - 1
    
    def passar_marcha(self, re: bool):
        if self.velocidade == 0:
            if re == True:
                self.marcha_atual = 6
            else:
                self.marcha_atual = 1
        elif self.velocidade == 20:
            self.marcha_atual = 2
        elif self.velocidade == 30:
            self.marcha_atual = 3
        elif self.velocidade == 40:
            self.marcha_atual = 4
        elif self.velocidade >= 50:
            self.marcha_atual = 5
        
        return self.marcha_atual