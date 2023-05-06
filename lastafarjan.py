cars = int(input())
length = int(input())
cars=[int(i) for i in input().split()]
new_cars = []
while sum(new_cars)<length*4 and len(cars)>0:
    new_cars+=[cars[0]]
    cars=cars[1:]
if sum(new_cars)>length*4:new_cars=new_cars[:-1]
lanes = [length for i in 4*'*']
out=len(new_cars)
new_cars+=[0]
while len(new_cars)>out:
    new_cars=[:-1]
    cars = new_cars
    cars.sort(reverse=True)
    parked_cars=0
    for car in cars:
        parked = False
        backup = -1
        for i in range(4):
            if lanes[i]>=car:
                if lanes[i]==car:
                    backup=i
                else:
                    lanes[i]-=car+1
                    parked=True
                    break
        if not parked:
            if backup>=0:
                lanes[i]-=car+1
                parked_cars+=1
            else:
                break
        else:
            parked_cars+=1
print(parked_cars)