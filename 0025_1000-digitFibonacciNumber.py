x = 1
y = 1
f = 0
i = 2
while len(list(str(f))) < 1000:
    f = x + y
    #print f
    x = y
    y = f
    i += 1

print i
