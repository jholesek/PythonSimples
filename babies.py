#4 lines: Fibonacci, tuple assignment
parents, babies= (1,1)
while babies < 100:
	print(f"This generation has {babies} babies")
	print('L2: This generation has {0} babies'.format(babies))
	parents, babies=(babies, parents+babies)

