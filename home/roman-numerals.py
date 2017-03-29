

def translate_to_roman(_n):
    """
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000

    Tested:
    print translate_to_roman(6) == 'VI'
    print translate_to_roman(76) == 'LXXVI'
    print translate_to_roman(13) == 'XIII'
    print translate_to_roman(44) == 'XLIV'
    print translate_to_roman(3999) == 'MMMCMXCIX'
    """
    tr = {
        0: ["I", "V"],
        1: ["X", "L"],
        2: ["C", "D"],
        3: ["M"],
    }

    _n_str = str(_n)[::-1]
    out = []
    for i, j in enumerate(_n_str):
        out.append([])
        _j = int(j)
        if _j < 4:
            out[i].extend(tr[i][0] * _j)
        elif _j == 4:
            out[i].extend(tr[i][0] + tr[i][1])
        elif _j == 5:
            out[i].append(tr[i][1])
        elif _j < 9:
            out[i].extend(tr[i][1] + tr[i][0] * (_j - 5))
        elif _j == 9:
            out[i].extend(tr[i][0] + tr[i + 1][0])
        else:
            "0"

    return "".join(["".join(i) for i in out[::-1]])
