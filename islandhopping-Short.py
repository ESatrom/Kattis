def d(a,b):return((a[0]-b[0])**2+(a[1]-b[1])**2)**.5
for n in range(int(input())):
 I=[[float(x)for x in input().split()]for i in'*'*int(input())]
 R=dict(zip(range(len(I)),[d(I[0], i) for i in I]))
 I=dict(zip(range(len(I)),I))
 I.pop(0)
 D=0
 while len(I)>0:
  ids=list(I.keys())
  ri=ids[0]
  rd=R[ri]
  for i in ids:
   if R[i]<rd:
    rd=R[i]
    ri=i
  o=I.pop(ri)
  ids.remove(ri)
  for i in ids:
   R[i]=min(R[i],d(o,I[i]))
  D+=rd
 print(D)