given = 600851475143

n = given
i = 2
largest_prime = 0
while i < n:
    if n % i == 0:
        n = n/i
        largest_prime = i
    else:
        i = i + 1
    print('largest_prime', largest_prime)
    print('i', i)
    print('n', n)
if n > largest_prime:
    largest_prime = n
print('answer = ', largest_prime)
