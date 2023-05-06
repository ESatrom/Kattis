import copy


#Taxicab distance between 2 points
def dist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2) 

#lists are not hashable objects (therefore not able to be used as a key for a dictionary/map), strings are. This converts a 2D list to an equivalent string to be used as a dictionary key
def encode(targList):
    return ','.join((' '.join(str(i) for i in point) for point in sorted(targList))) 


#return minimum distance from a given point to a given end point while hitting all targets.
def minDist(targs, x, y, Ex, Ey, mem):
    if len(targs)==0:return dist(x, y, Ex, Ey) #if there are no targets, just return distance
    targEnc=encode(targs) #save encoded target list to variable to save execution time
    try:return mem[x][y][targEnc] #given startpoint x, given startpoint y, given target list: if this minimum distance value has been saved, use it
    except:pass #if it hasn't been saved, it will error out and continue execution
    dists=[] #to be list of possible minimum distances for each possible first target
    for t in targs: #for each possible first element:
        ts=copy.deepcopy(targs) #deepcopy is a copy of an object which does not include references (you can modify the copy without modifying the original)
        ts.remove(t) #remove that element from the list to be forwarded
        dists+=[minDist(ts, t[0], t[1], Ex, Ey, mem)+dist(t[0],t[1],x,y)] #distance from current point to target point, plus the minimum distance from that point. This makes it recursive in the manner described in class.
    Z=min(dists)#set Z to the minimum distance
    mem[x][y][targEnc]=Z #store minimum distance for a given parameter set (start x,y and targs). This eliminates redundant calculations.
    return Z #return that shortest distance


n=int(input()) # There will be N test cases
for i in range(n): #repeat for each test case
    bx,by=[int(j) for j in input().split()] #board dimensions
    mem=[[{} for y in range(by)] for x in range(bx)] #initialize a memory board for each starting position
    x,y=[int(j)-1 for j in input().split()] # karel's starting position, converted from 1-indexed to 0-indexed
    n2=int(input()) #number of beepers
    targets=[]
    for j in range(n2):
        targets+=[[int(j)-1 for j in input().split()]] # make a list of beepers
    print(minDist(targets, x, y, x, y, mem)) #do the stuff