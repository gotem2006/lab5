# Шаг 1
def return_list(lst):
    return lst[::-1]
# Шаг 2
def modify_list(lst,func):
    return [func(item) for item in lst]
# Шаг 3
def VS_lists(*lists):
    return all(l == lists[0] for l in lists)
# Шаг 4
def slice_list(lst, start=None, stop=None, step=1):
    return lst[start:stop:step]
# Шаг 5
def create_list(*args):
    return list[args]
# Шаг 6
def insert_element(lst, index, value):
    lst.insert(index, value)
    return lst
# Шаг 7
def merge_and_sort(*lists, reverse=False, key=None):
    merged_list = []
    for lst in lists:
        merged_list.extend(lst)
    sorted_list = sorted(merged_list, reverse=reverse, key=key)
    return sorted_list
# Шаг 8
def handle_odd_length_list():
    import random
    lst = [random.randint(1, 100) for _ in range(random.randint(1, 20))]
    while len(lst) % 2 == 0:
        lst = [random.randint(1, 100) for _ in range(random.randint(1, 20))]
    central_value = lst[len(lst) // 2]
    return lst.count(central_value)
# Шаг 9
def extend_list_with_threshold(main_list, *other_lists, threshold):
    main_list.extend(sum(other_lists, []))
    return main_list[:threshold]

# Шаг 10 
def sort_by_length(lst):
    return sorted(lst, key=len)

def sort_alphabetically(lst):
    return sorted(lst)

def sort_reverse(lst):
    return sorted(lst, reverse=True)

def map_sort_by_length(lst):
    return list(map(len, lst))

def map_sort_to_upper(lst):
    return list(map(str.upper, lst))

def map_sort_to_lower(lst):
    return list(map(str.lower, lst))

# Шаг 11
def pop_min_element(lst):
    min_elem = min(lst)
    lst.remove(min_elem)
    return min_elem

# Шаг 12.1
def find_common_elements(*tuples):
    
    if len(tuples) < 2:
        raise ValueError("Для поиска общих элементов нужно минимум два кортежа.")
    
    # Используем пересечение множеств для нахождения общих элементов
    common_elements = set(tuples[0])
    for tpl in tuples[1:]:
        common_elements &= set(tpl)
    
    return tuple(common_elements)
# Шаг 12.2
def find_min_max(*tuples):
   
    # Объединяем все элементы всех кортежей в один список
    all_elements = [item for tpl in tuples for item in tpl]
    
    # Если список пуст, возвращаем None для min и max
    if not all_elements:
        return None, None
    
    # Находим минимальный и максимальный элементы
    return min(all_elements), max(all_elements)

# Шаг 13
def tuple_types(tpl):
    return tuple(type(item) for item in tpl)
# Шаг 14
def element_in_tuple(tpl, element):
    return element in tpl
# Шаг 15
def create_2d_list(*lists, chunk_size=None):
    """
    Формирует двумерный список на основе переданных списков.
    Элементы объединяются в строки заданной длины (chunk_size) или
    каждый переданный список становится строкой двумерного списка.
    
    :param lists: один или несколько списков
    :param chunk_size: размер строки двумерного списка (если None, каждый список — строка)
    :return: двумерный список
    """
    # Если chunk_size задан, разбиваем списки на части указанного размера
    if chunk_size:
        result = []
        for lst in lists:
            for i in range(0, len(lst), chunk_size):
                result.append(lst[i:i + chunk_size])
        return result
    
# Шаг 16.1
def dict_keys_to_upper(d):
    """Возвращает словарь с ключами в верхнем регистре."""
    return {k.upper(): v for k, v in d.items()}

# Шаг 16.2
def dict_values_sum(d):
    """Суммирует все числовые значения словаря."""
    return sum(v for v in d.values() if isinstance(v, (int, float)))

# Шаг 16.3
def filter_dict_by_value(d, threshold):
    """Возвращает элементы словаря, значения которых выше порога."""
    return {k: v for k, v in d.items() if v > threshold}

# Шаг 17
def count_key_occurrences(key, *dicts):
    """Считает, сколько раз ключ встречается в словарях."""
    return sum(1 for d in dicts if key in d)

# Шаг 18
def deep_find(dictionary, key_chain):
    """Ищет элемент в сложном словаре по цепочке ключей."""
    current = dictionary
    for key in key_chain:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current
