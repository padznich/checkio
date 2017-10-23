

def _max(*args, **kwargs):

    try:
        if len(args) == 1:
            args = list(args[0])
            if len(args) == 1:
                return args[0]

        # Compare elements
        if 'key' not in kwargs and len(args) > 1:
            return sorted(args)[-1]

        # Compare iterable
        if 'key' not in kwargs:
            return sorted(args[0])[-1] if len(args[0]) > 0 else None

        # Max in case of key-argument
        if len(args) > 1:
            key_iterable = sorted([kwargs['key'](i) for i in args])[-1]
            return sorted([i for i in args if kwargs['key'](i) == key_iterable])[0]
        if len(args) == 1:
            key_iterable = sorted([kwargs['key'](i) for i in args[0]])[-1]
            return sorted([i for i in args[0] if kwargs['key'](i) == key_iterable])[-1]

    except TypeError:
        return None


def _min(*args, **kwargs):

    try:
        if len(args) == 1:
            args = list(args[0])
            if len(args) == 1:
                return args[0]

        # Compare elements
        if 'key' not in kwargs and len(args) > 1:
            return sorted(args)[0]

        # Compare iterable
        if 'key' not in kwargs:
            return sorted(args[0])[0] if len(args[0]) > 0 else None

        # Min in case of key-argument
        if len(args) > 1:
            key_iterable = sorted([kwargs['key'](i) for i in args])[0]
            return sorted([i for i in args if kwargs['key'](i) == key_iterable])[0]
        if len(args) == 1:
            key_iterable = sorted([kwargs['key'](i) for i in args[0]])[0]
            return sorted([i for i in args[0] if kwargs['key'](i) == key_iterable])[0]

    except TypeError:
        return None


assert _max([1]), 1
assert _max(3, 2), 3
assert _min(3, 2), 2
assert _max([1, 2, 0, 3, 4]), 4
assert _max("hello"), "o"
assert _min("hello"), "e"
assert _max(2.2, 5.6, 5.9, key=int), 5.6
assert _max([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]), [3, 4]
assert _min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]), [9, 0]
assert _max((i for i in [1,2,3])), 3
assert _max(filter(str.isalpha, "@v$e56r5CY{]")), 'v'

print 'OK!'
