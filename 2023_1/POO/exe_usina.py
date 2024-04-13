from usina import Usina
x = 5
# Instanciando um objeto da classe Usina
referencia_obj: Usina = Usina()#metodo constutor
print(referencia_obj)
referencia_obj.tipo = 'Hidrelétrica'
referencia_obj.nome = 'Capanemaipu'
print(referencia_obj.nome)
print(referencia_obj.tipo)
# print(f'Endereço do objeto: {minha_variavel}')
# print(minha_variavel.tipo)
# minha_variavel.ligar_turbinas(True)
outro_obj = Usina("Ouricuripu")
print(outro_obj.nome)

