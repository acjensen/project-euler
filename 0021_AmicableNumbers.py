import collections
import itertools

def getPrimeFactors(n):
    primes = []
    i = 2
    while i <= n:
        #print n, 'divided by', i
        if n%i == 0:
            n = n/i
            primes.append(i)
        else:
            i = i + 1
    primes.append(1)
    return primes

def getDivisors(prime_factors):
    divisors = []
    for x in range(1,len(prime_factors)-1):
        combos = list(itertools.combinations(prime_factors, x))
        for combo in combos:
            product = 1
            for y in combo:
                product = product*y
            divisors.append(product)
    return set(divisors)

def sumDivisors(n):
    prime_factors = getPrimeFactors(n)
    divisors = getDivisors(prime_factors)
    #print 'prime factors:', prime_factors
    #print 'divisors:', list(divisors)
    total = 0
    for x in divisors:
        total = total + x
    return total

amicable = []
for n in range(1,10001):
    total = sumDivisors(n)
    if n == sumDivisors(total) and n != total:
        amicable.append(n)

total = 0
for x in list(set(amicable)):
    total = total + x
print amicable
print total
