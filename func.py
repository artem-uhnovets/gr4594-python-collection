"""
import sys
sys.path.append('C:/Users/uhnov/OneDrive/Рабочий стол/УЧЕБА GB/PYTHON/Collection')
import func as f
"""

def input_number(text) -> int:
    print(text, end='')
    while True:
        try:
            number = int(input())
        except ValueError:
            print('Pls input a number (int): ', end='')
            continue
        else:
            break
    return number

def gener_list_rnd_randint(begin_num, end_num, len_list):
    import random
    return [random.randint(begin_num, end_num) for _ in range(len_list)]

def gener_list_input_int_only(text):
    length = input_number(text)
    return [value := input_number(f'{_ + 1} value is: ') for _ in range(length)]

def gener_list_rnd_randiant_unique(begin_num, end_num, len_list):
    import random
    list = gener_list_rnd_randint(begin_num, end_num, len_list)
    for i in range(1, len(list)):
        while list[i] in list[:i]:
            list[i] = random.randint(begin_num, end_num)
    return list

def list_copy(source_list):
    return [value for value in source_list]

# функция, которая принимает два списка 
# возвращает True, если у них есть хотя бы один общий член.
def equal_value_list(list_1, list_2):
    count = 0
    for value in list_2:
        if value in list_1:
            count += 1
    return True if count > 0 else False

def equal_value_list_t_set(list_1, list_2):
    return False if not set(list_1).intersection(set(list_2)) else True

# функция, чтобы перемешать (в случайном порядке) и распечатать указанный список.
def mashup_list(source_list):
    import random
    l_index = [i for i in range(len(source_list))]
    l_result = []
    rnd_num = random.randint(0, len(source_list))
    for i in range(len(source_list)):
        while rnd_num not in l_index:
            rnd_num = random.randint(0, len(source_list))
        l_result.append(source_list[rnd_num])
        l_index.remove(rnd_num)
    return l_result

# быстрая сортировка списка
def sort_quick_list(array):
    if len(array) < 2:
        return array
    else:
        start_value = array[0]
        less = [i for i in array[1:] if i <= start_value]
        greater = [i for i in array[1:] if i > start_value]
    return sort_quick_list(less) + [start_value] + sort_quick_list(greater)
# через лямбда
def sort_quick_list_lambda(array):
    if len(array) < 2:
        return array
    else:
        start_val = array[0]
        less = list(filter(lambda x: x <= start_val, array[1:]))
        greater = list(filter(lambda x: x > start_val, array[1:]))
    return sort_quick_list(less) + [start_val] + sort_quick_list(greater)
