#Import Bibliotecas
import random
#Print Inicial
#Criar Baralho
def cria_baralho ():
    cartas=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    niepes=["♠","♥","♦","♣"]
    baralho=[]
    for e in niepes:
        for i in cartas:
            carta=i+e
            baralho.append(carta)
    random.shuffle(baralho)
    return baralho
<<<<<<< HEAD

def extrai_naipe (carta):
    if len(carta) == 3:
        return carta[2]
    else:
        return carta[1]

def extrai_valor (carta):
    if len(carta) == 3:
        return carta[0]+carta[1]
    else:
        return carta[0]
def lista_movimentos_possiveis (b,p):
    l_mov=[]
    if p==0:
        return []
    if extrai_naipe(b[p])==extrai_naipe(b[p-1]):
        l_mov.append(1)
    elif extrai_valor (b[p])==extrai_valor(b[p-1]):
        l_mov.append(1)
    if extrai_naipe(b[p])==extrai_naipe(b[p-3]) and (p-3) >=0:
        l_mov.append(3)
    elif extrai_valor(b[p]) == extrai_valor(b[p-3]) and (p-3)>=0:
        l_mov.append(3)
    return l_mov

def possui_movimentos_possiveis(b):
    i = 0
    while i < len(b):
        a = lista_movimentos_possiveis(b, i)
        if a != []:
            return True
        else:
            i += 1
    return False
=======
>>>>>>> ead8da7233c8501d381a4771551945b8490811e5
