with open('01.Dec_2015_Input.txt') as f:
    directions = f.read().strip()

etage = 0

for i in directions:
    if i == '(':
        etage = etage + 1

    if i == ')':
        etage = etage - 1

print(etage)