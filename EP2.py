#Import Bibliotecas
import random
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
#Extrai Naipe
def extrai_naipe (carta):
    if len(carta) == 3:
        return carta[2]
    else:
        return carta[1]
#Extrai Valor
def extrai_valor (carta):
    if len(carta) == 3:
        return carta[0]+carta[1]
    else:
        return carta[0]
#Lista de Movimentos Possiveis
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
#Possui Movimentos Possiveis
def possui_movimentos_possiveis(b):
    i = 0
    while i < len(b):
        a = lista_movimentos_possiveis(b, i)
        if a != []:
            return True
        else:
            i += 1
    return False
#Empilha
def empilha(b,o,d):
    b[d]=b[o]
    del b[o]
    return b
#Print inicial
print("Paciência Acordeão")
print("==================")
print("")
print("Seja bem-vindo ao jogo de Paciência Acordeão! O objetivod este jogo é colocar todas as cartas em uma mesma pilha")
print("")
print("Existem apenas dois movimentos possíveis:")
print("")
print("1. Empilhar uma carta sobre a carta imediatamente anterior;")
print("2. Empilhar uma carta sobre a terceira carta anterior.")
print("")
print("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:")
print("")
print("1. As duas cartas possuem o mesmo valor ou")
print("2. As duas cartas possuem o mesmo naipe.")
print("")
print("Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.")
