filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

paths = [[(int(coords.split(",")[0]), int(coords.split(",")[1])) for coords in path.split(" -> ")] for path in data]

minX = 500
maxX, maxY = 0, 0

for path in paths:
    for x, y in path:
        minX = min(minX, x)
        maxX = max(maxX, x)
        maxY = max(maxY, y)

for i in range(len(paths)):
    paths[i] = list(map(lambda coord: (coord[0] - minX, coord[1]), paths[i]))

sandOrigin = (500 - minX, 0)
maxX -= minX
caveGrid = [["." for x in range(maxX + 1)] for y in range(maxY + 1)]

caveGrid[sandOrigin[1]][sandOrigin[0]] = "o"
for path in paths:
    curCoord = None
    for x, y in path:
        if not curCoord:
            caveGrid[y][x] = "#"
            curCoord = (x, y)
            continue

        for i in range(min(curCoord[0], x), max(curCoord[0], x) + 1):
            caveGrid[y][i] = "#"

        for i in range(min(curCoord[1], y), max(curCoord[1], y) + 1):
            caveGrid[i][x] = "#"

        curCoord = (x, y)

floor = maxY + 2
bufferLeftX  = floor - sandOrigin[0]
bufferRightX = max(maxX, sandOrigin[0] + floor) - maxX

sandOrigin2 = (sandOrigin[0] + bufferLeftX, 0)
caveGrid2 = [["." for i in range(bufferLeftX)] + row + ["." for i in range(bufferRightX)] for row in caveGrid]
caveGrid2.append(["." for i in range(len(caveGrid2[0]))])
caveGrid2.append(["#" for i in range(len(caveGrid2[0]))])

def Part1And2(origin, grid, simFloor):
    totalSand = 0

    while (True):
        sandX, sandY = origin

        while (True):
            if (not simFloor and
                sandY == maxY):
                return totalSand

            if (grid[sandY + 1][sandX] == "."):
                sandY += 1
                continue

            if (not simFloor and
                sandX == 0):
                return totalSand

            if (grid[sandY + 1][sandX - 1] == "."):
                sandY += 1
                sandX -= 1
                continue

            if (not simFloor and
                sandX == maxX):
                return totalSand

            if grid[sandY + 1][sandX + 1] == ".":
                sandY += 1
                sandX += 1
                continue

            grid[sandY][sandX] = "o"
            totalSand += 1

            if (simFloor and
                (sandX, sandY) == origin):
                return totalSand

            break

    return -1

print(Part1And2(sandOrigin, caveGrid, False))
print(Part1And2(sandOrigin2, caveGrid2, True))
