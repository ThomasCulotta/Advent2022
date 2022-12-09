from operator import add

filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

def Part1And2(knotCount):
    knotPoses = [[0, 0] for i in range(knotCount)]
    posVisited = set()
    posVisited.add((knotPoses[-1][0], knotPoses[-1][1]))

    for line in data:
        direction, count = line.split()[0], int(line.split()[1])
        delta = [0, 0]

        if   (direction == "U"): delta = [ 0,  1];
        elif (direction == "D"): delta = [ 0, -1];
        elif (direction == "L"): delta = [-1,  0];
        elif (direction == "R"): delta = [ 1,  0];

        for i in range(count):
            knotPoses[0] = list(map(add, knotPoses[0], delta))

            for j in range(1, len(knotPoses)):
                if (abs(knotPoses[j - 1][0] - knotPoses[j][0]) > 1):
                    childDelta = [(knotPoses[j - 1][0] - knotPoses[j][0]) // 2]

                    if (knotPoses[j - 1][1] == knotPoses[j][1]):
                        childDelta.append(0)
                    elif (abs(knotPoses[j - 1][1] - knotPoses[j][1]) == 1):
                        childDelta.append(knotPoses[j - 1][1] - knotPoses[j][1])
                    else:
                        childDelta.append((knotPoses[j - 1][1] - knotPoses[j][1]) // 2)

                    knotPoses[j] = list(map(add, knotPoses[j], childDelta))

                elif (abs(knotPoses[j - 1][1] - knotPoses[j][1]) > 1):
                    childDelta = [(knotPoses[j - 1][1] - knotPoses[j][1]) // 2]

                    if (knotPoses[j - 1][0] == knotPoses[j][0]):
                        childDelta.insert(0, 0)
                    elif (abs(knotPoses[j - 1][0] - knotPoses[j][0]) == 1):
                        childDelta.insert(0, knotPoses[j - 1][0] - knotPoses[j][0])
                    else:
                        childDelta.insert(0, (knotPoses[j - 1][0] - knotPoses[j][0]) // 2)

                    knotPoses[j] = list(map(add, knotPoses[j], childDelta))

            posVisited.add((knotPoses[-1][0], knotPoses[-1][1]))

    return len(posVisited)

print(Part1And2(2))
print(Part1And2(10))
