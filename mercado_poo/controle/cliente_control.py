from entidades.cliente import Cliente

class Cliente_Control:
    
    def __init__(self) -> None:
        self.lista_clientes = None #nosso falso banco de dados (fake DB)

    def salvar_cliente(self, cliente):
        self.lista_clientes.append(cliente)
        
        return 'Cliente salvo com sucesso!'

    @property
    def lista_clientes(self):
        return self.__lista_clientes

    @lista_clientes.setter
    def lista_clientes(self, lista):
        self.__lista_clientes = []
    
    def excluir_cliente(self, indice):
        # cliente = self.lista_clientes[indice]
        # self.lista_clientes.remove(cliente)
        #ou podemos remover com a palavra del
        del self.lista_clientes[indice]
        return 'Cliente removido com sucesso!'
