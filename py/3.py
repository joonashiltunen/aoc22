with open("3.input") as f:
    lines = [line.strip() for line in f.readlines()]
                
result_letters = []
for line in lines:
    a = set(line[:len(line)//2])
    b = set(line[len(line)//2:])
    result_letters.append((a & b).pop())
    
result = 0
for r in result_letters:
    r = ord(r)
    if r >= ord('a'):
        r = r - ord('a') + 1
    else:
        r = r - ord('A') + 27
    print(r)
    result += r

print(result)
