import math


def isPrime(n):
    if n < 0:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


nMax = 0
a_ = range(-999, 999)
b_ = range(-1000, 1000)

for a in a_:
    for b in b_:
        n = 0
        while isPrime(n**2 + a*n + b):
            n += 1
        if n > nMax:
            nMax = n
            ans_a = a
            ans_b = b
        #print (a,b,n)

print(ans_a*ans_b)
