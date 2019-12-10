# assuming input file consist of nxn table, entries space separated. Entries are csv of preference amount

f = open("stable_table.txt", "r")
raw = f.readlines()
f.close()

left_pref = []
right_pref = []
for i in range(len(raw)):
    left_pref.append([int(x.split(',')[0]) for x in raw[i].split(" ")])
    right_pref.append(([int(x.split(',')[1]) for x in raw[i].split(" ")]))

free_lefts = [i for i in range(len(raw))]  # list of unmatched lefts

matches = {}  # dict mapping right index to left index for a matched pair

while len(free_lefts) != 0: # while we still have unmatched entries
    # list of tuples containing index of right and their preference amount
    prefs = [(i, left_pref[free_lefts[0]][i]) for i in range(len(left_pref[free_lefts[0]]))]
    prefs.sort(key=lambda x: x[1], reverse=True)    # sorting in descending order by second element of tuple
    has_match = False   # whether this person is matched yet
    trying = 0  # which index tuple in prefs we are trying to match with
    while not has_match:
        # if the person we are trying to match with is unmatched
        if prefs[trying][0] not in list(matches.keys()):
            has_match = True
            break
        # if the person who are trying to match with likes us more than their current person
        elif right_pref[prefs[trying][0]][free_lefts[0]] > right_pref[prefs[trying][0]][matches[prefs[trying][0]]]:
            free_lefts.append(matches[prefs[trying][0]])    # previously assigned person is not free
            has_match = True
            break
        trying += 1 # increment the index of what we're trying

    if not has_match:
        print("ERR: unmatched")
        break

    matches[prefs[trying][0]] = free_lefts[0]
    free_lefts = free_lefts[1:]

for k, v in matches.items():
    print(k, v)
