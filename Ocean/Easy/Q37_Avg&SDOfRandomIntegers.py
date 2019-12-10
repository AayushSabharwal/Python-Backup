import random
n = int(input("Enter n"))
k = int(input("Enter k"))
nums = random.sample(range(n), k)   #picks k random integers in the range [0, n)
nums.sort()
diffs = [] #dfference between consecutive entries

total = 0 #sum of differences
for i in range(1, k):   #since we are finding difference between ith and i-1th entries, our loop starts from 1 not 0
    diffs.append(nums[i] - nums[i-1])   #since the list is sorted, we know that the difference is positive
    total = total + diffs[i-1] #aside form appending differences to our list, we also find the sum of the differences

avg = total / (k-1)     #dividing the total by the number of entries. Since we had k integers in nums, there are k-1 differences in diffs

variance = 0 #standard deviation is sqrt of variance. variance is average of (avg - diffs[i])**2

for i in range(k-1): #looping through diffs list
    variance = variance + (avg - diffs[i])**2   #adding squares of deviations

variance = variance / (k-1) #final value of variance
sd = variance**0.5  #sqrt of variance
print("list of integers: ", nums)
print("differences: ", diffs)
print("average = ", avg)
print("standard deviation = ", sd)