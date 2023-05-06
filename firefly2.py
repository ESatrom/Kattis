L, H = [int(i) for i in input().split(' ')] #initialize length and height integers from first line of input
paths = [L//2]                              #initialize paths 1D array with the uppermost level (half length, rounded down)
flor = [0 for i in range(H)]                #initialize array of heights of floor spikes, 0 spikes of each height
ceil = [0 for i in range(H)]                #initialize array of heights of ceiling spikes, 0 spikes of each height
for i in range(L):                          #reading in each spike length from input
    if i%2:ceil[H-int(input())]+=1          #if odd numbered spike, add it to the ceiling (starting counting at 0) (1 is a "truthy" value, 1 is interpreted as True, 0 as False)
    else:flor[int(input())]+=1              #if even numbered spike, add it to the floor
for i in range(1,H)[::-1]:                  #each height, starting from H-1
    paths+=[paths[-1]+flor[i]-ceil[i]]      #make a new path for the next level down from the ceiling
x=min(paths)                                #find lowest number of objects in a path
print(str(x)+" "+str(paths.count(x)))       #print x and number of paths with lowest number of objects