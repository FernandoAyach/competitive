def ordenar_logs(logs):
    logs_ordenados = sorted(logs, key=lambda x: (x[0], x[1]))
    return logs_ordenados

logs = []

while True:
    try:
        linha = input().strip()
        if not linha:
            break
        logs.append(tuple(linha.split(' ', 1)))  
    except EOFError:
        break

logs_ordenados = ordenar_logs(logs)

for log in logs_ordenados:
    print(' '.join(log))