import copy
import os

# weird algorithm, not sure if works? avoids recursion as that was too slow
with open("input.txt", "r") as f:
	adapters = []
	consecutive_ones = {2: 0, 3: 0, 4: 0}

	for line in f:
		line = line.strip()
		adapters.append(int(line))

	adapters.sort()
	# print(adapters)

	counter = 0
	prev_adapter = 0
	for a in adapters:
		# print(a - prev_adapter)
		if a - prev_adapter == 3:
			if counter == 3:
				consecutive_ones[3] += 1
			elif counter == 2:
				consecutive_ones[2] += 1
			elif counter == 4:
				consecutive_ones[4] += 1

			counter = 0

		elif a - prev_adapter == 1:
			counter += 1			

		if counter == 4:
			consecutive_ones[4] += 1
			counter = 0

		prev_adapter = a

	# print(consecutive_ones)
	print("Total:", (7 ** consecutive_ones[4]) * (4 ** consecutive_ones[3]) * (2 ** consecutive_ones[2]))