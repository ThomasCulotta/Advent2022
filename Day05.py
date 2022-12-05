import copy

filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

stacks = []
instructions = []
stackLines = 0

for line in data:
    if (line[1] == "1"):
        stacks = [[] for i in range(int(line[-2]))]
        break

    stackLines += 1

for line in range(stackLines):
    stack = 1
    while stack < len(data[line]):
        if ((crate := data[line][stack]) != " "):
            stacks[(stack - 1) // 4].insert(0, crate)

        stack += 4

instructions = [[int(i) for i in data[line].split() if i.isdigit()] for line in range(stackLines + 2, len(data))]

def Part1():
    stacks1 = copy.deepcopy(stacks)
    for moveNum, fromStack, toStack in instructions:
        stacks1[toStack - 1].extend(stacks1[fromStack - 1][:None if (moveNum == len(stacks1[fromStack - 1])) else len(stacks1[fromStack - 1]) - moveNum - 1:-1])
        stacks1[fromStack - 1] = stacks1[fromStack - 1][:len(stacks1[fromStack - 1]) - moveNum]

    return "".join([stack[-1] for stack in stacks1])

def Part2():
    for moveNum, fromStack, toStack in instructions:
        stacks[toStack - 1].extend(stacks[fromStack - 1][len(stacks[fromStack - 1]) - moveNum:])
        stacks[fromStack - 1] = stacks[fromStack - 1][:len(stacks[fromStack - 1]) - moveNum]

    return "".join([stack[-1] for stack in stacks])

print(Part1())
print(Part2())
