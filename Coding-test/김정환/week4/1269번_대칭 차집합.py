n, m = map(int, input().split())
nset = set(input().split())
mset = set(input().split())

print(len(nset^mset))