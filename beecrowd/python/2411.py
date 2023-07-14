n = int(input())
movements = list((map(int, input().split())))

X = 0
Y = 1

done_movements = 0
stop = False

holes = [[1, 3], [2, 3], [2, 5], [5, 4]]
horse_position = [4, 3]

for movement in movements:

    if movement == 1:
        horse_position[X] += 1
        horse_position[Y] += 2
    elif movement == 2:
        horse_position[X] += 2
        horse_position[Y] += 1
    elif movement == 3:
        horse_position[X] += 2
        horse_position[Y] -= 1
    elif movement == 4:
        horse_position[X] += 1
        horse_position[Y] -= 2
    elif movement == 5:
        horse_position[X] -= 1
        horse_position[Y] -= 2
    elif movement == 6:
        horse_position[X] -= 2
        horse_position[Y] -= 1
    elif movement == 7:
        horse_position[X] -= 2
        horse_position[Y] += 1
    else:
        horse_position[X] -= 1
        horse_position[Y] += 2
    
    for hole in holes:

        if horse_position[X] == hole[X] and horse_position[Y] == hole[Y]:
            done_movements += 1
            stop = True
            break
    
    if stop:
        break
    done_movements += 1
print(done_movements)
    
