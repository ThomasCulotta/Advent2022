filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

def Part1():
    cycles = [20, 60, 100, 140, 180, 220]
    strengths = []
    x = 1
    cycle = 1

    for line in data:
        if (cycle == cycles[0]):
            strengths.append(cycles.pop(0) * x)

            if (len(cycles) == 0):
                return sum(strengths)

        if line == "noop\n":
            cycle += 1
            continue

        addx = int(line.split()[1])
        if (cycles[0] - cycle < 2):
            strengths.append(cycles.pop(0) * x)

            if (len(cycles) == 0):
                return sum(strengths)

        x += addx
        cycle += 2

    return -1

def Part2():
    pixels = []
    x = 1
    cycle = 1

    for line in data:
        pixels.append("#" if (abs(x - (cycle - 1) % 40) < 2) else " ")

        if line == "noop\n":
            cycle += 1
            continue

        pixels.append("#" if (abs(x - cycle % 40) < 2) else " ")
        addx = int(line.split()[1])
        x += addx
        cycle += 2

    for i in range(0, 240, 40):
        print("".join(pixels[i:i + 40]))

print(Part1())
Part2()
