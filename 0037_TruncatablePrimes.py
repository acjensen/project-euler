import primetools as pt

digits = str(list(range(1,10)))
print(digits)
prime_digits = [2, 3, 5, 7]

primes = pt.getPrimes(1000000)

def truncate(from_left=True):
    while len(digits) != 0:
        if int(''.join(digits)) not in primes:
            return False
        else:
            if from_left=True:
                digits = digits[:-1]
            else:
                digits = digits[1:]

def is_truncatable(p):
    digits = [c for c in str(p)]
    even = True
    digits2 = digits.copy()
    while len(digits) != 0:
        digits_as_num = int(''.join(digits))
        if digits_as_num not in primes:
            return False
        if even:
            digits = digits[:-1]
        else:
            digits = digits[1:]
        if len(digits) == 1:
            if int(digits[0]) not in prime_digits:
                return False
    even = False
    while len(digits2) != 0:
        digits_as_num = int(''.join(digits2))
        if digits_as_num not in primes:
            return False
        if even:
            digits2 = digits2[:-1]
        else:
            digits2 = digits2[1:]
        if len(digits2) == 1:
            if int(digits2[0]) not in prime_digits:
                return False
    return True

# for p in primes:
#     if is_truncatable(p) and p not in prime_digits:
#         print(p)

# The solution.
print(sum(
    [
     23 ,  
37    ,
53    ,
73    ,
313   ,
317   ,
373   ,
797   ,
3137  ,
3797  ,
739397,
    ]
))

print(is_truncatable(3797))
print(is_truncatable(739397))
