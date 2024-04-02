#https://www.acmicpc.net/problem/14425 - 시간초과
import sys
imput = sys.stdin.readline
n,m = map(int, input().split())
s=set()
for i in range(n):
  s.append(input())

count=0
for i in range(m):
  k=input()
  if k in s:
    count+=1
print(count)
