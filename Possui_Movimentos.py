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



L1=['A♦', '10♥', 'Q♣', 'K♠','10♣','4♠']
print (possui_movimentos_possiveis(L1))