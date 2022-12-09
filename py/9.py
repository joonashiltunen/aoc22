dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

vecsum = lambda v1, v2: (v1[0]+v2[0], v1[1]+v2[1])
vecdist = lambda v1, v2: (v2[0]-v1[0], v2[1]-v1[1])

def toofar(dist):
    v = abs(dist[0]), abs(dist[1])
    if v[0]==v[1]: 
        return False
    return sum(v) > 1

H = T = (0, 0)
visited = set()
for line in open("9.input").readlines():
    for _move in range(int(line.strip()[2:])):
        H = vecsum(H, dirs[line[0]])
        if toofar(vecdist(T, H)):
            x, y = vecdist(T, H)
            T = vecsum(T, (x and abs(x)//x, y and abs(y)//y))
        visited.add(T)

print(len(visited))
