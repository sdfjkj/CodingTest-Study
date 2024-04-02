# https://www.acmicpc.net/problem/1980
import sys
input = sys.stdin.readline
n,m,t = map(int, input().split())
coke=0

# if n>m:
#     n=m
#     m=n
# ka = int(t/m+1)
# kb = int(t/n+1)
# print(ka,kb)
def findAnswer(n,m,t):
    for i in range(t//m+1):
        for j in range(t//n+1):
            if n*j + m*i == t:
                array.append(i+j)
    return array

while True:
    array=[]
    findAnswer(n,m,t)
    if array!=[]:
        print(max(array), coke)
        break
    else:
        t-=1
        coke+=1
