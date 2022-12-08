m = []
vis = set()

for line in open("8.input").readlines():
    m.append(list(map(int, list(line.strip()))))
    
ylimit = len(m)-1
xlimit = len(m[0])-1

print(xlimit, ylimit)

def down(val, y, x):
    print("down")
    yi = y+1
    score=1
    while yi<=ylimit:
        if m[yi][x] >= val:
            print(score)
            return score
        yi += 1
        score += 1
    return score-1
    
def up(val, y, x):
    print("up")
    yi = y-1
    score=1
    while yi>=0:
        print(m[yi][x])
        if m[yi][x] >= val:
            print(score)
            return score
        yi -= 1
        score += 1
    return score-1
    
def right(val, y, x):
    print("right")
    xi = x+1
    score=1
    while xi<=xlimit:
        print(m[y][xi])
        if m[y][xi] >= val:
            print(score)
            return score
        xi += 1
        score += 1
    return score-1
    
def left(val, y, x):
    print("left")
    xi = x-1
    score=1
    while xi>=0:
        print(m[y][xi])
        if m[y][xi] >= val:
            print(score)
            return score
        xi -= 1
        score += 1
    return score-1

for x in range(len(m[0])):
    for y in range(len(m)):
        print()
        print()
        t=(x,y)
        if x==0 or y==0 or x==xlimit or y==ylimit:
            continue
        
        val=m[y][x]
        print(t,  val)
        score=[up(val, y, x), left(val, y, x), down(val, y, x), right(val, y, x)]
        vis.add(score[0]*score[1]*score[2]*score[3])

                
            
print(vis)
print(max(vis))
