product_max = 0

for i in reversed(range(100, 1000)):
    for j in reversed(range(100, 1000)):
        product = i*j
        string1 = str(product)
        string2 = string1[::-1]
        if string1 == string2:
            print(string1)
            print(string2)
            if product > product_max:
                product_max = product

print('answer = ', product_max)
