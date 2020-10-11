triangle = []
with open('0018_triangle.txt') as input_file:
    for line in input_file:
        line = line.strip().split(' ')
        line = [int(x) for x in line]
        triangle.append(line)

triangle = list(reversed(triangle))
connectors = list(triangle)

for row_i, this_row in enumerate(triangle):
    if row_i < len(triangle) - 1:
        next_row = list(triangle[row_i + 1])
        for num_j, this_num  in enumerate(this_row):
            if num_j < len(this_row) - 1:
                next_num = this_row[num_j + 1]
                if this_num > next_num:
                    larger = this_num
                    connectors[row_i + 1][num_j] = '//'
                else:
                    larger = next_num
                    connectors[row_i + 1][num_j] = '\\'
                next_row[num_j] = next_row[num_j] + larger
                triangle[row_i + 1] = next_row

for i, row in enumerate(reversed(triangle)):
    print i, row
    print i, connectors[len(connectors)-i-1]

print 'answer:', triangle[len(triangle)-1]
