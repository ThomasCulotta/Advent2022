import re

filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

pattern = "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
sensorsAndBeacons = []

for line in data:
    result = re.match(pattern, line)
    sensorsAndBeacons.append(((int(result.group(1)), int(result.group(2))), (int(result.group(3)), int(result.group(4)))))

def Part1():
    searchRow = 2000000
    invalidPositions = set()

    for sensor, beacon in sensorsAndBeacons:
        distance = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])

        if (searchRow in range(sensor[1] - distance, sensor[1] + distance + 1)):
            reduction = abs(searchRow - sensor[1])
            adjustedDistance = distance - reduction

            minX = sensor[0] - adjustedDistance
            maxX = sensor[0] + adjustedDistance

            invalidPositions.update(range(minX, maxX + 1))

    for sensor, beacon in sensorsAndBeacons:
        if (beacon[1] == searchRow and
            beacon[0] in invalidPositions):
            invalidPositions.remove(beacon[0])

    return len(invalidPositions)

def Part2():
    maxCoord = 4000000
    validXRanges = {}

    for sensor, beacon in sensorsAndBeacons:
        distance = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])

        for y in range(max(0, sensor[1] - distance), min(maxCoord, sensor[1] + distance + 1)):
            reduction = abs(y - sensor[1])
            adjustedDistance = distance - reduction

            minX = sensor[0] - adjustedDistance
            maxX = sensor[0] + adjustedDistance

            if y not in validXRanges:
                validXRanges[y] = []
                if (minX > 0):
                    validXRanges[y].append((0, minX - 1))
                if (maxX < maxCoord):
                    validXRanges[y].append((maxX + 1, maxCoord))

            else:
                if (len(validXRanges[y]) == 0):
                    continue

                newXRanges = []
                curXRanges = validXRanges[y]
                for i in range(len(curXRanges)):
                    if (minX > curXRanges[i][0] and
                        maxX < curXRanges[i][1]):
                        newXRanges.append((curXRanges[i][0], minX - 1))
                        newXRanges.append((maxX + 1, curXRanges[i][1]))

                    elif (curXRanges[i][0] < minX < curXRanges[i][1]):
                        newXRanges.append((curXRanges[i][0], minX - 1))

                    elif (curXRanges[i][0] < maxX < curXRanges[i][1]):
                        newXRanges.append((maxX + 1, curXRanges[i][1]))

                    elif (minX <= curXRanges[i][0] and
                          maxX >= curXRanges[i][1]):
                        continue

                    else:
                        newXRanges.append(curXRanges[i])

                validXRanges[y] = newXRanges


    for y, xRanges in validXRanges.items():
        if (len(xRanges) == 1 and
            xRanges[0][0] == xRanges[0][1]):
            return xRanges[0][0] * 4000000 + y

    return -1

print(Part1())
print(Part2())
