n = int(input())
nlist = []
str_nlist = []
row_count = 0
col_count = 0
for _ in range(n):
    line = input()
    nlist.append(list(line))
    for spline in line.split('X'):
        if '..' in spline:
            row_count += 1

new_list = list(map(list, zip(*nlist)))

for line in new_list:
    for spline in ''.join(line).split('X'):
        if '..' in spline:
            col_count += 1

print(f'{row_count} {col_count}')