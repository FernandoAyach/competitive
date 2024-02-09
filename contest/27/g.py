nums = list(map(int, input().split(" ")))

nums = sorted(nums)
size = len(nums)

i = 0
for n in nums:
    if n == 1:
        print("A", end = "")
    elif n == 11:
        print("J", end = "")
    elif n == 12:
        print("Q", end = "")
    elif n == 13:
        print("K", end = "")
    else:
        print(n, end = "")

    if i == size - 1:
        print()
    else:
        print("", end = " ")
    

    i += 1
    
