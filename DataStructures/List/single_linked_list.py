def new_list():
    newlist = {
        "first" : None,
        "last" : None,
        "size" : 0,
    }
    
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos +=1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count +=1
    
    if not is_in_array:
        count = -1
    return count
    
def add_first(my_list, element):
    nuevo = {
        "info": element,
        "next": my_list["first"]
    }
    
    if my_list["size"] == 0:
        my_list["first"] = nuevo
        my_list["last"] = nuevo
    else:
        my_list["first"] = nuevo
        
    my_list["size"] += 1
    
    return my_list

def add_last(my_list, element):
    nuevo = {
        "info": element,
        "next": None
    }
    
    if my_list["size"] == 0:
        my_list["first"] = nuevo
        my_list["last"] = nuevo
    else:
        my_list["last"]["next"] = nuevo
        my_list["last"] = nuevo
    
    my_list["size"] +=1
    
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] == 0:
        return None
    
    return my_list["first"]["info"]

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False

def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]["info"]
    
def remove_first(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    e_nodo = my_list["first"]["info"]
    
    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
        
    
    if my_list["size"] > 1:
        my_list["first"] = my_list["first"]["next"]
        
    my_list["size"] -=1
    
    return e_nodo
    
def remove_last(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    e_nodo = my_list["last"]["info"]
    
    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        nodo = my_list["first"]
        while nodo["next"] != my_list["last"]: #busca la referencia que apunte al ultimo nodo
            nodo = nodo["next"]
        nodo["next"] = None  # el penultimo se vuelve el nuevo ultimo
        my_list["last"] = nodo # y lo mencionamos en el diccionario
    
    my_list["size"] -=1
    
    return e_nodo

def insert_element(my_list,element,pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    n_n = {"info":element,"next":None}

    if pos == 0:
        return add_first(my_list,element)
    
    elif pos == (my_list["size"] - 1):
        return add_last(my_list,element)
    
    else:
        buscador = my_list["first"]
        i = 0
        
        while i < pos - 1:
            buscador = buscador["next"]
            i +=1
        
        n_n["next"] = buscador["next"]
        buscador["next"] = n_n
        
        my_list["size"] +=1
    
    return my_list
        
def delete_element(my_list,pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    if pos == 0:
        my_list["first"]["info"] == None
    
    elif pos == my_list["size"] - 1:
        my_list["last"]["info"] = None
    
    else:
        buscador = my_list[next]
        i = 0
        while i < pos :
            buscador = buscador["next"]
            i +=1
            
        buscador["info"] = None
    
    return my_list
    
def change_info(my_list,pos, new_info):
    
    if pos < 0 or pos >= my_list["size"]:
        return None
    
    
    i = 0
    buscador = my_list["first"]
        
    while i < pos:
        buscador = buscador["next"]
        i +=1
            
    buscador["info"] = new_info
    return my_list

def exchange(my_list,pos_1,pos_2):
    
    if pos_1 < 0 or pos_1 >= my_list["size"]:
        return None
    if pos_2 < 0 or pos_2 >= my_list["size"]:
        return None
    
    buscador_1 = my_list["first"]
    i_1 = 0
    while i_1 < pos_1:
        buscador_1 = buscador_1["next"]
        i_1 +=1
    info_a = buscador_1["info"]
        
        
        
    buscador_2 = my_list["first"]
    i_2 = 0
    while i_2 < pos_2:
        buscador_2 = buscador_2["next"]
        i_2 +=1
    
    buscador_1["info"] = buscador_2["info"]
    buscador_2["info"] = info_a
    
    return my_list

def sub_list(my_list,pos_i,num_elements):
    
    if pos_i < 0 or pos_i >= my_list["size"]:
        return None
    
    buscador = my_list["first"]
    i = 0
    
    while i < pos_i:
        buscador = buscador["next"]
        i +=1
    
    if pos_i + num_elements > my_list["size"]:
        return None
    
    sub = new_list()
    
    for i in range(num_elements):
        insert_element(sub,buscador["info"],i)
        buscador = buscador["next"]
    
    return sub

# implementacion funciones de ordenamiento 

def default_sort_criteria(info_elm1,info_elm2):
    is_sorted = False
    if info_elm1 < info_elm2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_crit):
    if my_list is None or my_list["size"] <= 1:
        return my_list

    buscador_a = my_list["first"]

    while buscador_a is not None:
        min_max = buscador_a
        buscador_b = buscador_a["next"]

        while buscador_b is not None:
            # usamos sort_crit para decidir si se actualiza
            if sort_crit(buscador_b["info"], min_max["info"]):
                min_max = buscador_b
            buscador_b = buscador_b["next"]
            
        buscador_a["info"], min_max["info"] = min_max["info"], buscador_a["info"]
        
        
        buscador_a = buscador_a["next"]
    
    return my_list
            
def insertion_sort(my_list,sort_crit):
    
    
    if my_list["first"] is None or my_list["first"]["next"] is None:
        return  my_list # Lista vacía o de un solo elemento
    
    
    ordenada = None
    buscador = my_list["first"]
    #hola
    
    while buscador is not None: # Recorremos todos los nodos de la lista
        
        buscador_b = buscador["next"]
        
        if ordenada is None or sort_crit(buscador["info"], ordenada["info"]):
            # Insertar al inicio
            buscador["next"] = ordenada
            ordenada = buscador
        else:
            # Buscar posición correcta
            temp = ordenada
            while temp["next"] is not None and not sort_crit(buscador["info"], temp["next"]["info"]):
                temp = temp["next"]

            buscador["next"] = temp["next"]
            temp["next"] = buscador
          
                
        buscador = buscador_b #siguiente variable

    my_list["first"] = ordenada
    return my_list
        

def shell_sort(my_list, sort_crit):
    """
    Ordena una lista enlazada simple usando el algoritmo Shell Sort.

    Parameters:
    my_list (dict): Lista enlazada simple.
    sort_crit (function): Función de comparación.

    Returns:
    dict: Lista ordenada.
    """
    n = my_list["size"]
    if n <= 1:
        return my_list

    nodes = []
    current = my_list["first"]
    while current:
        nodes.append(current)
        current = current["next"]

    # shell sort en array
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp_info = nodes[i]["info"]
            j = i
            while j >= gap and sort_crit(temp_info, nodes[j - gap]["info"]):
                nodes[j]["info"] = nodes[j - gap]["info"]
                j -= gap
            nodes[j]["info"] = temp_info
        gap //= 2

    return my_list

def merge_sort(my_list, sort_crit=default_sort_criteria):
#Listo Ambos 
    if my_list["size"] <= 1:
        return my_list

    mid = my_list["size"] // 2
    left = new_list()
    right = new_list()
    current = my_list["first"]
    idx = 0
    while current:
        if idx < mid:
            add_last(left, current["info"])
        else:
            add_last(right, current["info"])
        current = current["next"]
        idx += 1

    left = merge_sort(left, sort_crit)
    right = merge_sort(right, sort_crit)

    result = new_list()
    lnode = left["first"]
    rnode = right["first"]
    while lnode and rnode:
        if sort_crit(lnode["info"], rnode["info"]):
            add_last(result, lnode["info"])
            lnode = lnode["next"]
        else:
            add_last(result, rnode["info"])
            rnode = rnode["next"]
    while lnode:
        add_last(result, lnode["info"])
        lnode = lnode["next"]
    while rnode:
        add_last(result, rnode["info"])
        rnode = rnode["next"]

    my_list["first"] = result["first"]
    my_list["last"] = result["last"]
    my_list["size"] = result["size"]

    return my_list

def quick_sort(my_list, sort_crit=default_sort_criteria):
 
    if my_list["size"] <= 1:
        return my_list

  
    pivot = my_list["first"]["info"]

    left = new_list()
    right = new_list()
    current = my_list["first"]["next"]

    while current:
        if sort_crit(current["info"], pivot):
            add_last(left, current["info"])
        else:
            add_last(right, current["info"])
        current = current["next"]

    left = quick_sort(left, sort_crit)
    right = quick_sort(right, sort_crit)

 
    result = new_list()
    lnode = left["first"]
    while lnode:
        add_last(result, lnode["info"])
        lnode = lnode["next"]

    add_last(result, pivot)

    rnode = right["first"]
    while rnode:
        add_last(result, rnode["info"])
        rnode = rnode["next"]

    my_list["first"] = result["first"]
    my_list["last"] = result["last"]
    my_list["size"] = result["size"]

    return my_list