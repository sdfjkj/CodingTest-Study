# https://www.acmicpc.net/problem/14719
import sys
input = sys.stdin.readline
H,W = map(int, input().split())
array = list(map(int, input().split()))
gijun = array[0]
temp_array=[]
rain=0
for i in range(W):
    if array[i] <= gijun:
        temp_array.append(array[i])
    else:
        gijun = array[i]
        for k in temp_array:
            rain+=max(temp_array)-k
        temp_array=[]
    if i==W-1:
        if max(temp_array)==array[i]:
            for k in temp_array:
                rain+=max(temp_array)-k
    # print(temp_array)
print(rain)