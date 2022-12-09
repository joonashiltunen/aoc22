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
    if v[0]==v[1]: return abs(v[0])
    return sum(v)

#test
h = (2,4)
t = (2,2)
print(vecdist(h,t))
print(toofar(vecdist(h,t)))


K = [(0, 0) for i in range(10)]
for line in open("9.input").readlines():
    d = line[0]
    print(line)
    moves = int(line.strip()[2:])
    for i in range(moves):
        K[0] = vecsum(K[0], dirs[d]) # head moves
        for jj in range(1, len(K)):
            if f := toofar(vecdist(K[jj], K[jj-1])):
                #if f == 1:
                    #T = vecsum(T, dirs[d])
                if f > 1:
                    x,y=vecdist(K[jj], K[jj-1])
                    if x==0 or y==0:
                        if x==0:
                            K[jj] = vecsum(K[jj], (0, abs(y)//y))
                        elif y==0:
                            K[jj] = vecsum(K[jj], (abs(x)//x, 0))
                    elif abs(x)==1 and abs(y)==2:
                        K[jj] = vecsum(K[jj], (x, abs(y)//y))
                    elif abs(x)==2 and abs(y)==1:
                        K[jj] = vecsum(K[jj], (abs(x)//x, y))
                    elif abs(x)==2 and abs(y)==2:
                        K[jj] = vecsum(K[jj], (abs(x)//x, abs(y)//y))
                    else:
                        print(x,y)
                        raise Exception("unexpected diag move")
            visited.append(K[-1])
        print(K, len(set(visited)))
   
    
    
print(len(set(visited)))