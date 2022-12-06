(lambda l:[len(set(l[i-14:i]))==14 and exit(str(i))for i in range(len(l))])(open("6").read())
