filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

def Part1():
    total = 0

    scores = {
        "A X\n": 4,
        "A Y\n": 8,
        "A Z\n": 3,
        "B X\n": 1,
        "B Y\n": 5,
        "B Z\n": 9,
        "C X\n": 7,
        "C Y\n": 2,
        "C Z\n": 6
    }

    for match in data:
        total += scores[match]

    return total

def Part2():
    total = 0

    scores = {
        "A X\n": 3,
        "A Y\n": 4,
        "A Z\n": 8,
        "B X\n": 1,
        "B Y\n": 5,
        "B Z\n": 9,
        "C X\n": 2,
        "C Y\n": 6,
        "C Z\n": 7
    }

    for match in data:
        total += scores[match]

    return total

print(Part1())
print(Part2())
