encrypted_message_s = input()
crib_s = input()

encrypted_message = []
crib = []
possible_positions = 0

for letter in encrypted_message_s:
    encrypted_message.append(letter)   

for letter in crib_s:
    crib.append(letter) 

while len(encrypted_message) >= len(crib):
    i = 0
    while i < len(crib):
        if crib[i] == encrypted_message[i]:
            break
        i += 1
        if i == len(crib):
            possible_positions += 1
       
    encrypted_message.remove(encrypted_message[0])
print(possible_positions)