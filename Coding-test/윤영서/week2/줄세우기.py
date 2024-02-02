import sys
t=int(sys.stdin.readline())
count=0

for k in range(1,t+1):
  data = list(map(int, input().split()))
  count=0
  for i in range(1,len(data)-1):
    for j in range(i+1, len(data)):
      if data[i] > data[j]:
        data[i],data[j] = data[j],data[i]
        count+=1
  print(data[0], count)