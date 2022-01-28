class Gerenciador_Animais:
    def __init__(self) -> None:
        self.lista_animais = None

    def salvar_animal(self, animal) -> str:
        self.lista_animais.append(animal)
        return f'Animal (id: {animal.id}) salvo com sucesso!'

    def salvar_animal_em_arquivo(self):
        saida = ''
        for a in self.lista_animais:
            saida += f'{a.id}|{a.nome}|{a.idade}|{a.especie}|{a.subespecie}|{a.classificacao}|{a.habitat}\n'

        #w: escrever
        #r: ler
        #a: adicionar uma linha a um arquivo com conteudo
        with open('arquivo.txt', 'a') as arq:            
            arq.write(saida)
        
    def ler_animais_arquivo(self):
        saida = ''
        try:#tentar executar o bloco do "try"
            with open('arquivo.txt', 'r') as arq:
                saida = arq.read()
        except FileNotFoundError:
            saida = 'Arquivo não encontrado!'
        # else:
        #     pass
        finally:#sempre executa esse bloco do finally
            return saida


    @property
    def lista_animais(self):
        return self.__lista_animais

    @lista_animais.setter
    def lista_animais(self, value):
        self.__lista_animais = []


