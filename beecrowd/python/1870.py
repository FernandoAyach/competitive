# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def find_ventilators_and_power(position, line, n_columns):
    nearest_left = 0
    power_left = 0
    nearest_right = 0
    power_right = 0
    
    for i in range(position, -1, -1):
        if int(line[i]) != 0:
            nearest_left = i
            power_left = int(line[i])
            break
    
    for i in range(position, n_columns):
        if int(line[i]) != 0:
            nearest_right = i
            power_right = int(line[i])
            break
    
    return [nearest_left, power_left, nearest_right, power_right]

def next_position(position, nearest_left, nearest_right, power_left, power_right):
    result = power_left - power_right
    new_position = position + result
    
    if new_position == nearest_left:
        return [True, nearest_left]
    if new_position == nearest_right:
        return [True, nearest_right]
    
    return [False, new_position]

while True:
   
    lines, columns, init_column = input().split()
    
    if lines == "0":
        break
     
    lines = int(lines)
    columns = int(columns)
    init_column = int(init_column)
    current_position = init_column - 1
    
    boom = False
    for i in range(lines):
        line = input().split()
        
        if boom:
            continue
        
        nearest_left, power_left, nearest_right, power_right = find_ventilators_and_power(current_position, line, columns)
        
        if current_position == nearest_left or current_position == nearest_right:
            print("BOOM", i + 1, current_position + 1)
            boom = True
            continue
        
        is_boom_position, position = next_position(current_position, nearest_left, nearest_right, power_left, power_right)
         
        if is_boom_position:
            print("BOOM", i + 1, position + 1)
            boom = True
        else:
            current_position = position
            
    if not boom: 
        print("OUT", position + 1)
       