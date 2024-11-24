# main.py
from module import *

def test_all_functions():
    """Вызывает и тестирует все функции из functions.py."""
    print("Шаг 1: return_list ->", return_list([1, 2, 3, 4]))
    print("Шаг 2: modify_list ->", modify_list([1, 2, 3], lambda x: x ** 2))
    print("Шаг 3: VS_lists ->", VS_lists([1, 2], [1, 2], [1, 2]))
    print("Шаг 4: slice_list ->", slice_list([1, 2, 3, 4, 5], 1, 4, 2))
    print("Шаг 5: create_list ->", create_list(1, 2, 3))
    print("Шаг 6: insert_element ->", insert_element([1, 2, 4], 2, 3))
    print("Шаг 7: merge_and_sort ->", merge_and_sort([3, 1], [4, 2]))
    print("Шаг 8: handle_odd_length_list ->", handle_odd_length_list())
    print("Шаг 9: extend_list_with_threshold ->", extend_list_with_threshold([1], [2, 3, 4], threshold=3))
    print("Шаг 10: sort_by_length ->", sort_by_length(["apple", "pear", "banana"]))
    print("Шаг 11: pop_min_element ->", pop_min_element([3, 1, 2]))
    print("Шаг 12: find_common_elements ->", find_common_elements((1, 2), (2, 3)))
    print("Шаг 13: tuple_types ->", tuple_types((1, "string", 3.14)))
    print("Шаг 14: element_in_tuple ->", element_in_tuple((1, 2, 3), 2))
    print("Шаг 15: create_2d_list ->", create_2d_list([1, 2, 3, 4], chunk_size=2))
    print("Шаг 16: dict_keys_to_upper ->", dict_keys_to_upper({"a": 1, "b": 2}))
    print("Шаг 17: count_key_occurrences ->", count_key_occurrences("key", {"key": 1}, {"key": 2}, {"not_key": 3}))
    print("Шаг 18: deep_find ->", deep_find({"a": {"b": {"c": 42}}}, ["a", "b", "c"]))

if __name__ == "__main__":
    test_all_functions()
