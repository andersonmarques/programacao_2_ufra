class Gerente_Arquivos:

    def salvar_em_arquivo(self, conteudo):
            saida = f'{conteudo}\n'
            #w: escrever
            #r: ler
            #a: adicionar uma linha ao final de um arquivo (com conteudo)
            with open('arquivo.txt', 'a', encoding='UTF-8') as arq:            
                arq.write(saida)

    def leitor_arquivo_1(self, dir_arquivo: str):
        with open(dir_arquivo, 'r', encoding='UTF-8') as arq:
            conteudo = arq.read()

        return conteudo

    def leitor_arquivo_2(self, dir_arquivo: str):
        with open(dir_arquivo, 'r', encoding='UTF-8') as arq:
            conteudo = arq.readline()  

        return conteudo

    def leitor_arquivo_3(self, dir_arquivo: str):
        with open(dir_arquivo, 'r', encoding='UTF-8') as arquivo:
            conteudo = arquivo.readlines()  

        return conteudo
    

# ref = Gerente_Arquivos()
# ref.salvar_em_arquivo('Escrevendo por cima de')
# print(ref.leitor_arquivo_3('arquivo.txt'))