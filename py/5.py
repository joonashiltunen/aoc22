with open("5.input") as f:
    lines = [line for line in f.readlines()]
    
stacks = [[] for i in range(9)]
for line in lines:
    if "[" in line:
        for i in range(0, len(line), 4):
            chunk = line[i:i+4].replace("[", "").replace("]", "").strip()
            chunk and stacks[i//4].append(chunk)
    elif "move" in line:
        # move 1 from 3 to 5
        line = line.split()
        for i in range(int(line[1])):
            stacks[int(line[5])-1].insert(0, stacks[int(line[3])-1].pop(0))

print("".join([l[0] for l in stacks]))
