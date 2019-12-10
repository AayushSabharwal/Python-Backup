f = open("plain.txt", "r")
raw = f.read()
rawcharlist = list(raw)
f.close()

charlist = []
for i in rawcharlist:
      if(i.isalnum()):
            charlist.append(i.lower())

import random
shiftn = random.randint(1, 25)
shift = {
         'a' : 'b',
         'b' : 'c',
         'c' : 'd',
         'd' : 'e',
         'e' : 'f',
         'f' : 'g',
         'g' : 'h',
         'h' : 'i',
         'i' : 'j',
         'j' : 'k',
         'k' : 'l',
         'l' : 'm',
         'm' : 'n',
         'n' : 'o',
         'o' : 'p',
         'p' : 'q',
         'q' : 'r',
         'r' : 's',
         's' : 't',
         't' : 'u',
         'u' : 'v',
         'v' : 'w',
         'w' : 'x',
         'x' : 'y',
         'y' : 'z',
         'z' : 'a',
         }

for shifti in range(shiftn):
      for i in range(len(charlist)):
            charlist[i] = shift[charlist[i]]
      
f = open("encrypt.txt", "w")
for i in charlist:
      f.write(i)

f.close()