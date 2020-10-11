# Fermat's little theorem
# 1/d has an n digit cycle
# where n is the smallest n such that (10^n) mod (d) = 1 for prime d

import primetools

eMax = 0
dMax = 0

primes = primetools.getPrimes(1001)
for d in primes[3:1001]:
    e = 1
    while e < 20000:
        e += 1
        if (10**e) % d == 1:
            break
    if e > eMax:
        eMax = e
        dMax = d

print(dMax)
