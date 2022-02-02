class Gerenciador_Animais:
    def __init__(self) -> None:
        self.lista_animais = None #banco de dados FAKE

    def verificar_ultimo_id(self):
        tamanho_lista = len(self.lista_animais)
        if tamanho_lista == 0:
            return 0
        else:
            ultimo_animal = self.lista_animais[tamanho_lista - 1]
            id = ultimo_animal.id
            return int(id)

    def remover_animal_lista(self, posicao = None):
        msg = ''
        # print(f'----------- {bool(self.lista_animais)}')
        if not bool(self.lista_animais):# nao V = F; nao F = V
            #se a lista estiver vazia, este teste sera verdadeiro. Pois bool(lista_vazia) retornara False
            msg = 'Erro! Lista vazia.'
        elif posicao == None:
            posicao_ultimo_elemento = len(self.lista_animais) - 1
            self.lista_animais.remove(self.lista_animais[posicao_ultimo_elemento])#remove o ultimo elemento da lista
            msg = 'Animal removido com sucesso.'    
        elif posicao > (len(self.lista_animais) - 1):
            msg = 'Erro! Posição inválida.'
        else:
            # self.lista_animais.remove(len(self.lista_animais) - 1)
            del self.lista_animais[posicao]
            msg = 'Animal removido com sucesso.'    
        return msg
            

    def salvar_animal(self, animal) -> str:
        '''
        Salvar um novo animal em uma lista
        '''
        self.lista_animais.append(animal)
        return f'Animal (id: {animal.id}) salvo com sucesso!'

    def salvar_animal_em_arquivo(self, animal):
        saida = ''
        # for a in self.lista_animais:
        #     saida += f'{a.id}|{a.nome}|{a.idade}|{a.especie}|{a.subespecie}|{a.classificacao}|{a.habitat}\n'
        saida += f'{animal.id}|{animal.nome}|{animal.idade}|{animal.especie}|{animal.subespecie}|{animal.classificacao}|{animal.habitat}\n'
        #w: escrever
        #r: ler
        #a: adicionar uma linha ao final de um arquivo (com conteudo)
        with open('arquivo.txt', 'a', encoding='UTF-8') as arq:            
            arq.write(saida)
        
    def ler_animais_arquivo(self):
        lista_linhas = []
        msg = ''
        erro = False
        try:#tentar executar o bloco do "try"
            with open('arquivo.txt', 'r', encoding='UTF-8') as arq:
                # saida = arq.read() -> retorna todo arquivo em uma string (gigante)
                lista_linhas = arq.readlines() #retona uma lista de strings (cada linha sera um item da lista)
        except FileNotFoundError:
            msg = 'Arquivo não encontrado!'
            erro = True
        else:
             msg = 'Arquivo lido com sucesso!'
        finally:#sempre executa esse bloco do finally
            #listas [] - mutavel
            #tuplas () - imutavel 
            return lista_linhas, msg, erro #tupla


    @property
    def lista_animais(self):
        return self.__lista_animais

    @lista_animais.setter
    def lista_animais(self, value):
        self.__lista_animais = []


