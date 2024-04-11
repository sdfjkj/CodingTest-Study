import sys

input = sys.stdin.readline
g,S_len = map(int, input().split()) # 4 11
W= input().rstrip() # cAda
S = input().rstrip() # AbrAcadAbRa

wl=[0]*52
sl=[0]*52

# cAda 길이 g만큼 읽으면서 알파벳이 존재하면 +1
#wl = [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(g):
  if 'a'<= W[i] <= 'z':
    wl[ord(W[i])-ord('a')]+=1
  else:
    wl[ord(W[i])-ord('A')+26]+=1
# print(wl)
length=0
count=0
start=0

# AbrAcadAbRa 길이 S_len만큼 일그면서 알파벳 존재하면 +1
# sl = [...0,0...]
for i in range(S_len):
  if 'a' <=S[i] <='z':
    sl[ord(S[i])-ord('a')]+=1
  else:
    sl[ord(S[i])-ord('A')+26]+=1
  length+=1
  
  #cAda 길이 g만큼 읽었다면
  if length==g:
    if wl==sl: #지금까지 읽은 부분이 cAda와 같다면 count+1
      count+=1
    
    # 같은 거 하나 찾았으니까 그 다음부터는 전 꺼 하나 제외, 뒤에 하나 추가
    #배열에서 맨 앞에 있는 문자를 제외시키는 부분
    if 'a' <= S[start] <='z':
      sl[ord(S[start])-ord('a')]-=1
    else:
      sl[ord(S[start])-ord('A')+26]-=1
    start+=1 # start 는 윈도우의 첫번째 문자를 가리키는 인덱스
    length-=1 # 현재 윈도우의 길이

print(count)
  


