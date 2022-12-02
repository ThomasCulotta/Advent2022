filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

def Part1():
    maxCal = 0
    curCal = 0

    for line in data:
        if not line.strip():
            if curCal > maxCal:
                maxCal = curCal

            curCal = 0

        else:
            curCal += int(line)

    return maxCal

def Part2():
    maxCals = [0, 0, 0]
    curCal = 0

    for line in data:
        if not line.strip():
            minCal = min(maxCals)
            if curCal > minCal:
                maxCals[maxCals.index(minCal)] = curCal

            curCal = 0

        else:
            curCal += int(line)

    return sum(maxCals)

print(Part1())
print(Part2())
