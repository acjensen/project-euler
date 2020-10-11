def isPalindrome(ls):
    if ls == list(reversed(ls)):
        return True
    else:
        return False

total = 0
for n in range(1,1000001):
    n10 =  list(str(n))
    n2 = list(str(bin(n)))[2:]
    if isPalindrome(n10) and isPalindrome(n2):
        total = total + n

print total
