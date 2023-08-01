from usina import Usina
# Instanciando um objeto da classe Usina
minha_usina: Usina = Usina()
minha_usina.tipo = 'Hidrelétrica'
minha_usina.nome = 'Capanemaipu'

print(f'Endereço do objeto: {minha_usina}')
print(minha_usina.tipo)
minha_usina.ligar_turbinas(True)

