dictionary = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}


def getTriangularNumbers(limit):
    triNums = []
    for n in range(1, limit):
        triNums.append(n*(n+1)/2)
    return triNums


def getWordValue(word):
    characters = list(word)
    #print ('characters:', characters)
    total = 0
    for c in characters:
        if c in dictionary:
            total = total + dictionary[c]
    return total


triNums = getTriangularNumbers(10000)
words = []
with open('0042_words.txt') as inputFile:
    for line in inputFile:
        words = line.split(',')
        print('words:', words)

total = 0
for word in words:
    wordValue = getWordValue(word)
    if wordValue in triNums:
        total = total + 1

print(total)
