dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

vecsum = lambda v1, v2: (v1[0]+v2[0], v1[1]+v2[1])
vecdist = lambda v1, v2: (v2[0]-v1[0], v2[1]-v1[1])
   
def toofar(dist):
    v = abs(dist[0]), abs(dist[1])
    return (v[0]==v[1] and abs(v[0]) or sum(v)) > 1

K = [(0, 0) for i in range(10)]
visited = set()
for line in open("9.input").readlines():
    for _move in range(int(line[2:])):
        K[0] = vecsum(K[0], dirs[line[0]])
        for i in range(1, len(K)):
            dist = vecdist(K[i], K[i-1])
            if toofar(dist):
                x, y = dist
                K[i] = vecsum(K[i], (x and abs(x)//x, y and abs(y)//y))
            visited.add(K[-1])

print(len(visited))
