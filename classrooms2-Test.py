import random
def input():
    a = random.randint(1,20)
    return str(a)+" "+str(random.randint(a,20))
NA, NC = [int(i) for i in "10 3".split()]
activities = [[int(i)for i in input().split()]for x in range(NA)]
activities.sort(key=lambda x:x[1])
rooms = [0 for room in range(NC)]
filled = 0
print(rooms)
print(activities)
print()
while 1:
    m = min(rooms)
    i = rooms.index(m)
    x = 0
    try:
        while activities[x][0]<=m:x+=1
    except:break
    filled+=1
    rooms[i]=activities[x][1]
    activities=activities[1+x:]
    print(rooms)
    print(activities)
    print()
print(filled)