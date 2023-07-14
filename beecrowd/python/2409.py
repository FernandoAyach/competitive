a, b, c = map(int, input().split())
h, w = map(int, input().split())

if (a <= h and b <= w) or \
    (a <= h and c <= w) or \
    (b <= h and a <= w) or \
    (b <= h and c <= w) or \
    (c <= h and a <= w) or \
    (c <= h and b <= w):
    print('S')
else:
    print('N')