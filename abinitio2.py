V,E,Q=[int(i) for i in input().split()]
outs = [[False for v2 in '*'*V] for v in '*'*V]

def edge(path):outs[path[0]][path[1]]=True

for i in '*'*E:edge([int(i) for i in input().split()])

for i in '*'*Q:
    query = [int(i) for i in input().split()]
    if query[0]==1:
        outs+=[[False for v2 in '*'*len(outs)]]
        for i in range(len(outs)):outs[i]+=[False]
    elif query[0]==2:
        edge(query[1:])
    elif query[0]==3:
        for i in range(len(outs)):
            outs[i][query[1]]=False
            outs[query[1]][i]=False
    elif query[0]==4:
        outs[query[1]][query[2]]=False
    elif query[0]==5:
        temp = [[False for i in '*'*len(outs)] for i in '*'*len(outs)]
        for x in range(len(outs)):
            for y in range(len(outs)):
                temp[x][y]=False if not outs[y][x] else True
                print()
                print("("+str(x)+","+str(y)+")"+str(outs[y][x]))
                print('\n'.join(''.join([' ','.'][cell]for cell in row)for row in outs))
        outs=temp
    elif query[0]==6:
        for x in range(len(outs)):
            for y in range(len(outs)):
                if x==y:continue
                outs[x][y] = not outs[x][y]



print(len(outs))

for i in range(len(outs)):
    d=sum(outs[i])
    x=0
    y=0
    for e in range(len(outs[i])):
        if outs[i][e]==True:
            x+=7**y*e
            y+=1
    print(str(d)+" "+str(x))