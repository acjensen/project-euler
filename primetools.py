# generates list containing prime numbers less than n
# implements a seive of Eratosthenes

# todo: consolodate functions used by getPrimes
def getPrimes(prime_limit):
    integers = [True]*prime_limit
    p = 2
    while p < prime_limit:
        markPrimes(p, integers, prime_limit)
        p = getNextPrime(p, integers, prime_limit)
        if p == -1:
            break
    primes = boolToPrimes(integers)
    return primes[2:]


def markPrimes(prime, integers, prime_limit):
    # 3. enumerate the multples of prime p
    i = 2
    while prime*i < prime_limit:
        integers[prime*i] = False
        i = i + 1


def getNextPrime(current_prime, integers, prime_limit):
    # 4. find the next prime j starting at the first multiple of current prime p
    next_prime = current_prime + 1
    while next_prime < prime_limit:
        if integers[next_prime] == True:
            return next_prime
        else:
            next_prime += 1
    return -1


def boolToPrimes(integers):
    primes = []
    for index, isPrime in enumerate(integers):
        if isPrime == True:
            primes.append(index)
    return primes
