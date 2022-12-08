filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = [line.strip() for line in file.readlines()]

def Part1():
    numVisible = len(data) * 2 + len(data[0]) * 2 - 4

    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            tree = int(data[i][j])
            row = data[i]
            col = [data[k][j] for k in range(len(data))]

            if ((tree > int(max(row[:j]))) or
                (tree > int(max(row[j + 1:]))) or
                (tree > int(max(col[:i]))) or
                (tree > int(max(col[i + 1:])))):
                numVisible += 1
                continue

    return numVisible

def Part2():
    bestScore = 0

    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            score, north, south, east, west = 0, 0, 0, 0, 0
            tree = int(data[i][j])
            row = data[i]
            col = [data[k][j] for k in range(len(data))]

            for k in range(j - 1, -1, -1):
                west += 1
                if (tree <= int(row[k])):
                    break

            for k in range(j + 1, len(row)):
                east += 1
                if (tree <= int(row[k])):
                    break

            for k in range(i - 1, -1, -1):
                north += 1
                if (tree <= int(col[k])):
                    break

            for k in range(i + 1, len(col)):
                south += 1
                if (tree <= int(col[k])):
                    break

            score = north * south * east * west

            if (score > bestScore):
                bestScore = score

    return bestScore

print(Part1())
print(Part2())
