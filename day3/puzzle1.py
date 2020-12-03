import os

with open("input.txt", "r") as f:
	p = 0
	count = 0

	for line in f:
		if p >= len(line.strip()):
			# print(p, len(line))
			p -= len(line.strip())

		if line[p] == '#':
			count += 1

		p += 3

	print(count)
