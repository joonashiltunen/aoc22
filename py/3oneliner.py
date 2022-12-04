print(sum(map(lambda r:r>96 and r-96 or r-38,[ord(min(set(l[:len(l)//2])&set(l[len(l)//2:])))for l in open("3").readlines()])))
