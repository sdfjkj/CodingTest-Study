# https://www.acmicpc.net/problem/16953
import sys
input = sys.stdin.readline
a,b = map(int,input().split())
r = 1
while(b!=a):
    r+=1
    temp = b
    if b%10 == 1:
        b//=10
    elif b%2 == 0:
        b//=2
    
    if temp == b:
        print(-1)
        break
else:
    print(r)