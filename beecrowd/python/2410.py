n = int(input())

presences = []
for i in range(n):
    presences.append(input())
print(len(dict.fromkeys(presences)))