import itertools

chars = list('0123456789')
ls = list(sorted(itertools.permutations(chars)))
print(''.join(ls[1000000-1]))
