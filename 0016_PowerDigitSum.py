n = 2**1000
digits = [int(i) for i in str(n)]
total = 0
for i in digits:
    total = total + i
print(total)
