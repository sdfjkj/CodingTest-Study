import sys
input = sys.stdin.readline
g,S_len = map(int, input().split())
W= input().rstrip()
S = input().rstrip()

dict={}
for token in 'abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
  dict[token] = 0

for i in W:
  dict[i]=1

count = 0
for i in range(S_len-g+1):
  if dict[S[i]]==1:
    for j in range(1,g):
      if dict[S[i+j]]==0:
        break

      if j == g-1:
        count += 1

print(count)


