from carro import Carro

ref_carro = Carro()

print(f'Antes: {ref_carro.cor}')#original
ref_carro.cor = 'Branca'
print(f'Depois: {ref_carro.cor}')#mudança
print(ref_carro.ligar(virar_chave=True))
for v in range(0, 101):
    print(ref_carro.passar_marcha(re=False))
    print(ref_carro.acelerar(v))

for v in range(101, 0, -1):
    print(ref_carro.passar_marcha(re=False))
    print(ref_carro.freiar(v))

print(ref_carro.ligar(False))