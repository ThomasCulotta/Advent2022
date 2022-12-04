filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = [[[int(endpoint) for endpoint in elfRange.split("-")] for elfRange in line.split(",")] for line in file.readlines()]

def Part1():
    total = 0

    for pair in data:
        elf1, elf2 = pair

        if ((elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or
            (elf2[0] <= elf1[0] and elf2[1] >= elf1[1])):
            total += 1

    return total

def Part2():
    total = 0

    for pair in data:
        elf1, elf2 = pair

        if ((elf2[0] in range(elf1[0], elf1[1] + 1)) or
            (elf1[0] in range(elf2[0], elf2[1] + 1))):
            total += 1

    return total

print(Part1())
print(Part2())
