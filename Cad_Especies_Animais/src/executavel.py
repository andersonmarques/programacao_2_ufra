from model.classe import Classe
from model.especie import Especie#, Genero
from model.familia import Familia
from model.genero import Genero
from model.ordem import Ordem

def criar_classes():
    mammalia = Classe(nome='mamifero')
    aves = Classe(nome='aves')     
    lista_classes = [mammalia, aves]
    return lista_classes

def criar_ordens(c: Classe):
    psittaciformes = Ordem(nome='Psittaciformes', classe = c)
    rheiformes = Ordem(nome='Rheiformes', classe = c)
    eurypygiformes = Ordem(nome='Eurypygiformes', classe = c)    
    c.lista_ordens.append(psittaciformes)
    c.lista_ordens.append(rheiformes)
    c.lista_ordens.append(eurypygiformes)    
    return c.lista_ordens

def criar_familias(o: Ordem):
    strigopidae = Familia(nome='Strigopidae', ordem = o)
    psittacidae = Familia(nome='Psittacidae', ordem = o)
    cacatuidae = Familia(nome='cacatuidae', ordem = o)    
    o.lista_familias.append(strigopidae)
    o.lista_familias.append(psittacidae)
    o.lista_familias.append(cacatuidae)
    return o.lista_familias

def criar_generos(f: Familia):
    arinae = Genero(nome='Arinae', familia = f)
    psittacinae = Genero(nome='Psittacinae', familia = f)
    # arinae = Genero(nome='Arinae')
    # psittacinae = Genero(nome='Psittacinae')
    f.lista_generos.append(arinae)
    f.lista_generos.append(psittacinae)
    return f.lista_generos

def main():       
    ordens = criar_ordens(criar_classes()[1])
    familias = criar_familias(ordens[0])
    generos = criar_generos(familias[1])    
    arara_azul = Especie('Anodorhynchus hyacinthinus', generos[0])
    # arara = Especie('Anodorhynchus hyacinthinus', Genero())
    # arara = Especie()
    # arara_ = Especie('Anodorhynchus hyacinthinus')
    # azul = Especie('Anodorhynchus hyacinthinus', Genero())
    # _azul = Especie(None, Genero('Arinae'))

    print(arara_azul.genero.familia.ordem.classe)
    print(arara_azul.genero.familia.ordem)
    print(arara_azul.genero.familia)
    print('======= cheia =======')
    for i in arara_azul.genero.familia.lista_generos:
        print(i)
    arara_azul.genero.familia.lista_generos = []
    print('======= limpa? =======')
    for i in arara_azul.genero.familia.lista_generos:
        print(i)
    print(arara_azul)
    # print(azul)
    # print(_azul)

main()

