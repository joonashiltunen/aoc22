m = []
for line in open("12.input").readlines():
    m.append(list(map(ord, list(line.strip()))))

TARGET = 69
START = 83
XLIMIT = len(m[0])
YLIMIT = len(m)

def v(vec):
    return m[vec[1]][vec[0]]
get_value = v

def gd(from_cell):
    nu = from_cell[1] < YLIMIT - 1 and (from_cell[0],     from_cell[1] + 1) or None
    nd = from_cell[1] > 0          and (from_cell[0],     from_cell[1] - 1) or None
    nr = from_cell[0] < XLIMIT - 1 and (from_cell[0] + 1, from_cell[1])     or None
    nl = from_cell[0] > 0          and (from_cell[0] - 1, from_cell[1])     or None
    return [n for n in [nu, nd, nr, nl] if n]
    
def dirs_to_go_to(from_cell, visited):
    dirs = gd(from_cell)
    return [d for d in dirs if good_loc(from_cell, d, visited)]
        
def good_loc(prev, d, visited):
    if d in visited:
        return False
    v_prev = (v(prev) == ord("S") and ord("a") or v(prev))
    v_d = (v(d) == ord("E") and ord("z") or v(d))
    return v_d - v_prev <=1

tree = {}
start = ()
target = ()
for i in range(XLIMIT):
    for j in range(YLIMIT):
        if v((i,j))==START:
            start = (i,j)
        if v((i,j))==TARGET:
            target = (i,j)
        tree[(i,j)] = dirs_to_go_to((i,j), [])

print(len(tree))
print(start)
print(target)

def bfs(tree, root):
    parents = {}
    Q = [root]
    explored = [root]
    while Q:
        v = Q.pop(0)
        if v == target:
            p = parents[v]
            d = 1
            path = [v, p]
            while True:
                if p in parents:
                    p = parents[p]
                    path.append(p)
                    d += 1
                else:
                    break
            vis = [[chr(get_value((i,j))) for i in range(XLIMIT)] for j in range(YLIMIT)]
            for i in range(XLIMIT):
                for j in range(YLIMIT):
                    if (i,j) in path:
                        vis[j][i]=chr(get_value((i,j))-(ord("a")-ord("A")))
            for x in vis:
                print("".join(x))
            return d
        for w in dirs_to_go_to(v, explored):
            explored.append(w)
            Q.append(w)
            parents[w] = v
            
print(bfs(tree, start))
