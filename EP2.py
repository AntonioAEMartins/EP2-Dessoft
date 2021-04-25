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
