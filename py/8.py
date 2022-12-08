m = []
for line in open("8.input").readlines():
    m.append(list(map(int, list(line.strip()))))

vecsum = lambda v1, v2: (v1[0]+v2[0], v1[1]+v2[1])

def search(val, vec, dirvec):
    vec = vecsum(vec, dirvec)
    while vec[0]>=0 and vec[1]>=0 and vec[0]<=len(m[0])-1 and vec[1]<=len(m)-1:
        if m[vec[1]][vec[0]] >= val:
            return False
        vec = vecsum(vec, dirvec)
    return True

result = 0
for x in range(len(m[0])):
    for y in range(len(m)):
        sd = lambda d: search(m[y][x], (x,y), d)
        if sd((0,1)) or sd((0,-1)) or sd((-1,0)) or sd((1,0)):
            result += 1

print(result)
