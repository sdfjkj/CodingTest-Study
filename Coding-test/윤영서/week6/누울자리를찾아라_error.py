#https://www.acmicpc.net/problem/1652
import sys
input = sys.stdin.readline
N = int(input())
room = []
for i in range(N):
  room.append(input().rstrip())
g_count=0
s_count=0
if N==1:
  print(0,0)
else:
  #가로
  for i in range(N):
    count=0
    for k in range(1,N):
      if room[i][k-1]=="." and room[i][k]=="." :
        count+=1
        # print(i,"번째 줄 : ", count)
    if count>=1:
      g_count+=1


  #세로
  for i in range(N):
    count=0
    for k in range(1,N):
      if room[k-1][i]=="." and room[k][i]=="." :
        count+=1
    if count>=1:
      s_count+=1

  print(g_count, s_count)