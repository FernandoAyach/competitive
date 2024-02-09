naipes = {0: "Paus", 1: "Ouro", 2: "Coração", 3: "Espada"}

def converter_carta(valor):
    if valor == 1:
        return "Às"
    elif valor == 11:
        return "Valete"
    elif valor == 12:
        return "Dama"
    elif valor == 13:
        return "Rei"
    else:
        return str(valor)

naipe, carta = map(int, input().split())

carta_convertida = converter_carta(carta)

naipe_convertido = naipes[naipe]

print(f"{carta_convertida} de {naipe_convertido}")