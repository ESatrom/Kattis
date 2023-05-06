def run():
    n,s,m = [int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    h=0
    mem=[s]
    while b[s]!=m:
        s+=b[s]
        h+=1
        if s<0:
            print("left\n"+str(h))
            return
        if s>=len(b):
            print("right\n"+str(h))
            return
        if s in mem:
            print("cycle\n"+str(h))
            return
        mem+=[s]
    
    print("magic\n"+str(h))
    
run()