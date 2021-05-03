def extrai_valor (carta):
    if len(carta) == 3:
        return carta[0]+carta[1]
    else:
        return carta[0]

L1=['A♦', 'J♥', 'Q♣', 'K♠', '10♣']
print (extrai_naipe(L1))