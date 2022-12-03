filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

ASCII_A = 65
ASCII_a = 97

def Part1():
    totalPri = 0

    for sack in data:
        sack = sack.strip()
        midpoint = int(len(sack) / 2)

        for i in range(midpoint, len(sack)):
            item = sack[i]

            if (sack.index(item) < midpoint):
                pri = ord(item)

                if pri < ASCII_a:
                    totalPri += pri - ASCII_A + 27
                else:
                    totalPri += pri - ASCII_a + 1

                break

    return totalPri

def Part2():
    totalPri = 0

    for i in range(0, len(data), 3):
        sack1 = set(data[i].strip())
        sack2 = set(data[i + 1].strip())
        sack3 = set(data[i + 2].strip())

        badge = sack1.intersection(sack2).intersection(sack3).pop()
        pri = ord(badge)

        if pri < ASCII_a:
            totalPri += pri - ASCII_A + 27
        else:
            totalPri += pri - ASCII_a + 1

    return totalPri

print(Part1())
print(Part2())
