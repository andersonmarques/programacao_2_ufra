from mae import Mae
from filho import Filho

ref_mae = Mae(alt = 180)
ref_filho = Filho('João')

# print(ref_mae.__nome)
print(ref_mae.idade)
ref_mae.idade = 39
print(ref_mae.idade)
ref_mae.idade = 41
ref_mae.cor_olhos = 'azul'
print(ref_mae.idade)
print(f'Glicose mãe: {ref_mae._glicose}')
# print(ref_filho.__nome)
print(f'Glicose filho:  {ref_filho._glicose}')
print(ref_filho.time_coracao)