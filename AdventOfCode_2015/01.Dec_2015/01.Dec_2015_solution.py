with open('01.Dec_2015_Input.txt') as f:
    directions = f.read().strip()

solution1 = 0

for i in directions:
    if i == '(':
        solution1 += 1
    elif i == ')':
        solution1 -= 1

print("Part1: Santa has go to floor: " + str(solution1))

########## Part2 ##########

solution1 = 0
solution2 = 0

for i in directions:
    if i == '(':
        solution1 += 1
    elif i == ')':
        solution1 -= 1

    solution2 += 1

    if solution1 < 0:
        break

print("Part2: Santa went to basement on character position: " + str(solution2))




