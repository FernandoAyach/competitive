# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

paths = [0] * n
for i in range(n):
    
    _trail = input().split()
    trail = [0] * (len(_trail) - 1)
    
    for j in range(1, len(_trail)):
        trail[j - 1] = int(_trail[j])
    
    left_path = 0
    right_path = 0
    best_path = 0
    
    for j in range(len(trail) - 1):
        
        if trail[j + 1] > trail[j]:
            left_path += trail[j + 1] - trail[j]
    
    for j in range(len(trail) - 1, 0, -1):
        
        if trail[j - 1] > trail[j]:
            right_path += trail[j - 1] - trail[j]  
    
    best_path = left_path
    
    if right_path < best_path:
        best_path = right_path
        
    paths[i] = best_path

minor = paths[0]
position = 1
for i in range(1, len(paths)):
    
    if paths[i] < minor:
        minor = paths[i]
        position = i + 1
print(position)
    
    
    
    
    
    
    
    



