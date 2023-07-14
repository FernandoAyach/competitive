def calculate_expression(expression_elements):
        result = []
        operator_index = 0
        while len(expression_elements) > 1: 

            while True:
                try:
                    expression_elements.index('*')
                except:
                    break

                for component in expression_elements:
                    print(expression_elements)
                    if component == '*':
                        operator_index = expression_elements.index(component)
                        result = get_intersection(operator_index, expression_elements)
                        replace_with_result(operator_index, result, expression_elements)
                        print(expression_elements)
                
            for component in expression_elements:  
                if component == '+':
                    operator_index = expression_elements.index(component)
                    result = get_union(operator_index, expression_elements)
                    replace_with_result(operator_index, result, expression_elements)
                    print(expression_elements)
                elif component == '-':
                    operator_index = expression_elements.index(component)
                    result = get_diference(operator_index, expression_elements)
                    replace_with_result(operator_index, result, expression_elements)
                    print(expression_elements)
        return result

def get_intersection(operator_index, expression_elements):  # Calcula a interssecção
    first_set = []
    result_list = []
    
    for element in expression_elements[operator_index - 1]:
        first_set.append(element)

    for first_set_element in first_set:
        for element in expression_elements[operator_index + 1]:
            if element == first_set_element:
                result_list.append(element) 
                break
    return result_list

def replace_with_result(operator_index, result, expression_elements):  # Trocar operação pelo seu resultado na expressão
    expression_elements.pop(operator_index+1)      
    expression_elements.pop(operator_index-1)     
    expression_elements.pop(operator_index-1) 
    expression_elements.insert(operator_index-1, result)

def remove_repeated(repeated_list):  # Retira elementos iguais
    return list(dict.fromkeys(repeated_list))

def get_union(operator_index, expression_elements):  # Calcula a união
    result_set = []
    for element in expression_elements[operator_index - 1]:
        result_set.append(element)

    for element in expression_elements[operator_index + 1]:
        result_set.append(element)

    return remove_repeated(result_set)

def get_diference(operator_index, expression_elements):  # Calcula a diferença
    first_set = []
    for element in expression_elements[operator_index - 1]:
        first_set.append(element)

    for element in expression_elements[operator_index + 1]:
        for first_set_element in first_set:
            if first_set_element == element:
                first_set.remove(first_set_element)
                break
    return first_set

def show_formatted_set(list):  # Mostra no formato {ABCDE}
    set = '{'
    for element in list:
        set += element
    set += '}'
    print(set)

while True:

    try:
        expression = input()  # Coleta a expressão
    except EOFError:
        break

    no_operators = True  # Não há operadores
    no_parentheses = True  # Não há parenteses

    for term in expression:  # Verifica se há operadores
        
        if term == '+' or  term == '-' or term == '*':
            no_operators = False
            break

    for term in expression:  # Verfica se há operadores
        
        if term == '(' or  term == ')':
            no_parentheses = False
            break

    set_opened = False  # Não abriu um conjunto
    expression_elements = []  # Lista de components da expressão
    
    priority = False

    for term in expression:  # Percorre a expressão

        if term == '(':
            priority = True
            priority_elements = []
            continue

        if term == ')':
            priority = False
            continue
        
        if term == '{':  # Se abriu um conjunto
            set_opened = True
            elements = []
            continue

        if term == '}':  # Se fechou um conjunto
            set_opened = False
            expression_elements.append(elements)
            continue

        if term == '+' or  term == '-' or term == '*':  # Se é um operador
            expression_elements.append(term)
        
        if set_opened:  # Conjunto foi aberto
            elements.append(term)

    if no_operators:   # Se não tem operadores
        show_formatted_set(expression_elements[0])
    elif no_parentheses: # Se tem operadores e nao tem parenteses
        expression_result = calculate_expression(expression_elements) 
        show_formatted_set(expression_result)
    break