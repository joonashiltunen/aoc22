print(sum(map(lambda r:r>96 and r-96 or r-38,[ord((set(l[:len(l)//2])&set(l[len(l)//2:])).pop())for l in open("3").readlines()])))
