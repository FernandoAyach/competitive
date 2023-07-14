import math  # Importa o módulo math

n = int(input())  # Coleta a quantidade de termos

five_number = 5  # Define o número de padrao x5
log_number = 4  # Define o número de padrao log
double_number = 2  # Define o número de padrao x2

total = 0  # Inicia variável para soma dos valores

term = five_number / double_number  # Calcula o termo
total += term  # Soma o termo no total

print('{:.2f}'.format(term), end = '')  # Mostra o termo

for i in range(2, n + 1):  # Inicia um loop de intervalo [1, n]
    five_number = five_number * 5  # Multiplica five_number por 5
    
    if i % 2 == 1:  # Se for posição impar
        double_number *= 2  # Dobra o valor de double_number
        term = five_number / double_number  # Calcula o termo
        total += term  # Soma o termo no total
        
    else:  # Se for par
        term = five_number / math.log2(log_number)  # Calcula o termo
        term = -term  # Inverte o valor do termo
        total += term  # Soma o termo no total
        
        log_number *= 4  # Multiplica log_number por 4
    
    print(' {:.2f}'.format(term), end = '')  # Mostra o termo
print()  # Pula uma linha
print('{:.2f}'.format(total))  # Imprime a soma total
            
   
    



