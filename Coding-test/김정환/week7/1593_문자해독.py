n, m = map(int, input().split())
n_string = input()
m_string = input()
res = 0

from itertools import permutations

for i in permutations(n_string, n):
    print(''.join(i))