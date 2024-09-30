# https://gorokke.tistory.com/38
import sys
input = sys.stdin.readline
s = input().strip()
t = input().strip()

while len(t)> len(s):
    if (t[-1]=='A'):
        # print('A 공식')
        t=t[:-1]
    else:
        # print('B 공식')
        t=t[:-1]
        t=t[::-1]
if t==s:
    print(1)
else:
    print(0)