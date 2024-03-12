n, m = map(int, input().split())

nset = set()
mset = set()
res = 0

for _ in range(n):
    nset.add(input())

for _ in range(m):
    mset.add(input())

print(len(nset&mset))