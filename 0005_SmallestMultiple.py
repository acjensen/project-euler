'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
max_divisor = 20
number_limit = 1000000000

def isDivisible(number, max_divisor):
    for x in range(2,max_divisor):
        if number%x != 0:
            return False
    return True

number = max_divisor
while number < number_limit:
    if isDivisible(number, max_divisor) == True:
        print "highest number is", number
        break
    else:
        number = number + max_divisor
