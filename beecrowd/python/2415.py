n = input()
numbers = list((map(int, input().split())))

current_sequence_number = numbers[0]
current_score = 0
scores = []

for number in numbers:

    if number == current_sequence_number:
        current_score +=1
    else:
        scores.append(current_score)
        current_score = 1
        current_sequence_number = number
scores.append(current_score)
print(max(scores))