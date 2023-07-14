index_fibonot = int(input())

stop = False

first = 1
second = 1
counter = 0
while not stop:
    next_fibonacci = first + second
    first = second
    second = next_fibonacci

    for i in range(first + 1, second):
        counter += 1

        if counter == index_fibonot:
            print(i)
            stop = True
            break
