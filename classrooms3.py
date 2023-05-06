NA, NC = [int(i) for i in input().split()]                          #read in number of assignments and classrooms respectively.
activities = [[int(i)for i in input().split()]for x in range(NA)]   #initialize activities with input. List of tuples [start, end]
activities.sort(key=lambda x:x[1]+(x[0]/10**9))                     #sort activities by lowest ending time first, highest ending time last, break tie by lowest start time
rooms = [0 for room in range(NC)]                                   #initialize each room at time 0
filled = 0                                                          #no classes have yet been filled
while 1: #while true
    m = min(rooms)                                                  #find earliest available time
    i = rooms.index(m)                                              #find room for that time
    activities = list(filter(lambda x:x[0]>m, activities))
    activities.sort(key=lambda x:x[1]+(x[0]/10**9))
    if len(activities)==0:break
    filled+=1 #we found an activity!
    rooms[i]=activities[0][1]                                       #time for room is now ending time for that activity
    activities = activities[1:]
print(filled)