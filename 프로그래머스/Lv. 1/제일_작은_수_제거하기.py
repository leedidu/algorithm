def solution(arr):
    arr_list = list(arr)
    arr_list.remove(min(arr))
    return arr_list if len(arr_list) > 0 else [-1]