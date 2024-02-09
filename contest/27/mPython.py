N = int(input())

convidados = []

for _ in range(N):
    nome = input()
    convidados.append(nome)

convidados.sort()

for nome in convidados:
    print(nome)