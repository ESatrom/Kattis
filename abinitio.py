V,E,Q=[int(i) for i in input().split()]
ins = {}
outs = {}
flip = False

def edge(path):
    print(path)
    try:
        outs[path[0]]+=[path[1]]
    except:
        outs[path[0]]=[path[1]]
    try:
        ins[path[1]]+=[path[0]]
    except:
        ins[path[1]]=[path[0]]

for i in '*'*E:
    edge([int(i) for i in input().split()])
    
for i in '*'*Q:
    query = [int(i) for i in input().split()]
    if query[0]==1:
        V+=1
    elif query[0]==2:
        edge(query[1:])
    elif query[0]==3:
        try:
            for e in ins[query[1]]:
                outs[e].remove(query[1])
        except:pass
        try:
            for e in outs[query[1]]:
                ins[e].remove(query[1])
        except:pass
        ins[query[1]]=[]
        outs[query[1]]=[]
    elif query[0]==4:
        if flip:
            temp = query[1]
            query[1] = query[2]
            query[2] = temp
        outs[query[1]].remove(query[2])
        ins[query[2]].remove(query[1])
    elif query[0]==5:
        flip = not flip
    elif query[0]==6:
        pass

print(V)
if flip:
    temp=ins
    ins=outs
    outs=temp
for i in range(V):
    try:
        outs[i]=outs[i]
    except:
        outs[i]=[]
    d=len(outs[i])
    x=sum(7**n*outs[i][n] for n in range(len(outs[i])))
    print(str(d)+" "+str(x))