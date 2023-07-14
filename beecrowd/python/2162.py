def last_position():
    return total_heights - 1

total_heights = int(input())
heights = list((map(int, input().split())))
there_is_pattern = True

if heights[1] > heights[0]:  # Picos estão nas posições impares 

    for position in range(1, total_heights, 2):

        if position == last_position():
            if heights[position] <= heights[position - 1]:
                there_is_pattern = False
                print(0)
                break
        else:
            if heights[position] <= heights[position - 1] or heights[position] <= heights[position + 1]:
                there_is_pattern = False
                print(0)
                break
elif heights[1] < heights[0]: # Picos estão nas posições pares

    for position in range(1, total_heights, 2):

        if position == last_position():
            if heights[position] >= heights[position - 1]:
                there_is_pattern = False
                print(0)
                break
        else:
            if heights[position] >= heights[position - 1] or heights[position] >= heights[position + 1]:
                there_is_pattern = False
                print(0)
                break
else:
    there_is_pattern = False
    print(0)

if there_is_pattern:
    print(1)