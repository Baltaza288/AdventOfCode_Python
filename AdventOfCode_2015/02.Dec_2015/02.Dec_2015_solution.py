with open('02.Dec_2015_Input.txt') as f:
    meassurements = f.read().splitlines()

presents = []
areas = []
n = 0
paper = 0
ribbon = 0

for i in meassurements:
    i = i.split("x")
    presents.append(i)

for i in range(len(presents)):
    areas = [int(presents[n][0]) * int(presents[n][1]),
             int(presents[n][0]) * int(presents[n][2]),
             int(presents[n][1]) * int(presents[n][2])]
    paper += 2 * areas[0] + 2 * areas[1] + 2 * areas[2] + min(areas)

########## Part2 ##########

    presents_ = [ int(x) for x in presents[n]]
    presents_.sort()
    girth = 2 * presents_[0] + 2 * presents_[1]
    ribbon += girth + presents_[0] * presents_[1] * presents_[2]
    n += 1

print("PART 1: The elfes need to order " + str(paper) + " cm² of wrapping paper.")
print("PART 2: The elfes need to order " + str(ribbon) + " cm of ribbon.")
