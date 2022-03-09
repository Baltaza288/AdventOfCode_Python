with open('03.Dec_2015_Input.txt') as f:
    directions = f.read().strip()

x = 0
y = 0
pos = [x,y]
log = [pos]

for n in directions:
    if   n == '^': y += 1
    elif n == 'v': y -= 1
    elif n == '<': x -= 1
    elif n == '>': x += 1

    pos = [x,y]
    if pos not in log:
        log.append(pos)

haeuser = len(log)

print("PART 1: Santa brings presents to " + str(haeuser) + " different houses.")

########## Part2 ##########
i = 0
x2 = 0
y2 = 0
x = 0
y = 0
log = []

for n in directions:

    if i % 2:
        if   n == '^': y2 += 1
        elif n == 'v': y2 -= 1
        elif n == '<': x2 -= 1
        elif n == '>': x2 += 1
        pos2 = [x2,y2]
        if pos2 not in log:
            log.append(pos2)
    else:
        if   n == '^': y += 1
        elif n == 'v': y -= 1
        elif n == '<': x -= 1
        elif n == '>': x += 1
        pos = [x,y]
        if pos not in log:
            log.append(pos)
    i += 1

haeuser2 = len(log)

print("PART 2: Santa and RoboSanta brings presents to " + str(haeuser2) + " different houses.")
