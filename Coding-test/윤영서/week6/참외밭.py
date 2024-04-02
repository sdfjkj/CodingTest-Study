import sys
one_place_cham = int(sys.stdin.readline())
a=[list(map(int, input().split())) for _ in range(6)]
h=0
h_idx=0
w=0
w_idx=0
for i in range(6):
  if a[i][0]==3 or a[i][0]==4:
    if w<a[i][1]:
      w=a[i][1]
      w_idx=i
  elif a[i][0]==1 or a[i][0]==2:
    if h<a[i][1]:
      h=a[i][1]
      h_idx=i

small_w = abs(a[(w_idx-1)%6][1]-a[(w_idx+1)%6][1])
small_h = abs(a[(h_idx-1)%6][1]-a[(h_idx+1)%6][1])
space = w*h - small_w*small_h
print(space*one_place_cham )