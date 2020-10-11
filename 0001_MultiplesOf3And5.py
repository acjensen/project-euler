# Multiples of 3 and 5
# Andrew Charles Jensen

n = 1000
i = 0
total = 0
while i < n:
    if i % 3 == 0 or i % 5 == 0:
        total = total + i
    i = i + 1
print("total = ", total)
