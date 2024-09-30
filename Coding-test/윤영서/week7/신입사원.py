# https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    # print(array)
    count=1
    array.sort(key=lambda x: x[0])
    # k = sorted(array)
    # print(k)
    min = array[0][1]
    for i in range(1,n):
        if array[i][1] < min:
            min = array[i][1]
            count+=1
    print(count)
