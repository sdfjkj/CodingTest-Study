all_num  = set(range(1,10001))
nonself_num=set()

for i in range(1,10001):
  for j in str(i):
    i+=int(j)
  nonself_num.add(i)


self_num=all_num-nonself_num
for i in self_num:
  print(i)