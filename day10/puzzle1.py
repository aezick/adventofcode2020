import os

with open("input.txt", "r") as f:
	one_gaps = 0
	three_gaps = 1	# built-in adapter
	adapters = []

	for line in f:
		line = line.strip()
		adapters.append(int(line))

	adapters.sort()
	last_adapter = 0

	while len(adapters) > 0:
		new_adapter = adapters[0]

		if new_adapter - last_adapter == 1:
			one_gaps += 1
		elif new_adapter - last_adapter == 3:
			three_gaps += 1

		adapters.pop(0)
		last_adapter = new_adapter

	print(one_gaps, three_gaps, one_gaps * three_gaps)