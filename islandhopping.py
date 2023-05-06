def dist(point1, point2):return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**.5


for n in range(int(input())): #Repeat for each set of islands
    islands=[[float(x) for x in input().split()]for i in'*'*int(input())] #process island input into a list of coordinate tuples
    routes=dict(zip(range(len(islands)),[dist(islands[0], i) for i in islands])) #initialize routes as a dict: target island ID as key, distance to that island from start island as value
    islands=dict(zip(range(len(islands)),islands)) #convert islands to a dictionary so that elements can be safely removed
    islands.pop(0) #routes have already been generated from island 0
    total_distance=0
    while len(islands)>0: #visited islands are removed, thus when all islands have been visited, length of islands will be 0
        ids=list(islands.keys()) #list of unvisited island ids
        ri=ids[0] #id of shortest available route
        rd=routes[ri] #length of shortest available route
        for i in ids:
            if routes[i]<rd:
                rd=routes[i]
                ri=i
        o=islands.pop(ri) #remove new node from list: origin point for each new route
        ids.remove(ri)
        for i in ids: #for each route from the new node to remaining nodes: if it is shorter than the existing route to that node, replace existing route
            routes[i]=min(routes[i],dist(o,islands[i]))
        total_distance+=rd
    print(total_distance)