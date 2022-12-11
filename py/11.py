class Monkey:
    def __init__(self, op, test, items):
        self.op = op
        self.test = test
        self.items = items
        self.inspections = 0
        
    def inspected(self):
        self.inspections += 1
        
monkeys = []  
monkeys.append(Monkey(lambda x: x*3,  lambda x: x%2==0 and 1 or 4,  [66, 59, 64, 51])) # 0
monkeys.append(Monkey(lambda x: x*19, lambda x: x%7==0 and 3 or 5,  [67, 61])) # 1
monkeys.append(Monkey(lambda x: x+2,  lambda x: x%11==0 and 4 or 0, [86, 93, 80, 70, 71, 81, 56])) # 2
monkeys.append(Monkey(lambda x: x*x,  lambda x: x%19==0 and 7 or 6, [94])) # 3
monkeys.append(Monkey(lambda x: x+8,  lambda x: x%3==0 and 5 or 1,  [71, 92, 64])) # 4
monkeys.append(Monkey(lambda x: x+6,  lambda x: x%5==0 and 3 or 6,  [58, 81, 92, 75, 56])) # 5
monkeys.append(Monkey(lambda x: x+7,  lambda x: x%17==0 and 7 or 2, [82, 98, 77, 94, 86, 81])) # 6
monkeys.append(Monkey(lambda x: x+4,  lambda x: x%13==0 and 2 or 0, [54, 95, 70, 93, 88, 93, 63, 50])) # 7

for rd in range(20):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.op(monkey.items.pop(0))
            monkey.inspected()
            item //= 3
            monkeys[monkey.test(item)].items.append(item)

r = sorted([m.inspections for m in monkeys])[-2:]
print(r[0]*r[1])
