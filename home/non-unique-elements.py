

def clear_unique(_list):
    """
    Tested
    print clear_unique([1, 2, 3, 1, 3])
    print clear_unique([1, 2, 3, 4, 5])
    print clear_unique([5, 5, 5, 5, 5])
    print clear_unique([10, 9, 10, 10, 9, 8])
    """

    _list_unique = set(_list)

    for i in _list_unique:

        if _list.count(i) == 1:
            _list.pop(_list.index(i))

    return _list
