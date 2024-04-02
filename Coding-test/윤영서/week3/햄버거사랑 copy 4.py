# 1980 햄버거 사랑
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m, t = map(int, input().split())
coke = 0

while True:
    arr = [
        i + j
        for i in range(t // n + 1)
        for j in range(t // m + 1)
        if i * n + j * m == t 
    ]
    if arr:
        print(max(arr), coke)
        break
    else:
        coke, t = coke + 1, t - 1