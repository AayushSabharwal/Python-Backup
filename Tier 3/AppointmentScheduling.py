from datetime import datetime

def MakePair(csv):
    l = csv.split(",")
    tt1 = l[0].split(":")
    tt2 = l[1].split(":")
    t1 = datetime(2001, 1, 1, int(tt1[0]), int(tt1[1]))
    t2 = datetime(2001, 1, 1, int(tt2[0]), int(tt2[1]))
    return (t1, t2)

def RemoveIntersections(l, app): #!!!!
    for a in l:
        if (app[0] <= a[0] <= app[1]):
            l.remove(a)
        elif (app[0] <= a[1] <= app[1]):
            l.remove(a)
    
    return l
    
n = int(input("Number of appointments: "))
l = [MakePair(x) for x in input("space separated appointments, csv times, times h:m").split(' ')]

l.sort(key = lambda x: x[1])
#print([ (x[0].strftime("%X"), x[1].strftime("%X")) for x in l])

endtime = 0
curapp = 0
count = 0
while(len(l) > 0):
    endtime = l[0][0]
    curapp = l[0]
    l = RemoveIntersections(l, curapp)
    print([ (x[0].strftime("%X"), x[1].strftime("%X")) for x in l])
    print(curapp[0].strftime("%X"), curapp[1].strftime("%X"))
    count = count + 1

print(count)