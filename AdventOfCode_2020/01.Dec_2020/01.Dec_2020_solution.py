with open('01.Dec_2020_Input.txt') as f:
    entries = f.readlines()

    for x in entries:

        for y in entries:
            if int(x) + int(y) == 2020:
                solution_1 = int(x) * int(y)

            for z in entries:
                if int(x) + int(y) + int(z) ==2020:
                    solution_2 = int(x) * int(y) * int(z)

    print("Part 1: " + str(solution_1))
    print("Part 2: " + str(solution_2))