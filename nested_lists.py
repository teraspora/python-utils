# Work with elements of nested lists
# Author:  John Lynch
# December 7th 2019

def is_nested_in(arr: list, val) -> bool:
    """
    If val is nested in list arr, deeply or shallowly, return True, else return False.
    """
    if val in arr:
        return True
    else:
        for item in arr:
            if type(item) is list and is_nested_in(item, val):
                return True
    return False

def get_depth_nested(arr: list, val) -> int:
    """
    If val is nested in list arr, deeply or shallowly, return the nesting depth as an int; else return 0.
    """
    return len(get_nested_ref(arr, val))

def get_nested_ref(arr: list, val) -> list:
    """
    If val is nested within list arr, return a list of the indices needed to reference it.
    Else return an empty list.
    """
    indices = []
    if val in arr:
        indices.append(arr.index(val))
    elif is_nested_in(arr, val):
        for item in arr:
            if type(item) is not list:
                continue
            if val in item:
                indices.extend([arr.index(item), item.index(val)])
                break
            elif is_nested_in(item, val):
                indices.append(arr.index(item))
                return indices + get_nested_ref(item, val)
    return indices

def get_nested_item_from_indices(arr: list, index_list: list):
    """
    Given a list, and a list of indices, ordered outer to inner,
    retrieve an element from a nested list.
    """
    item = arr
    for index in index_list:
        item = item[index]
    return item

def get_depth_total(arr: list) -> int:
    """
    Return the sum of the nesting depths for all leaf elements in arr
    """
    body_list = get_leaf_elements(arr)
    depth = 0
    for body in body_list:
        curr_depth = get_depth_nested(arr, body)
        depth += curr_depth
        print(f'Body: {body} - Depth: {curr_depth}')
    return depth

def get_leaf_elements(arr: list) -> list:
    """
    Get all leaf elements (strings) nested in list arr, deeply or shallowly.
    """
    leaves = []
    for item in arr:
        if type(item) is not list:
            leaves +=[item]
        else:
            leaves += get_leaf_elements(item)
    return leaves


# Usage

# print(get_nested_ref([1,2,3,4,5], 4))
# [3]
# print(get_nested_ref([1,2,3,[4],5], 4))
# [3, 0]

# a = [1,2,3, 5, [[2,3,8,7,9,[[1,4]]]],[1, [[13, 24, [55,600,928, "fred", [38,39,40,41,42,43,[2,[4]]], 1],5]]]]

# print(is_nested_in(a, [2, [4]]))
# True

# get_nested_ref_ex(a, [2,[4]])
# [5, 1, 0, 2, 4, 6]

# get_nested_item_from_indices(a, [5, 1, 0, 2, 4, 6])
# [2, [4]]

# com =['b',['g',['h']], ['c',['d', ['i'],['e',['j',['k',['l']]],['f']]]]]
# comr = ['b', 'c', 'd', 'i', 'e', 'j', 'k', 'l', 'f', 'g', 'h']
