print(f"{__import__('timeit').timeit(main, number=1000)*1000:.5f}ms")
