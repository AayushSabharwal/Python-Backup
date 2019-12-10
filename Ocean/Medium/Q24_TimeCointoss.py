import time
l = []
for i in range(100):
    if((time.monotonic()*1000)%2 == 0):
        l.append("H")
    else:
        l.append("T")

print(l)