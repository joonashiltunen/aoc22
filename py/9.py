visited = [] # set()
dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

vecsum = lambda v1, v2: (v1[0]+v2[0], v1[1]+v2[1])
def vecdist(v1, v2):
    xd = v2[0]-v1[0]
    yd = v2[1]-v1[1]
    return (xd, yd)
    
def vecabs(v):
    return (abs(v[0]), abs(v[1]))
   
def toofar(v): # returns 1 for 2-space normal case, 2 for diagonal move required
    v = vecabs(v)
    if v[0]==v[1]: return 1
    return sum(v)

#test
h = (4,2)
t = (3,0)
print(toofar(vecdist(h,t)))


H = (0, 0)
T = (0, 0)
for line in open("9.input").readlines():
    d = line[0]
    print(d)
    moves = int(line.strip()[2:])
    for i in range(moves):
        H = vecsum(H, dirs[d])
        if f := toofar(vecdist(T, H)):
            #if f == 1:
                #T = vecsum(T, dirs[d])
            if f > 1:
                x,y=vecdist(T, H)
                if x==0 or y==0:
                    T = vecsum(T, dirs[d])
                elif abs(x)==1 and abs(y)==2:
                    T = vecsum(T, (x, abs(y)//y))
                elif abs(x)==2 and abs(y)==1:
                    T = vecsum(T, (abs(x)//x, y))
                else:
                    raise Exception("unexpected diag move")
            visited.append(T)
        print(H, T)
   
print(len(set(visited)))
