# -*- coding: utf-8 -*-

n, m = input().split()
n = int(n)
m = int(m)

wanted_fruits = [""]*n
encrypted_fruits = [""]*m

for i in range(n + m):
    fruit = input()
    lower_fruit = ""
    
    for char in fruit:
        if ord(char) >= 65 and ord(char) <= 90:
            lower_code = ord(char) + 32
            lower_fruit += chr(lower_code)
        else:
            lower_fruit += char
            
    if i >= n:
        encrypted_fruits[i - n] = lower_fruit
    else:
        wanted_fruits[i] = lower_fruit

for wanted_fruit in wanted_fruits:
    like = False
    for encrypted_fruit in encrypted_fruits:
        
        if wanted_fruit in encrypted_fruit:
            print("Sheldon come a fruta", wanted_fruit)
            like = True
            break
        else:
            reverse_encrypted_fruit = ""
        
            for i in range(len(encrypted_fruit) - 1, -1, -1):
                reverse_encrypted_fruit += encrypted_fruit[i]
            
            if wanted_fruit in reverse_encrypted_fruit:
                print("Sheldon come a fruta", wanted_fruit)
                like = True
                break
    if not like:
        print("Sheldon detesta a fruta", wanted_fruit)
