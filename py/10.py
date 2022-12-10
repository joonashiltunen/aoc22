cycles = [20, 60, 100, 140, 180, 220]
X = 1
c = 0
result = 0
queue=[]
I = iter(open("10.input").readlines())
while True:
    c += 1
    print(c, X)
    if c in cycles:
        result += c * X
    
    try:
        if queue:
            X += queue.pop(0)
        elif line := next(I):
            if line.strip() == "noop":
                pass
            else:
                queue.append(int(line.split()[-1]))
    except StopIteration:
        print(result)
        break
