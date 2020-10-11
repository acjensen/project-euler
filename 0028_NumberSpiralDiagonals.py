n = 1
skip = 2
corner = 0
squareSize = 1001
ls = []
while skip + 2 < squareSize + 4:
    ls.append(n)
    n += skip
    corner += 1
    if corner == 4:
        skip += 2
        corner = 0

print(sum(ls[:-3]))
