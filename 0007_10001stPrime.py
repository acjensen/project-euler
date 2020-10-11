'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
# implement seive of Eratosthenes
n = 10001 # find the 10001st prime number
prime_limit = 150001 # highest prime number to check

integers = [True]*prime_limit # true is prime number

def markPrimes(prime):
    # 3. enumerate the multples of prime p
    i = 2
    while prime*i < prime_limit:
        integers[prime*i] = False
        i = i + 1

def getNextPrime(current_prime):
    # 4. find the next prime j starting at the first multiple of current prime p
    next_prime = current_prime + 1
    while next_prime < prime_limit:
        if integers[next_prime] == True:
            return next_prime
        else:
            next_prime += 1
    return -1

def boolToPrimes():
    primes = []
    for index, isPrime in enumerate(integers):
        if isPrime == True:
            primes.append(index)
    return primes

p = 2
while p < prime_limit:
    markPrimes(p)
    p = getNextPrime(p)
    if p == -1:
        break

primes = boolToPrimes()
print '# of primes generated:', len(primes)
print '10001st prime:', primes[n+1]
