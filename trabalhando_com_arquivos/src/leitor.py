class Leitor:

    def leitor_arquivo_1(self, dir_arquivo: str):
        with open(dir_arquivo, 'r', encoding='UTF-8') as arquivo:
            conteudo = arquivo.read()

        return conteudo

    def leitor_arquivo_2(self, dir_arquivo: str):
        with open(dir_arquivo, 'r', encoding='UTF-8') as arquivo:
            conteudo = arquivo.readline()  

        return conteudo

    def leitor_arquivo_3(self, dir_arquivo: str):
        with open(dir_arquivo, 'r', encoding='UTF-8') as arquivo:
            conteudo = arquivo.readlines()  

        return conteudo

ref = Leitor()
print(ref.leitor_arquivo_3('README.md')) 



# print(ref.leitor_arquivo_1('README.md'))
# print(ref.leitor_arquivo_2('README.md'))

# print('--------------')


# print('--------------')



