#Import Bibliotecas
import random
from colorama import Fore, Back, Style
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
#Pressione Enter para iniciar:
estado_inicial=True
while estado_inicial:
    comeca=input("Precione Enter para começar")
    if comeca == (""):
#Variaveis
        baralho = cria_baralho()
#Print Baralho
        existe_movimentos = possui_movimentos_possiveis(baralho)
        while existe_movimentos:
            i_baralho = 0
            numero = 1
            while i_baralho < len(baralho):
                naipe=extrai_naipe(baralho[i_baralho])
                if naipe == "♠":
                    print(Fore.RED + '{0}.  {1}'.format(numero, baralho[i_baralho]))
                if naipe == "♥":
                    print(Fore.WHITE + '{0}.  {1}'.format(numero, baralho[i_baralho]))
                if naipe == "♦":
                    print(Fore.GREEN + '{0}.  {1}'.format(numero, baralho[i_baralho]))
                if naipe == "♣":
                    print(Fore.YELLOW + '{0}.  {1}'.format(numero, baralho[i_baralho]))
                numero += 1
                i_baralho += 1
            a = True
            while a:
                p =  int(input(Fore.WHITE + "Escolha uma carta (digite um número entre 1 e {}):  ".format(numero-1)))
                if p >52 or p>=numero:
                    print("Posição inválida. Por favor, digite um número entre 1 e {}:  ".format(numero-1))
                    a =False
                    break
                possiveis_mov = lista_movimentos_possiveis(baralho, p-1)
                if possiveis_mov == []:
                    print ("A carta {0} não pode ser movida. Por favor, digite um número entre 1 e {1}:  ".format(baralho[p-1],numero-1))
                    a = False
                if possiveis_mov == [1]:
                    empilha(baralho, p-1, p-2)
                if possiveis_mov == [3]:
                    empilha(baralho,p-1, p-4)
                if possiveis_mov == [1, 3]:
                    b = True
                    while b:
                        print('Sobre qual carta você quer empilhar o {0}?'.format(baralho[p-1]))
                        print('1.  {0}'.format(baralho[p-2]))
                        print('2.  {0}'.format(baralho[p-4]))
                        posicao_empilha = int(input('Digite o número de sua escolha(1-2):  '))
                        if posicao_empilha == 1:
                            empilha(baralho, p-1, p-2)
                            b = False
                            break
                        if posicao_empilha == 2:
                            empilha(baralho, p-1, p-4)
                            b = False
                            break
                        else:
                            print('Posição inválida, digite um número entre 1 e 2:')
                            b= True
                a= False
            existe_movimentos = possui_movimentos_possiveis(baralho)
    if len(baralho) >1:
        print(Fore.RED + "Você Perdeu")
    else:
        print(Fore.GREEN + "Parabéns! Você ganhou")
    estado_final=input(Fore.WHITE + "Você quer jogar de novo? (sim/nao) ")
    if estado_final == "sim":
        estado_inicial = True
    if estado_final == "nao":
        estado_inicial = False
