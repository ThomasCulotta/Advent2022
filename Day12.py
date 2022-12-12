from heapq import heappush, heappop

filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

grid = [[ord(point) for point in line.strip()] for line in data]

start = (0, 0, 0, 0)
dest = (0, 0)

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == ord("S"):
            start = (ord("a"), 0, x, y)
            grid[y][x] = ord("a")
        elif grid[y][x] == ord("E"):
            dest = (x, y)
            grid[y][x] = ord("z")

def Part1():
    searching = [start]
    visited = set()
    maxX, maxY = len(grid[0]), len(grid)

    while any(searching):
        height, steps, x, y = heappop(searching)

        if (x, y) == (dest[0], dest[1]):
            return steps

        if (x, y) in visited:
            continue

        visited.add((x,y))

        offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        nextTiles = [(nextX,
                      nextY,
                      steps + 1) for offset in offsets if (nextX := x + offset[0]) in range(maxX) and
                                                          (nextY := y + offset[1]) in range(maxY) and
                                                          ((grid[nextY][nextX] - height) < 2)]

        for x, y, steps in nextTiles:
            heappush(searching, (grid[y][x], steps, x, y))

    return -1

def Part2():
    starts = []
    totalSteps = []

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == ord("a"):
                starts.append((ord("a"), 0, x, y))

    for s in starts:
        searching = [s]

        visited = set()
        maxX, maxY = len(grid[0]), len(grid)

        while any(searching):
            height, steps, x, y = heappop(searching)

            if (x, y) == (dest[0], dest[1]):
                totalSteps.append(steps)

            if (x, y) in visited:
                continue

            visited.add((x,y))

            offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            nextTiles = [(nextX,
                          nextY,
                          steps + 1) for offset in offsets if (nextX := x + offset[0]) in range(maxX) and
                                                              (nextY := y + offset[1]) in range(maxY) and
                                                              ((grid[nextY][nextX] - height) < 2)]

            for x, y, steps in nextTiles:
                heappush(searching, (grid[y][x], steps, x, y))

    return min(totalSteps)

print(Part1())
print(Part2())
