scores = list((map(int, input().split())))
scores.remove(max(scores))

print(max(scores))