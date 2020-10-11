'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

n = 100

sum_of_squares = n*(n+1)*(2*n+1)/6

total = 0
for x in range(1, n+1):
     total = total + x

square_of_sum = total*total

print sum_of_squares
print square_of_sum
print "answer =", square_of_sum - sum_of_squares
