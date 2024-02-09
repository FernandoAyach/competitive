import math

def calcular_valor_total(valor_conta, idade_cliente):
    if idade_cliente <= 5:
        valor_total = valor_conta * 0.5
    elif 5 < idade_cliente < 18:
        valor_total = valor_conta * 0.95
    elif 18 <= idade_cliente < 60:
        valor_total = valor_conta * 1.1
    else:
        valor_total = valor_conta * 0.85

    return math.ceil(valor_total * 100) / 100 

valor_conta = float(input())
idade_cliente = int(input())

resultado = calcular_valor_total(valor_conta, idade_cliente)
print(resultado)