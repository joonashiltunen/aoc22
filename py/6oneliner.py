(lambda l:[len(set(l[i-4:i]))==4 and exit(str(i))for i in range(len(l))])(open("6").read())
