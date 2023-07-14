i, f = input().split()
i = int(i)
f = int(f)

print(i, end = '')

n = i - f

for i in range(i - 1, f - 1, -1):
    
    for s in range(n):
        print(' ', end = '')
    
    n -= 1
    print(i, end = '')
print()
    