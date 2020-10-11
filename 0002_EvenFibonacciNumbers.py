f = 0
f1 = 1
f2 = 2
total = 2

while f < 4000000:
    f = f1 + f2
    if f % 2 == 0:
        total = total + f
    f1 = f2
    f2 = f
    print(f)

print(total)
