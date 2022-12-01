biggest = 0
current = 0

with open("1.input") as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            current += int(line)
        else:
            biggest = max(biggest, current)
            current = 0

print(biggest)
