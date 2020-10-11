def getSum():
    sum = 0
    i = 0
    while i < len(values):
        sum = sum + values[i]*counts[i]
        i = i + 1
    return sum


total = 0
values = [5, 2, 1]
counts = [0, 0, 0]
sum_to = 10

for i, value in enumerate(values):
    counts = [0, 0, 0]
    # calculate starting count
    starting_count = int(sum_to/value)
    counts[i] = starting_count
    # get remainder
    remainder = sum_to - getSum()
    if remainder == 0:
        total = total + 1
        counts[i] = counts[i] - 1
    for j in range(1, len(values)-1-i):
        values[i + j] = int(remainder/values[i + j])


'''
coinValue = [10, 5, 2, 1]

n = 10

def getSum():
    sum = 0
    i = 0
    while i < 7:
        sum = sum + coinValue[i]*coinCount[i]
        i = i + 1
    return sum

def isCorrectChange():
    if getSum() == 200:
        return True
    else:
         False

totalWays = 0

coinCount = [0, 0, 0, 0]
remainder = n
i = 0
j = 0
while i < len(coinValue):
    while i + j < len(coinValue):
        remainder = 10 - getSum()
        # get the maximum beginning coin count
        coinCount[i + j] = int(remainder/value)
        # calculate the remainder
        remainder = n%value
        if remainder == 0:
            totalWays = totalWays + 1
            coinCount[i] = coinCount[i] - 1
            j = j + 1
        else:
            j = j + 1
        print (coinCount)
    i = i + 1





print (count + 1)

'''
