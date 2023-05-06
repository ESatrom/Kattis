N=int(input())
p=[[int(i)for i in input().split()]for x in'*'*(N-1)]
l=[[int(i),0][int(i)<0]for i in input().split()]
while sum(l[1:])>0:
 for i in range(N):
  for P in p:
   if P[1]-1==i:
    X,Y=l[i],P[2]/100
    l[P[0]-1]=max(min(X/Y,X**[1,.5][P[3]]/Y),l[P[0]-1])                
    l[i]=0
print(l[0])