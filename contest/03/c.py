def binario_para_decimal(binario):
    decimal = int(binario, 2)
    return decimal

n = int(input())

for _ in range(n):
    binario = input()

    resultado = binario_para_decimal(binario)
    print(resultado)