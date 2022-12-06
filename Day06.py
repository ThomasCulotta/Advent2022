filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.read().strip()

def Part1And2(length):
    for i in range(len(data) - length):
        if (len(set(data[i:i + length])) == length):
            return i + length

    return -1

print(Part1And2(4))
print(Part1And2(14))
