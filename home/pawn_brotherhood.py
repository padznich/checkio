
def safe_pawns(s):

    literals = 'abcdefgh'
    safe = set()

    structured = {}
    for i in s:
        if structured.get(int(i[1])):
            structured[int(i[1])].append(i[0])
        else:
            structured[int(i[1])] = [i[0]]

    order = sorted(structured.keys())

    for step, level in enumerate(order):

        if not step or not level:
            continue

        pre_level = order[step - 1]

        if pre_level != level - 1:
            continue

        for col in structured[level]:
            r_side = literals.index(col) + 1
            l_side = literals.index(col) - 1
            if r_side > 7:
                protector_1 = 'z'
            else:
                protector_1 = literals[r_side]
            if l_side < 0:
                protector_2 = 'z'
            else:
                protector_2 = literals[l_side]

            if protector_1 in structured[level - 1] or protector_2 in structured[level - 1]:
                safe.add('{}{}'.format(col, level))

    return len(safe)


print safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
print safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})
print safe_pawns(["a1","b2","c3","d4","e5","f6","g7","h8"])
print safe_pawns(["a2","b4","c6","d8","e1","f3","g5","h8"])
print safe_pawns(["b6","a7","b8","c7","g1","f2","h2","g3"])
