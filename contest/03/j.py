def calcular_valor_final(I, L, N):
    valor_final = I + (N - 1) * L
    return valor_final

I = float(input())
L = float(input())
N = int(input())

resultado = calcular_valor_final(I, L, N)
print(f"{resultado:.1f}")