import hashlib
with open('04.Dec_2015_Input.txt') as f:
    sec_key = f.read()
n = 0
builded_sec = sec_key + str(n)
hashed = hashlib.md5(builded_sec.encode())
searched = hashed.hexdigest()[:5]

while searched != '00000':
    builded_sec = sec_key + str(n)
    hashed = hashlib.md5(builded_sec.encode())
    searched = hashed.hexdigest()[:5]
    n += 1

print("PART 1: The lowest number it combines with to make an MD5 hash starting with five zeroes is " + str(n - 1) + ".")

########## Part2 ##########

m = 0
while searched != '000000':
    builded_sec = sec_key + str(m)
    hashed = hashlib.md5(builded_sec.encode())
    searched = hashed.hexdigest()[:6]
    m += 1

print("PART 2: The lowest number it combines with to make an MD5 hash starting with six zeroes is " + str(m - 1) + ".")
