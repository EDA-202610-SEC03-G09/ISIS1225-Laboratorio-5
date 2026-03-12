def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list['elements'].insert(0, element)
    my_list['size'] += 1    
    return my_list

def add_last(my_list, element):    
    my_list['elements'].append(element)    
    my_list['size'] += 1    
    return my_list

def size(my_list):    
    return my_list["size"]
    
def first_element(my_list):   
    if my_list["size"] == 0:
        raise IndexError("list index out of range")    
    return my_list["elements"][0]

def is_empty(my_list):    
    return my_list["size"] == 0

def last_element(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    return my_list["elements"][my_list["size"] - 1]

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"] = my_list["elements"][:pos] + my_list["elements"][pos+1:]
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    first_element = my_list["elements"][0]
    my_list["elements"] = my_list["elements"][1:]
    my_list["size"] -= 1
    return first_element

def remove_last(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    last_element = my_list["elements"][my_list["size"] - 1]
    my_list["elements"] = my_list["elements"][:-1]
    my_list["size"] -= 1
    return last_element

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list['size']:
        raise IndexError("La posición está fuera de rango")
    my_list['elements'] = my_list['elements'][:pos] + [element] + my_list['elements'][pos:]
    my_list['size'] += 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list['size']:
        raise IndexError("list index out of range")
    my_list['elements'][pos] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    if (pos_1 < 0 or pos_1 >= my_list['size']) or (pos_2 < 0 or pos_2 >= my_list['size']):
        raise IndexError("list index out of range")
    temp = my_list['elements'][pos_1]
    my_list['elements'][pos_1] = my_list['elements'][pos_2]
    my_list['elements'][pos_2] = temp
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list['size']:
        raise IndexError("list index out of range")
    sub_elements = my_list['elements'][pos_i : pos_i + num_elements]
    new_list = {
        "size": len(sub_elements),
        "elements": sub_elements
    }
    
    return new_list


# Implementacion funciones de ordenamiento

def default_sort_criteria(elm_1,elm_2):
    is_sorted = False
    if elm_1 < elm_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_crit):
    ele = my_list["size"]

    for x in range(ele - 1):
        valor = x
        for y in range(x + 1, ele):
            if sort_crit(my_list["elements"][y], my_list["elements"][valor]):
                valor = y

        if valor != x:
            my_list["elements"][x], my_list["elements"][valor] = (my_list["elements"][valor],my_list["elements"][x])

    return my_list
            
def insertion_sort(my_list, sort_crit):
    cantidad = my_list["size"]

    for x in range(1, cantidad):
        valor = my_list["elements"][x]  # elemento actual
        filtro = x - 1

        # Usamos sort_crit para decidir si mover los elementos
        while filtro >= 0 and sort_crit(valor, my_list["elements"][filtro]):
            my_list["elements"][filtro + 1] = my_list["elements"][filtro]
            filtro -= 1

        my_list["elements"][filtro + 1] = valor

    return my_list
        
def shell_sort(my_list, sort_crit):
    cantidad = my_list["size"]
    saltos = 1

    # Secuencia de Knuth
    while saltos < cantidad // 3:
        saltos = 3 * saltos + 1

    while saltos > 0:
        for x in range(saltos, cantidad):
            valor = my_list["elements"][x]
            posicion = x

            # Usamos sort_crit en lugar de comparaciones directas
            while (
                posicion >= saltos
                and sort_crit(valor, my_list["elements"][posicion - saltos])
            ):
                my_list["elements"][posicion] = my_list["elements"][posicion - saltos]
                posicion -= saltos

            my_list["elements"][posicion] = valor

        saltos //= 3

    return my_list

def merge_sort(my_list, sort_crit=True):
    if my_list["size"] > 1: 
        mid = my_list["size"] // 2

        # separar en dos sublistas que también son de tipo dict
        left_half = {
            "elements": my_list["elements"][:mid],
            "size": mid
        }
        right_half = {
            "elements": my_list["elements"][mid:],
            "size": my_list["size"] - mid
        }

        # recursion
        merge_sort(left_half, sort_crit)
        merge_sort(right_half, sort_crit)

        i = j = k = 0
 
        while i < left_half["size"] and j < right_half["size"]:
            if sort_crit:  # ascendente
                condition = left_half["elements"][i] < right_half["elements"][j]
            else:          # descendente
                condition = left_half["elements"][i] > right_half["elements"][j]

            if condition:
                my_list["elements"][k] = left_half["elements"][i]                
                i += 1
            else:
                my_list["elements"][k] = right_half["elements"][j]
                j += 1
            k += 1
     
        while i < left_half["size"]:
            my_list["elements"][k] = left_half["elements"][i]
            i += 1
            k += 1
 
        while j < right_half["size"]:
            my_list["elements"][k] = right_half["elements"][j]
            j += 1
            k += 1

    return my_list


def quick_sort(my_list, sort_crit=True):
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if sort_crit:
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            else:
                if arr[j] > pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    stack = []
    start = 0
    end = my_list["size"] - 1
    stack.append((start, end))

    while stack:
        pos = stack.pop()
        low, high = pos[0], pos[1]
        if low < high:
            pi = partition(my_list["elements"], low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

    return my_list