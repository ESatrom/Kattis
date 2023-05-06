NA, NC = [int(i) for i in input().split()]                          #read in number of assignments and classrooms respectively.
activities = [[int(i)for i in input().split()]for x in range(NA)]   #initialize activities with input. List of tuples [start, end]
activities.sort(key=lambda x:x[1]+(x[0]/10**9))                     #sort activities by lowest ending time first, highest ending time last, break tie by lowest start time
rooms = [0 for room in range(NC)]                                   #initialize each room at time 0
filled = 0                                                          #no classes have yet been filled
next_activities = activities.copy()
for room in rooms:
    activities = next_activities.copy()
    next_activities = []
    while 1: #while true
        x = 0
        try:
            while activities[x][0]<=room:x+=1                              #find earliest-ending activity which starts at an available time in that room
        except:break
        filled+=1 #we found an activity!
        room=activities[x][1]                                       #time for room is now ending time for that activity
        next_activities += activities[:x]
        activities=activities[1+x:]                                     #destroy that activity, and all activities preceding (too early start)
print(filled)