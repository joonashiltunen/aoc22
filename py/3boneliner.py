print(sum(map(lambda r:r>96 and r-96 or r-38,(lambda l:[ord(min(set(l[i])&set(l[i+1])&set(l[i+2])))for i in range(0,len(l),3)])(open("3").read().split()))))
