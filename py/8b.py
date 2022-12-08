m = []
for line in open("8.input").readlines():
    m.append(list(map(int, list(line.strip()))))

vecsum = lambda v1, v2: (v1[0]+v2[0], v1[1]+v2[1])

def search(val, vec, dirvec):
    res = 0
    vec = vecsum(vec, dirvec)
    while vec[0]>=0 and vec[1]>=0 and vec[0]<=len(m[0])-1 and vec[1]<=len(m)-1:
        res += 1
        if m[vec[1]][vec[0]] >= val:
            return res
        vec = vecsum(vec, dirvec)
    return res

result = 0
for x in range(1, len(m[0])-1):
    for y in range(1, len(m)-1):
        sd = lambda d: search(m[y][x], (x,y), d)
        score = sd((0,1)) * sd((0,-1)) * sd((-1,0)) * sd((1,0))
        result = max(score, result)

print(result)
