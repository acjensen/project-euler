#note that it is forty not fourty

intWords = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

def intToWords(n):
    digits = [int(i) for i in str(n)]
    if len(digits) == 4:
        return 'onethousand'
    if len(digits) == 3:
        str_hundred = 'hundredand'
        if digits[2] == 0 and digits[1] == 0:
            str_hundred = 'hundred'
        if digits[1] == 1:
            return intWords.get(digits[0]) + str_hundred + intWords.get(digits[1]*10+digits[2])
        else:
            return intWords.get(digits[0]) + str_hundred + intWords.get(digits[1]*10) + intWords.get(digits[2])
    if len(digits) == 2:
        if digits[0] == 1:
            return intWords.get(digits[0]*10+digits[1])
        else:
            return intWords.get(digits[0]*10) + intWords.get(digits[1])
    if len(digits) == 1:
        return intWords.get(digits[0])

total = 0
for n in range(1,1001):
    words = intToWords(n)
    print n, words
    total = total + len(words)
print 'total:', total
