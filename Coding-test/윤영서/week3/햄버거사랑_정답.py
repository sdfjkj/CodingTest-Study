# https://www.acmicpc.net/problem/1980
import sys

input = sys.stdin.readline
n, m, t = map(int, input().split())
coke = 0

def findAnswer() -> list:
    return [i + j for i in range(t // n + 1) for j in range(t // m + 1) if i * n + j * m == t]

while True:
    arr = findAnswer()
    if arr:
        print(max(arr), coke)
        break
    else:
        coke, t = coke + 1, t -1
        arr = findAnswer()