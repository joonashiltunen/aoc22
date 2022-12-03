with open("3.input") as f:
    lines = [line.strip() for line in f.readlines()]
                
result_letters = []
for line in lines:
    a = set(line[:len(line)//2])
    b = set(line[len(line)//2:])
    result_letters.append((a & b).pop())
    
def to_priority(r):
    r = ord(r)
    if r >= ord('a'):
        return r - ord('a') + 1
    return r - ord('A') + 27

print(sum(map(to_priority, result_letters)))
