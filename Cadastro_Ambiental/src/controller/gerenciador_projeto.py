class Gerenciador_Projeto:
    def __init__(self) -> None:
        self.pilha = None
  
    @property
    def pilha(self):
        return self.__pilha

    @pilha.setter
    def pilha(self, p):
        self.__pilha = []

    def cadastrar_projeto(self, projeto) -> str:
        '''
        Este método será responsável por receber um projeto
        como parâmetro e o inserir na pilha. Caso algum erro
        ocorra ao inserir o projeto na pilha o método deverá
        retornar uma mensagem de erro, informando o usuário 
        do problema ocorrido. Caso nenhum erro ocorra, o 
        método deverá enviar uma mensagem informando o 
        usuário de que o projeto foi adicionado a pilha.
        '''
        self.pilha.append(projeto)
        return 'Projeto empilhado com sucesso!'

    def desempilhar_projeto(self):
        '''
        Este método será responsável por retirar o projeto que 
        estiver no topo da pilha. Se ao tentar retirar um projeto 
        da pilha e a pilha esteja vazia, o método deverá enviar 
        uma mensagem de erro informando o usuário do problema 
        ocorrido. Se o projeto for retirado com sucesso da pilha, 
        o método deverá enviar uma mensagem de sucesso ao usuário.
        '''
        removeu = False
        if len(self.pilha) > 0:
            self.pilha.pop()
            removeu = True
            return 'Projeto saiu da pilha!', removeu
        else:
            return 'Pilha vazia!', removeu