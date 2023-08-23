class Escritor:

    def salvar_em_arquivo(self, conteudo):
            saida = ''
            
            saida += f'{conteudo.habitat}\n'
            #w: escrever
            #r: ler
            #a: adicionar uma linha ao final de um arquivo (com conteudo)
            with open('arquivo.txt', 'a', encoding='UTF-8') as arq:            
                arq.write(saida)


    