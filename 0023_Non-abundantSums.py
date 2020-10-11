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

# 1. Generate a lot of abundant numbers
# 2. Generate all possible pairs of those abundant numbers and their sums, delete duplicates
# 3. Check each integer in range(0,28123) if it is an abundant number sum pair. If not, add to total

def getAbundantNumbers(n):
    abundantNumbers = []
    for i in range(2,n):
        if sumDivisors(i) > i:
            abundantNumbers.append(i)
    return abundantNumbers

def getAbundantNumberPairSums(abundantNumbers):
    sums = []
    pairs = itertools.product(abundantNumbers, repeat=2)
    for p in pairs: sums.append(p[0]+p[1])
    return sorted(list(set(sums)))

abundantNumbers = getAbundantNumbers(28123)
abundantNumberPairSums = getAbundantNumberPairSums(abundantNumbers)
#print abundantNumbers
#print abundantNumberPairSums

total = 0
k = 0
for i in range(0,28123):
    if i != abundantNumberPairSums[k]:
        # cant be made from sum of abundant numbers
        total += i
        print i
    else:
        k += 1
print 'total:', total
print 'i, k:', i, k, len(abundantNumberPairSums)
