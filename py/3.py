with open("3.input") as f:
    lines = [line.strip() for line in f.readlines()]

def find_one(a, b):
    for x in a:
        for y in b:
            if x==y:    
                return x
                
result_letters = []
for line in lines:
    a = line[:len(line)//2]
    b = line[len(line)//2:]
    result_letters.append(find_one(a,b))
    
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
