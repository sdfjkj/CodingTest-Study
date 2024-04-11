import sys
input = sys.stdin.readline
g,S_len = map(int, input().split())
W= input().rstrip()
S = input().rstrip()

count=0
for i in range(S_len-g+1):
  if S[i] in W:
    w_test = W.replace(S[i], '0')
    
    for j in range(1,g):
      if S[i+j] in w_test:
        w_test = w_test.replace(S[i+j], '0')
        
        if w_test=='0000':
          count+=1
      
      else:
        w_test=W
        
        
        break
      
  else:
    w_test=W

print(count)


