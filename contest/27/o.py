def insertion_sort_comparisons(string):
    comparisons = 0
    array = list(string)
    length = len(array)

    for i in range(1, length):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            comparisons += 1
        array[j + 1] = key

    comparisons += length - 1

    return comparisons

t = int(input())

for _ in range(t):
    string = input().strip()
    total_comparisons = insertion_sort_comparisons(string)
    print(total_comparisons)