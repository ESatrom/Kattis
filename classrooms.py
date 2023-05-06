NA, NC = [int(i) for i in input().split()]
activities = []
for i in range(NA):
    activities += [[int(i) for i in input().split()]]
activities.sort(key=lambda x:x[1]-x[0])
activities = [range(a[0],a[1]+1) for a in activities]
rooms = [range(10**9+1) for room in range(NC)]
for activity in activities:
    for room in rooms:
        sum(int(not time in room) for time in activity)
                available=False
                break
print(1)

#this is bad