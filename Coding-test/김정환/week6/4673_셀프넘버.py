def d(n):
    n = n + sum(map(int, str(n)))
    return n


nonself = set()
allset = set()

for i in range(1, 10001):
    nonself.add(d(i))
    allset.add(d(i))

for j in nonself - allset:
    print(j)