def new_list():
    new_list={"elements":[],
              "size":0}
    return new_list

def add_first(my_list,element):
    my_list["elements"].insert(0,element)
    my_list["size"]+=1
    
def add_last(my_list,element):
    my_list["elements"].append(element)
    my_list["size"]+=1
    
def size(my_list):
    longitud=len(my_list['elements'])
    return longitud

def first_element(my_list):
    primer_elemento=my_list["elements"][0]
    return primer_elemento

def get_element(my_list,pos):
    return my_list["elements"][pos-1]

def is_present(my_list,element,cmp_function):
    size=my_list["size"]
    if size > 0:
        keyexist=False
        for keypos in range (0,size):
            info=my_list["elements"][keypos]
            if (cmp_function(element,info)==0):
                keyexist=True
                break
        if keyexist:
            return keypos
    return -1

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size=my_list["size"]
    if size > 0:
        keyexist=False
        for keypos in range(0,size):
            info=my_list["elements"][keypos]
            if cmp_function(element, info)==0:
                keyexist=True 
                break
        if keyexist:
            return keypos
    return -1

def is_empty(newlist):
    if newlist['size']==0:
        return True
    else:
        return False
    
def remove_first(newlist):
    element = newlist['elements'].pop(0)
    newlist['size'] -= 1
    return element

def remove_last(newlist):
    element = newlist['elements'].pop(newlist['size']-1)
    newlist['size'] -= 1
    return element

def insert_element(newlist, element, pos):
    newlist['elements'].insert(pos-1, element)
    newlist['size']+=1
    return newlist

def delete_element(newlist, pos):
    newlist['elements'].pop(pos-1)
    newlist['size'] -= 1
    return newlist

def change_info(newlist, pos, newinfo):
    newlist['elements'][pos-1] = newinfo
    return newinfo

def exchange(newlist, pos1, pos2):
    infopos1 = get_element(newlist, pos1)
    infopos2 = get_element(newlist, pos2)
    change_info(newlist, pos1, infopos2)
    change_info(newlist, pos2, infopos1)
    return newlist

def sub_list(newlsit, pos, numelem):
    sublist = new_list()
    n = pos + (numelem - 1)
    for i in range(pos, pos + numelem):
        sublist["elements"].append(newlsit["elements"][i])
        sublist["size"] = numelem
        return sublist
    
def merge_sort(my_list, sort_crit):
    size = len(my_list)
    if size <= 1:
        return my_list
    else:
        mitad = size//2
        leftlist = my_list[:mitad]  
        rightlist = my_list[mitad:] 
        leftlist = merge_sort(leftlist, sort_crit)
        rightlist = merge_sort(rightlist, sort_crit)
        return merge(leftlist, rightlist, sort_crit)

def merge(leftlist, rightlist, sort_crit):
    resp=[] 
    i=0 
    j=0 
    while i < len(leftlist) and j < len(rightlist):
        if sort_crit(leftlist[i], rightlist[j]):
            resp.append(leftlist[i])
            i += 1
        else:
            resp.append(rightlist[j]) 
            j += 1
    while i < len(leftlist):
        resp.append(leftlist[i])
        i += 1
    while j < len(rightlist):
        resp.append(rightlist[j])
        j += 1

    return resp


def quick_sort(my_list, cmp_function):
    
    if len(my_list) <= 1:
        return my_list
    
    pivot = my_list[len(my_list) // 2]
    left = [x for x in my_list if cmp_function(x, pivot)]
    middle = [x for x in my_list if x == pivot]
    right = [x for x in my_list if not cmp_function(x, pivot) and x != pivot]
    
    return quick_sort(left, cmp_function) + middle + quick_sort(right, cmp_function)

