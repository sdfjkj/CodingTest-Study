# https://www.acmicpc.net/problem/2309
import sys
import itertools
input = sys.stdin.readline
arr = [int(input()) for _ in range(9)]
nPr = itertools.combinations(arr,7)
# print(list(nPr))
array = list(nPr)
for i in array:
    if sum(i)==100:
        i = sorted(i)
        for j in i:
            print(j)
        break# break 안하니까 틀림 (왜?? 없는 경우 없다 해두고)=> 조건 만족하는 값이 여러개일수 있으므로!!