def extrai_naipe (carta):
    if len(carta) == 3:
        return carta[2]
    else:
        return carta[1]

L1=['A♦', 'J♥', 'Q♣', 'K♠', '10♣']
print (extrai_naipe(L1))