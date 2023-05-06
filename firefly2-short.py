R=range
I=input
L,H=[int(i)for i in I().split()]
P=[L//2]
F=[0 for i in R(H)]
C=[0 for i in R(H)]
for i in R(L):
 x=int(I())
 if i%2:C[H-x]+=1
 else:F[x]+=1
for i in R(1,H)[::-1]:P+=[P[-1]+F[i]-C[i]]
x=min(P)
print(str(x)+" "+str(P.count(x)))