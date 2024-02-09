def inverte_numero(numero):
    return int(str(numero)[::-1])

def e_capicua(numero):
    return numero == inverte_numero(numero)

def gera_capicua(n):
    for _ in range(4):
        n += inverte_numero(n)
        if e_capicua(n):
            return n
    return 0

# Entrada do usuário
numero_input = int(input())

# Verifica e imprime o resultado
resultado = gera_capicua(numero_input)
print(resultado)