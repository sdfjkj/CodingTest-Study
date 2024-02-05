import sys
sys.stdin = open('CodingTest-Study/Coding-test/윤영서/week3/input.txt','r')
input = sys.stdin.readline

for _ in range(4):
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