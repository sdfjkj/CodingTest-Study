# https://www.acmicpc.net/problem/1149 - 통과
#메모리 : 109240 KB / 시간 : 112ms
import sys
input = sys.stdin.readline
n = int(input())

nlist = list(map(int, input().split()))

for _ in range(n-1):
    newlist = list(map(int, input().split()))

    newlist[0] += min(nlist[1], nlist[2])
    newlist[1] += min(nlist[2], nlist[0])
    newlist[2] += min(nlist[0], nlist[1])

    nlist = newlist

print(min(nlist))