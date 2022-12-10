X = 1
c = 0
output = ""
queue=[]
I = iter(open("10.input").readlines())
while True:
    print(c, X)
    if abs(c%40 - X) < 2:
        output += "#"
    else:
        output += "."
        
    c+=1
    
    try:
        if queue:
            X += queue.pop(0)
        elif line := next(I):
            if line.strip() == "noop":
                pass
            else:
                queue.append(int(line.split()[-1]))
    except StopIteration:
        for i in range(0, len(output), 40):
            print(output[i:i+40])
        break
