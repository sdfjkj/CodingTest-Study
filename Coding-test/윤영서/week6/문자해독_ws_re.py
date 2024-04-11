import sys
input= sys.stdin.readline
n,m  = map(int, input().split())
W=input() #cAda
S=input() # AbrAcadAbRa


#알파벳은 26개, 대문자까지는 52개인데 중간에 6,7개가 더 있음
#결론은 넉넉잡아 58개 정도로 만들어두기
wl = [0]*58
sl = [0]*58

#wl에 W의 정보를 만든다 > sl이랑 비교하기 위해!
for i in range(n):
  if 'a' <= W[i] <= 'z':
    wl[ord(W[i])-ord('a')]+=1
  else:
    wl[ord(W[i])-ord('A')+26]+=1

length =0 #윈도우의 길이
count=0 # 답 
start=0 # 윈도우의 첫글자

#sl에 정보 저장하면서 바로 비교
for i in range(m):
  if 'a' <= S[i] <= 'z':
    sl[ord(S[i])-ord('a')]+=1
  else:
    sl[ord(S[i])-ord('A')+26]+=1
  length+=1

  if length==n:
    if wl==sl:
      count+=1
  
    if 'a'<= S[start] <='z':
      sl[ord(S[start])-ord('a')]-=1
    else:
      sl[ord(S[start])-ord('A')+26]-=1
    start+=1
    length-=1
print(count)
