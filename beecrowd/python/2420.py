quant_sections = int(input())
sections = list((map(int, input().split())))

total_territory = 0
for section in sections:
    total_territory += section
middle = total_territory // 2

current_territory = 0
i = 0
while i <= quant_sections:
    current_territory += sections[i]
    
    if current_territory == middle:
        print(i + 1) 
        break
    i += 1