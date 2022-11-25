from random import randint

def quick_sort(lst):
    if len(lst) > 1:
        pivot = lst[randint(0, len(lst) - 1)]
        
        left_list = [i for i in lst if i < pivot]
        mid_list = [i for i in lst if i == pivot]
        right_list = [i for i in lst if i > pivot]
        
        return quick_sort(left_list) + mid_list + quick_sort(right_list)
    
    else:
        return lst
    
print(quick_sort([int(i) for i in input('Введите элементы списка через пробел: ').split()]))