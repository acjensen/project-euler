# found thes solution using the last number here... https://oeis.org/A006877,
# to improve, I would store the sequence length for each number and use that if the program ever encountered it again

def func(n):
    if n & 1 == 0:
        n = n/2
    else:
        n = 3*n + 1
    return n


i_max = 0
for n in range(150, 200):
    i = 0
    while n != 1:
        n = func(n)
        i = i + 1
    if i > i_max:
        i_max = i

print(i_max)
