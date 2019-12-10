import KthSmallest as kth
import time
from matplotlib import pyplot as plt
import random

l = random.sample(range(10000000), 100000)
easytime = []
for i in range(1, 101):
    start = time.time()
    kth.kth(l, i)
    end = time.time()
    easytime.append(end-start)

ingtime = []
for i in range(1, 101):
    start = time.time()
    kth.kth_ing(l, i)
    end = time.time()
    ingtime.append(end - start)

x = range(1, 101)

plt.plot(x, easytime)
plt.plot(x, ingtime)