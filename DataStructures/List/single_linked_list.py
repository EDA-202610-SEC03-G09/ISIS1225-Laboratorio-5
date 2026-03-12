from DataStructures.List import list_node as ln
from DataStructures.Utils import error

def new_list():
    new_list={"size" : 0,
              "first" : None,
              "last" : None
              }
    return new_list

def get_element(my_list, pos):
    searchpos=0
    node=my_list["first"]
    while searchpos<pos:
        node=node["next"]
        searchpos+=1
    return node["info"]

def add_last(my_list, element):
    nodo = ln.new_single_node(element)
    if my_list['last'] == None:
        my_list['first'] = nodo 
        my_list['last'] = nodo 
    else:
        my_list['last']['next'] = nodo 
        my_list['last'] = nodo 

    my_list['size'] += 1

    return my_list
    

def size(my_list):
    tamaño=my_list["size"]
    return tamaño

def is_present(my_list, pos,cmp_function):
    size = my_list['size']
    if size > 0:
        keyexist = False
        element = my_list["first"]
        for i in range (0,size):
            if (cmp_function(pos, element["info"]) == 0):
                keyexist = True
                break
            element=element["next"]
        if keyexist:
            return i
    return -1

def add_first(my_list, element):
    new_node = {'info': element, 'next': None}
    if my_list['first'] is None:
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        new_node['next'] = my_list['first']
        my_list['first'] = new_node
    my_list['size'] += 1
    return my_list

def is_empty(newlist):
    if newlist["size"]==0:
        return True
    return False

def first_element(newlist):
    if newlist["size"]==0:
        return -1
    return newlist["first"]["info"]

def last_element(newlist):
    if newlist["size"]==0:
        return -1
    return newlist["last"]["info"]

def remove_first(newlist):
    if newlist['first'] is not None:
        temp=newlist['first']['next']
        node=newlist['first']
        newlist['first']=temp
        newlist['size']-=1
        if (newlist['size']==0):
            newlist['last']=newlist['first']
            return node['info']
        else:
            return None

def remove_last(newlist):
    try:
        if newlist['size']>0:
            if newlist['first']==newlist['last']:
                node=newlist['first']
                newlist['last']=None
                newlist['first']=None
            else:
                temp=newlist['first']
                while temp['next']!=newlist['last']:
                    temp=temp['next']
                node=newlist['last']
                newlist['last']=temp
                newlist['last']['next']=None
            newlist['size'] -= 1
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->remoLast: ')

def insert_element(newlist, element, pos):
    new_node = ln.new_single_node(element)
    if (newlist['size']==0):
        newlist['first']=new_node
        newlist['last']=new_node
    elif ((newlist['size']>0) and (pos==0)):
        new_node['next']=newlist['first']
        newlist['first']=new_node
    else:
        cont=1
        temp=newlist['first']
        while cont<pos:
            temp=temp['next']
            cont+=1
        new_node['next']=temp['next']
        temp['next']=new_node

        if (pos==newlist['size']):
            newlist['last']=new_node
    newlist['size']+=1
    return newlist

def delete_element(newlist, pos):
    if (newlist['size']>0):
        if (pos==0):
            newlist['first']=newlist['first']['next']
            newlist['size']-=1
        elif (pos>1):
            temp=newlist['first']
            searchpos=1
            while searchpos<pos:
                temp=temp['next']
                searchpos+=1
                temp['next']=temp['next']['next']
                if (pos==newlist['size']-1):
                    newlist['last']=temp
                newlist['size']-=1
        return newlist

def change_info(newlist, pos, new_info):
    current=newlist['first']
    cont=0
    while cont<pos:
        current=current['next']
        cont+=1
        current['info']=new_info
    return newlist
    
def exchange(newlist, pos1, pos2):
    if pos1==pos2:
        return newlist
    else:
        element_1 = get_element(newlist, pos1)
        element_2 = get_element(newlist, pos2)
        change_info(newlist, pos1, element_2)
        change_info(newlist, pos2, element_1)

def sub_list(newlist, pos, num_elem):
    i=0
    posicion=0
    info=newlist["first"]
    sublist=new_list()
    if newlist["size"]==0:
        return None
    if pos==0 and num_elem <= newlist["size"]:
        while i != num_elem:
            add_last(sublist, info)
            info = info["next"]
            i += 1 
        return sublist
    elif pos <= newlist["size"] and (pos + num_elem) <= newlist["size"]:
        while posicion != pos:
            info = info["next"]
            posicion += 1 
        while i != num_elem:
            add_last(sublist, info)
            info = info["next"]
            i += 1 
        return sublist
    
def merge_sort(my_list, sort_crit):
    size = size(my_list)
    if size == 1:
        return my_list
    else:
        mitad = size // 2
        leftlist = sub_list(my_list, 1, mitad)
        rightlist = sub_list(my_list, mitad + 1, size - mitad)
        merge_sort(leftlist, sort_crit)
        merge_sort(rightlist, sort_crit)
        merge(my_list, leftlist, rightlist, sort_crit)

def merge(my_list, leftlist, rightlist, sort_crit):
    i=1
    j=1
    k=1
    leftelements = size(leftlist)
    rightelements = size(rightlist)
    while (i <= leftelements) and (j <= rightelements):
        elemi = get_element(leftlist, i)
        elemj = get_element(rightlist, j)
        if sort_crit(elemi, elemj):
            change_info(my_list, k, elemi)
            i += 1
        else: 
            change_info(my_list, k, elemj)
            j += 1
        k += 1
    while i <= leftelements:
        change_info(my_list, k, get_element(leftlist, i))
        i += 1
        k += 1
    while j <= rightelements:
        change_info(my_list, k, get_element(rightlist, j))
        j += 1
        k += 1
    return my_list

def quick_sort(my_list, cmp_function):
    
    if len(my_list) <= 1:
        return my_list
    
    pivot = my_list[len(my_list) // 2]
    left = [x for x in my_list if cmp_function(x, pivot)]
    middle = [x for x in my_list if x == pivot]
    right = [x for x in my_list if not cmp_function(x, pivot) and x != pivot]
    
    return quick_sort(left, cmp_function) + middle + quick_sort(right, cmp_function)