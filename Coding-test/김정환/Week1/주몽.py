from itertools import combinations

n = int(input())
m = int(input())
nlist = list(map(int, input().split()))

res = 0

for com in combinations(nlist, 2):
    if sum(com) == m:
        res += 1

print(res)
asdfkasdjvklasdjv