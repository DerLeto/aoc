input_path = "input/11.txt"

ROUNDS_1 = 20
ROUNDS_2 = 10000

class Operation:
    def __init__(self, operand1, operation, operand2):
        self.operand1 = operand1
        self.operation = operation
        self.operand2 = operand2

    def compute(self, oldValue):
        operand1 = oldValue if self.operand1 == "old" else int(self.operand1)
        operand2 = oldValue if self.operand2 == "old" else int(self.operand2)

        if self.operation == "+":
            return operand1 + operand2
        elif self.operation == "-":
            return operand1 - operand2
        elif self.operation == "*":
            return operand1 * operand2
        elif self.operation == "/":
            return operand1 / operand2

class Test:
    lcm = 1

    def __init__(self, testValue, posId, negId):
        self.testValue = testValue
        self.posId = posId
        self.negId = negId
        Test.lcm *= testValue

    def test(self, value):
        res = value % self.testValue
        if res == 0:
            return self.posId
        else:
            return self.negId

class Monkey:
    monkeys = {}
    reliefLevel = 1

    def __init__(self, id: int, items: list, operation: Operation, test: Test):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.activityCount = 0
        Monkey.monkeys[id] = self

    def appendItem(self, item):
        self.items.append(item)

    def play(self):
        for item in self.items:
            self.activityCount += 1
            newValue = self.operation.compute(item)
            newValue //= self.reliefLevel
            #print(Test.lcm)
            newValue %= Test.lcm
            newMonkeyId = self.test.test(newValue)
            Monkey.monkeys[newMonkeyId].appendItem(newValue)
        self.items.clear()

    def __str__(self):
        return "Monkey {}: {}".format(self.id, self.activityCount)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.activityCount == other.activityCount

    def __lt__(self, other):
        return self.activityCount < other.activityCount

def parseMonkey(string):
    lines = string.split("\n")
    id = int(lines[0].strip()[-2])
    items = [int(number.strip()) for number in lines[1].split(":")[1].split(",")]
    op_parts = lines[2].split("=")[1].strip().split()
    operation = Operation(*op_parts)
    testValue = int(lines[3].split()[-1].strip())
    posId = int(lines[4].split()[-1].strip())
    negId = int(lines[5].split()[-1].strip())
    test = Test(testValue, posId, negId)
    #print(id, items, op_parts, testValue, posId, negId)
    return Monkey(id, items, operation, test)


def a():
    res = 0
    monkeys = []
    with open(input_path) as file:
        for part in file.read().split("\n\n"):
            monkey = parseMonkey(part)
            monkeys.append(monkey)

    Monkey.reliefLevel = 3
    for i in range(ROUNDS_1):
        #print(monkeys)
        for monkey in monkeys:
            #print(monkey.items)
            monkey.play()

    print(monkeys)
    monkeys.sort()
    print(monkeys)
    res = monkeys[-1].activityCount * monkeys[-2].activityCount

    return res


def b():
    res = 0
    monkeys = []
    with open(input_path) as file:
        for part in file.read().split("\n\n"):
            monkey = parseMonkey(part)
            monkeys.append(monkey)

    Monkey.reliefLevel = 1
    for i in range(ROUNDS_2):
        # print(monkeys)
        for monkey in monkeys:
            # print(monkey.items)
            monkey.play()

    print(monkeys)
    monkeys.sort()
    print(monkeys)
    res = monkeys[-1].activityCount * monkeys[-2].activityCount

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
