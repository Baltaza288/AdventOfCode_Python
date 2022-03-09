with open('05.Dec_2015_Input.txt') as f:
    passphrases = f.read().splitlines()

# hat das Passwort ab, cd, pq oder xy enthalten?
valid = []
for n in passphrases:
    i = 0
    j = 1
    index = 0
    while j < len(n):
        chars = n[i] + n[j]
        if chars in ('ab','cd','pq','xy'):
            index += 1
        i += 1
        j += 1
    if index == 0:
        # falls nicht:
        valid.append(n)

# hat das Passwort mindestens 3 x a,e,i,o oder u?
x = 0
valid2 = []
for n in valid:
    vowels = 0
    for m in n:
        if m in ('a','e','i','o','u'):
            vowels += 1
    if vowels >= 3:
        valid2.append(n)
    x += 1

# hat das Passwort mindestens 1x doppelte Buchstaben?
counter = 0
valid3 = []
for n in valid2:
    i = 0
    j = 1
    index = 0
    while j < len(n):
        if n[j] == n[i]:
            index += 1
        i += 1
        j += 1
    if index > 0:
        valid3.append(n)

print("PART 1: There are " + str(len(valid3)) + " good passphrases.")

########## Part2 ##########

