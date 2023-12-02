
###################################################################
### Function to create all files for one year of Advent_of_Code ###
###################################################################

import os
year = input("witch year is it?\n")
for x in range(1,26,1):
    num = x
    day = "{:02d}".format(num)
    path = 'C:/Users/altma/Documents/Coding/AdventOfCode_Python/AdventOfCode_' + year + '/' + day + '.Dec_' + year
    challenge = os.path.join(path, day + '.Dec_' + year + '_Challenge.txt')
    challenge_d = os.path.join(path, day + '.Dec_' + year + '_Challenge_D.txt')
    input = os.path.join(path, day + '.Dec_' + year + '_Input.txt')
    solution = os.path.join(path, day + '.Dec_' + year + '_solution.py')
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(challenge, "a")
    f = open(challenge_d, "a")
    f = open(input, "a")
    f = open(solution, "a")