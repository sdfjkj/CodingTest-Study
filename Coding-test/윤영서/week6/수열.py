import sys
input = sys.stdin.readline

N,k = map(int, input().split())
a = list(map(int, input().split()))
# print(a)
length =0
count=0
start=0
plused=0
plused_array=[]
for i in range(N):
    length+=1
    plused+=a[i]
    if length==k:
        plused_array.append(plused)
        plused-=a[start]
        start+=1
        length-=1

print(max(plused_array))