with open("3.input") as f:
    lines = [line.strip() for line in f.readlines()]

def find_one(a, b, c):
    for x in a:
        for y in b:
            for z in c:
                if x==y==z:    
                    return x
                
result_letters = []
i = 0
while i < len(lines):
    a = lines[i]
    b = lines[i+1]
    c = lines[i+2]
    result_letters.append(find_one(a,b,c))
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
