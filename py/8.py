m = []
vis = set()

for line in open("8.input").readlines():
    m.append(list(map(int, list(line.strip()))))
    
ylimit = len(m)-1
xlimit = len(m[0])-1

print(xlimit, ylimit)

def down(val, y, x):
    yi = y+1
    while yi<=ylimit:
        if m[yi][x] >= val:
            return False
        yi += 1
    return True
    
def up(val, y, x):
    yi = y-1
    print("up:")
    print(val, y, x)
    while yi>=0:
        print(m[yi][x])
        if m[yi][x] >= val:
            print(False)
            return False
        yi -= 1
    return True
    
def right(val, y, x):
    xi = x+1
    print("right:")
    print(val, y, x)
    while xi<=xlimit:
        print(m[y][xi])
        if m[y][xi] >= val:
            print(False)
            return False
        xi += 1
    return True
    
def left(val, y, x):
    xi = x-1
    print("left:")
    print(val, y, x)
    while xi>=0:
        print(m[y][xi])
        if m[y][xi] >= val:
            print(False)
            return False
        xi -= 1
    return True

for x in range(len(m[0])):
    for y in range(len(m)):
        t=(x,y)
        if x==0 or y==0 or x==xlimit or y==ylimit:
            vis.add(t)
        else:
            val=m[y][x]
            if down(val, y, x) or up(val, y, x) or left(val, y, x) or right(val, y, x):
                print(t)
                vis.add(t)
                
            
print(vis)
print(len(vis))
