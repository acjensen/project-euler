import primetools as pt
import timeit

def problem():

    primes = pt.getPrimes(1000000)

    def truncate(p: int, from_left=True):
        ''' Repeatedly truncate the number. Return false if any truncated number is not prime. '''
        digits = [c for c in str(p)]
        while len(digits) != 0:
            if int(''.join(digits)) not in primes:
                return False
            else:
                if from_left==True:
                    digits = digits[:-1]
                else:
                    digits = digits[1:]
        return True

    def is_truncatable(p: int):
        ''' Returns whether the prime `p` is truncatable from the left and the right. '''
        return truncate(p, True) and truncate(p, False)

    def get_first_11_truncatable_primes():
        ''' First, generate a bunch of prime numbers. Go through each one in order and determine if it is truncatable until we hit 11. '''
        truncatable_primes = []
        num_truncatable_primes_found = 0
        for p in primes:
            if num_truncatable_primes_found == 11:
                return truncatable_primes
            if is_truncatable(p) and p not in [2, 3, 5, 7]:
                num_truncatable_primes_found += 1 
                truncatable_primes.append(p)
                print(p)
        return []

    print(get_first_11_truncatable_primes())

print(timeit.timeit(problem()))