#Q3 to find best way for Arun to go to office
n, v1, v2 = [int(x) for x in input().split(" ")]
cabtime = 2*n/v2
walktime = (2**0.5)*n/v1

if(cabtime < walktime):
    print('Cab')
else:
    print('Walk')