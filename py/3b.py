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
