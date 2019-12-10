f = open("encrypt.txt", "r")
raw = f.read()
rawcharlist = list(raw)
f.close()

charlist = []
for i in rawcharlist:
      if(i.isalnum()):
            charlist.append(i)

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

for shifti in range(25):
      for i in range(len(charlist)):
            charlist[i] = shift[charlist[i]]
      print(shifti)
      for i in charlist:
            print(i, end = '')
      print()
      print()