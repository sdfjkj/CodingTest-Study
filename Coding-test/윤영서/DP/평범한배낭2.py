# https://www.acmicpc.net/problem/12920
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
array = [[0]*(M+1) for _ in range(N+1)]
# print(array)
for i in range(1, N+1):
    for j in range(1, M+1):
        if j>=bag[i-1][0]:
            array[i][j] = max(array[i-1][j]+array[i][j])