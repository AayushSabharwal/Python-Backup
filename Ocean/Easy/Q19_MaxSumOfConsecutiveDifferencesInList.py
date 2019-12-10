l = [int(x) for x in input().split()]

l.sort()    

#idea is to continually take elements from l and put them in the front or back of ans so as to maximise difference
ans = []    #resultant arrangement
ans.append(l[len(l)-1]) #adding the maximum element of l to ans
l.pop(n-1)  #removing the corresponding element

while(len(l) > 0):
    #list of all possible absolute differences from inserting an element of l into ans
    #obviously, to maximise difference we only consider smallest and largest elements of l
    possible_diffs = [absval(l[len(l) - 1] - ans[len(ans) - 1]),
                      absval(l[len(l) - 1] - ans[0]),
                      absval(l[0] - ans[len(ans) - 1]),
                      absval(l[0] - ans[0])]
    
    #insert element at position depending on which possibility maximises our difference
    if(possible_diffs[0] >= possible_diffs[1] and possible_diffs[0] >= possible_diffs[2] and possible_diffs[0] >= possible_diffs[3]):
        ans.append(l[len(l) - 1])
        l.pop(len(l) - 1)
    elif(possible_diffs[1] >= possible_diffs[0] and possible_diffs[1] >= possible_diffs[2] and possible_diffs[1] >= possible_diffs[3]):
        ans.insert(0, l[len(l) - 1])
        l.pop(len(l) - 1)
    elif(possible_diffs[2] >= possible_diffs[1] and possible_diffs[2] >= possible_diffs[0] and possible_diffs[2] >= possible_diffs[3]):
        ans.append(l[0])
        l.pop(0)
    else:
        ans.insert(0, l[0])
        l.pop(0)

for i in ans:
    print(i, end = ' ')