from matplotlib import pyplot as plt

f = open("StopWords.txt", "r")

stops = f.readlines()[0].split()   #our list of stopwords

f.close()

f = open("3MenInABoatCh1.txt", "r")

lines = f.readlines()

f.close()

words = []
for line in lines:
    words.extend(line.split(' '))

stoppos = []
for i in range(len(words)):
    if(words[i] in stops):
        stoppos.append(i)

spacing = []
for i in range(len(stoppos)-1):
    spacing.append(stoppos[i+1] - stoppos[i])

plt.plot(stops, [words.count(x) for x in stops])
plt.xticks(rotation = 'vertical')
fig = plt.gcf()
fig.set_size_inches(60, 10.5)
fig.savefig('wordFreq.png', dpi=100)
plt.clf()

plt.plot(list(set(spacing)), [spacing.count(x) for x in set(spacing)])
fig = plt.gcf()
fig.set_size_inches(10, 10.5)
fig.savefig('spacingFreq.png', dpi=100)