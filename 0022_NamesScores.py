with open('0022_names.txt') as f:
    content = f.readlines()
content = content[0]
content = content.replace('\"', '')
content = content.split(',')
content = sorted(content)

keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
values = range(1, len(keys)+1)
alphabet = dict(zip(keys, values))
print(alphabet)

total = 0
for i, name in enumerate(content):
    wordScore = 0
    for character in list(name):
        wordScore += alphabet[character]
    total += wordScore*(i+1)

print(total)
