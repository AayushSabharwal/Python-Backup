import random

print("Enter space separated list of letter,frequency")
raw = [(x.split(',')[0], int(x.split(',')[1])) for x in input().split()]
print(raw)
freq = {}
total = 0
for pair in raw:
    freq[pair[0]] = pair[1]
    total += pair[1]

f = open("huffman_uncompressed.txt", "w")

for i in range(total):
    choice = random.choice(list(freq.keys()))
    freq[choice] -= 1
    if freq[choice] == 0:
        del freq[choice]
    f.write(choice)
