while True:
    
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    
    if a != b and a != c:
        player1 = 'B'
        player2 = 'C'
        break
    elif b != a and b != c:
        player1 = 'A'
        player2 = 'C'
        break
    if c != a and c != b:
        player1 = 'A'
        player2 = 'B'
        break
    
print(player1, player2)

bet1, bet2 = input().split()
n1, n2 = input().split()
n1 = int(n1)
n2 = int(n2)

total = n1 + n2

if total % 2 == 0:
    
    if bet1 == 'par':
        print(player1, 'par', total)
    else:
        print(player2, 'par', total)
else:
    if bet1 == 'ímpar':
        print(player1, 'ímpar', total)
    else:
        print(player2, 'ímpar', total)