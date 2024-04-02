# https://www.acmicpc.net/problem/1980
import sys
sys.stdin = open('CodingTest-Study/Coding-test/윤영서/week3/input.txt','r')

input = sys.stdin.readline
n, m, t = map(int, input().split())
coke = 0


def findAnswer() -> int:
    global result
    for i in range(t // n + 1):
        for j in range(t // m + 1):
            if i * n + j * m == t:
                result = max(result, i + j)
    return result

while True:
    result = 0
    findAnswer()
    if not result:
        coke, t = coke + 1, t - 1
    else:
        print(result, coke)
        break