import copy
from operator import add, mul

filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

monkeys1 = []
monkeys2 = []
worryMod = 1

class Monkey:
    items = []
    baseOp = 0
    operation = 0
    throw = 0
    mod = 0
    testAgainst = 0
    trueMonkey = 0
    falseMonkey = 0

    inspectionCount = 0
    relief = 3

    def __init__(self, items, baseOp, mod, testAgainst, trueMonkey, falseMonkey, monkeys):
        self.items = items
        self.baseOp = baseOp
        self.mod = mod
        self.testAgainst = testAgainst
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.throw = lambda item : monkeys[self.trueMonkey if (item % self.testAgainst == 0) else self.falseMonkey].AddItem(item % worryMod)

        if (self.mod == "old"):
            self.operation = lambda item : self.baseOp(item, item) // self.relief
        else:
            self.operation = lambda item : self.baseOp(item, self.mod) // self.relief


    def NoRelief(self):
        if (self.mod == "old"):
            self.operation = lambda item : self.baseOp(item, item)
        else:
            self.operation = lambda item : self.baseOp(item, self.mod)

    def AddItem(self, item):
        self.items.append(item)

    def Turn(self):
        inspected = list(map(self.operation, self.items))
        self.inspectionCount += len(inspected)
        self.items = []
        list(map(self.throw, inspected))

for i in range(0, len(data), 7):
    items = data[i + 1].split(":")[1]
    items = [int(item) for item in items.split(",")]
    baseOp = add if "+" in data[i + 2] else mul
    mod = int(data[i + 2].split()[-1]) if data[i + 2].split()[-1].isdigit() else "old"
    testAgainst = int(data[i + 3].split()[-1])
    trueMonkey = int(data[i + 4].split()[-1])
    falseMonkey = int(data[i + 5].split()[-1])
    worryMod *= testAgainst

    monkeys1.append(Monkey(items, baseOp, mod, testAgainst, trueMonkey, falseMonkey, monkeys1))
    monkeys2.append(Monkey(copy.copy(items), baseOp, mod, testAgainst, trueMonkey, falseMonkey, monkeys2))

def Part1():
    for _ in range(20):
        for monkey in monkeys1:
            monkey.Turn()

    counts = sorted([monkey.inspectionCount for monkey in monkeys1])

    return counts[-1] * counts[-2]

def Part2():
    for monkey in monkeys2:
        monkey.NoRelief()

    for i in range(10000):
        for monkey in monkeys2:
            monkey.Turn()

    counts = sorted([monkey.inspectionCount for monkey in monkeys2])

    return counts[-1] * counts[-2]

print(Part1())
print(Part2())
