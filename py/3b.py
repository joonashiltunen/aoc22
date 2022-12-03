with open("3.input") as f:
    lines = [line.strip() for line in f.readlines()]

result_letters = []
i = 0
while i < len(lines):
    a = set(lines[i])
    b = set(lines[i+1])
    c = set(lines[i+2])
    result_letters.append((a & b & c).pop())
    i += 3
    
def to_priority(r):
    r = ord(r)
    if r >= ord('a'):
        return r - ord('a') + 1
    return r - ord('A') + 27
    
result = 0
for r in result_letters:
    result += to_priority(r)

print(result)
