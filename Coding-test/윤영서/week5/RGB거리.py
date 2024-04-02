# https://www.acmicpc.net/problem/1149 - 통과
#메모리 : 109240 KB / 시간 : 112ms
import sys
input = sys.stdin.readline
n = int(input())
a = [0]* n
for i in range(n):
  a[i] = list(map(int, input().split()))

for i in range(1,n):
  a[i][0] = min(a[i-1][1],a[i-1][2])+ a[i][0]
  a[i][1] = min(a[i-1][0],a[i-1][2])+ a[i][1]
  a[i][2] = min(a[i-1][1],a[i-1][0])+ a[i][2]
print(min(a[n-1][0],a[n-1][1], a[n-1][2] ))