n = int(input())
nlist = []

for i in range(n):
    a, b = input().split(" ")
    nlist.append([int(a), i, b])

nlist.sort(key = lambda x: (x[0], x[1]))

for n in nlist:
    print(str(n[0]) + ' ' + n[2])