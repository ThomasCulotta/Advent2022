filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

dirs = {}

def Part1():
    currentDir = ""
    totalSize = 0
    testSize = 0

    for line in data:
        if (line[0] == "$"):
            inputs = line[1:].split()

            if (inputs[0] == "cd"):
                if (inputs[1] == ".."):
                    lastIndex = currentDir[-2::-1].index("/")
                    currentDir = currentDir[:len(currentDir) - lastIndex - 1]

                elif (inputs[1] == "/"):
                    currentDir = "/"

                else:
                    currentDir += inputs[1] + "/"

                if (currentDir not in dirs):
                    dirs[currentDir] = 0

        elif ((size := line.split()[0]).isdigit()):
            testSize += int(size)
            dirs[currentDir] = dirs[currentDir] + int(size)

            parent = currentDir
            while parent != "/":
                lastIndex = parent[-2::-1].index("/")
                parent = parent[:len(parent) - lastIndex - 1]
                dirs[parent] = dirs[parent] + int(size)

    for size in dirs.values():
        if (size <= 100000):
            totalSize += size

    return totalSize

def Part2():
    deletionCandidates = [d for d in dirs.values() if (dirs["/"] - d) <= 40000000]

    return min(deletionCandidates)

print(Part1())
print(Part2())
