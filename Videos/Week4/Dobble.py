#Dobble Game
import string
import random
symbols = list(string.ascii_letters)
card1 = [0]*5
card2 = [0]*5
pos1 = random.randint(0,4)
pos2 = random.randint(0,4)

samesymbol = random.choice(symbols)
symbols.remove(samesymbol)
print(samesymbol)
print(pos1)
print(pos2)

card1[pos1] = samesymbol
card2[pos2] = samesymbol

if(pos1 != pos2):
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])

for i in range(5):
    if(i != pos1 and i != pos2):
        card1[i] = random.choice(symbols)
        symbols.remove(card1[i])
        card2[i] = random.choice(symbols)
        symbols.remove(card2[i])

print(card1)
print(card2)