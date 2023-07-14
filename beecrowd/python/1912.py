n, area = map(int, input().split())
while n != 0:
    lenghts = list(map(int, input().split()))

    k = sum(lenghts)
    h = (k - area) / n

    if h == 0:
        print(":D")
    elif h > 0:
        print("{:.4f}".format(h))
    else:
        print("-.-")

    n, area = map(int, input().split())
