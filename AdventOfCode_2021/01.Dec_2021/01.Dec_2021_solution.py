measurements = []
with open("01.Dec_2021_Input.txt") as f:
    measurements = list(map(int, f.readlines()))
    counter = 0

    for i in range(len(measurements) - 1):
        if measurements[i] < measurements[i + 1]:
            counter += 1

    print(str(counter) + " measurements are larger than the previous measurement.")