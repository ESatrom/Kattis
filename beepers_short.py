import copy
I=input
def D(x,y,a,b):return abs(x-a)+abs(y-b)
def E(t):return','.join((' '.join(str(i)for i in p)for p in sorted(t)))
def M(z,x,y,a,b,m):
 if len(z)==0:return D(x, y, a, b)
 e=E(z)
 try:return m[x][y][e]
 except:pass
 u=[]
 for t in z:
  w=copy.deepcopy(z)
  w.remove(t)
  u+=[M(w,t[0],t[1],a,b,m)+D(t[0],t[1],x,y)]
 Z=min(u)
 m[x][y][e]=Z
 return Z
X=int
for i in range(int(I())):
 a,b=[X(j)for j in I().split()]
 x,y=[X(j)-1 for j in I().split()]
 B=X(I())
 z=[[X(j)-1 for j in I().split()]for i in'*'*B]
 print(M(z,x,y,x,y,[[{}for j in'*'*b]for i in'*'*a]))