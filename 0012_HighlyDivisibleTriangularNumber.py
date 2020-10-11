import collections


def getTriNum(n):
    return n*(n+1)/2


def getPrimeFactors(n):
    primes = []
    i = 2
    while i <= n:
        if n % i == 0:
            n = n/i
            primes.append(i)
        else:
            i = i + 1
    return primes


def getPrimeDuplicity(prime_factors):
    counter = collections.Counter(prime_factors)
    return counter.values()


def countPrimeFactors(primeDuplicity):
    powers = [x + 1 for x in primeDuplicity]
    product = 1
    for x in powers:
        product = x*product
    return product


n_factors_max = 0
for i in range(0, 100000):
    n_factors = countPrimeFactors(
        getPrimeDuplicity(getPrimeFactors(getTriNum(i))))
    if n_factors > 500:
        print(i, ' ', getTriNum(i), ' ', n_factors)
        break
