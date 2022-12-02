print(sum(map(lambda g:(lambda x,y:((y+1-x)%3)*3+y+1)(ord(g[0])-65,ord(g[1])-88),[l.split()for l in open("2").readlines()])))
