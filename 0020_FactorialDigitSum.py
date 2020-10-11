n = 100
factorial = 1
for x in range(1,n):
    factorial = x*factorial
digits = [int(x) for x in list(str(factorial))]
total = 0
for x in digits:
    total = total + x
print total
