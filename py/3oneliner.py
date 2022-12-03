print(sum(map(lambda r:r>96 and r-96 or r-38,[ord(list(set(l[:len(l)//2])&set(l[len(l)//2:]))[0])for l in open("3").readlines()])))
