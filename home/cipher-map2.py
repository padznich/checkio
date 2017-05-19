
def decrypt(grid, encrypted_pass):

    row_length = len(grid[0]) - 1
    poss = []

    # Get first pattern positions
    for i, row in enumerate(grid):

        for j, char in enumerate(row):

            if char == "X":
                poss.append((i, j))
    # Turn three times
    for _ in range(3):
        turned_poss = []
        for i in poss[-4:]:
            turned_poss.append((i[1], row_length - i[0]))
        turned_poss = sorted(turned_poss)
        poss.extend(turned_poss)
    # Get message
    out = []
    for i in poss:
        out.append(encrypted_pass[i[0]][i[1]])

    return ''.join(out)

print decrypt(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')
)
