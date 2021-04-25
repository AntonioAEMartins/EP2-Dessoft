#Import Bibliotecas
import random
from matl
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

def possui_movimentos_possiveis(baralho):
    naipe=[]
    valor=[]
    for e in baralho:
        naipe.append(extrai_naipe(e))
        valor.append(extrai_valor(e))
    estado=False
    t=1
    if naipe[t]==naipe[t-1]:
        estado = True
    elif valor[t]==valor[t-1]:
        estado=True
    while t<(len(baralho)):
        if naipe[t]==naipe[t-3] and (t-3) >=0:
            estado=True
        elif valor[t] == valor[t-3] and (t-3)>=0:
            estado=True
        t+=1
    return estado