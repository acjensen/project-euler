'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
# implement seive of Eratosthenes
prime_limit = 2000000 # highest prime number to sum
total = 2
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
    #print p
    total = total + p

primes = boolToPrimes()
print 'sum of primes up to ', prime_limit, 'primes is ', total
