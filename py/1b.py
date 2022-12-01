top3 = [0]*3
current = 0

with open("1.input") as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            current += int(line)
        else:
            if current > top3[0]:
                top3[0] = current
                top3.sort()
            current = 0

print(sum(top3))
