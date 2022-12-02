print(sum(map(lambda g:(lambda x,y:3*y+(x+y-1)%3+1)(ord(g[0])-65,ord(g[1])-88),[l.split()for l in open("2").readlines()])))
