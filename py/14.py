vecsum = lambda v1, v2: (v1[0]+v2[0], v1[1]+v2[1])
vecdist = lambda v1, v2: (v2[0]-v1[0], v2[1]-v1[1])
normalize = lambda v: (v[0] and abs(v[0])//v[0], v[1] and abs(v[1])//v[1])

fall_priority = [(0, 1), (-1, 1), (1, 1)]

def parse_vec(p):
    p = p.split(",")
    return int(p[0]), int(p[1])

XLIMIT = YLIMIT = 1000
smallest_x = XLIMIT
smallest_y = 0 # sand starts at y=0
largest_x = 501 # sand starts at x=500
largest_y = 0
M = [["." for i in range(XLIMIT)] for i in range(YLIMIT)]
for line in [l.strip() for l in open("14.input").readlines()]:
    l = line.split(" -> ")
    for i,k in enumerate(l[:-1]):
        start = parse_vec(k)
        end = parse_vec(l[i+1])
        
        # for visualization mainly
        smallest_x = min(smallest_x, start[0], end[0])
        smallest_y = min(smallest_y, start[1], end[1])
        largest_x = max(largest_x, start[0], end[0])
        largest_y = max(largest_y, start[1], end[1])
        
        print(start, " -> ", end, normalize(vecdist(start, end)))
        
        pt = start
        d = normalize(vecdist(start, end))
        M[pt[1]][pt[0]] = "#"
        while pt != end:
            pt = vecsum(pt, d)
            M[pt[1]][pt[0]] = "#"

M[0][500] = "+"
        
def vis(M):
    for x in M[smallest_y:largest_y+2]:
        print("".join(x[smallest_x-1:largest_x+2]))
    print(smallest_x, largest_x, smallest_y, largest_y)

v = lambda t: M[t[1]][t[0]]
result = 0
while True:
    ns = (500,0) # new sand falling
    falling = True
    while falling:
        falling = False
        for fd in fall_priority:
            if v(vecsum(ns, fd)) == ".":
                ns = vecsum(ns, fd)
                falling = True
                break
    M[ns[1]][ns[0]] = "o"
    vis(M)    
    result += 1
    print(result)
