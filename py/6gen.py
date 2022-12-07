print((lambda chars:f"all_different = lambda {','.join(chars)}:"+"".join([f"{c[0]}!={c[1]} and " for c in __import__("itertools").combinations(chars, 2)])[:-4])([chr(97+i) for i in range(14)]))
