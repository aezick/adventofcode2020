import copy
import os

def recurse_adapters(adapters, previous_adapter, count):
	# print(previous_adapter, count)

	if len(adapters) == 0:
		return count + 1

	if len(adapters) == 1:
		return count + 1

	if adapters[0] - previous_adapter == 3:
		return recurse_adapters(copy.deepcopy(adapters[1:]), adapters[0], count)

	elif adapters[0] - previous_adapter == 2:
		if adapters[1] - previous_adapter == 3:
			return recurse_adapters(copy.deepcopy(adapters[1:]), adapters[0], count) \
				+ recurse_adapters(copy.deepcopy(adapters[2:]), adapters[1], count)
		else:
			return recurse_adapters(copy.deepcopy(adapters[1:]), adapters[0], count)

	elif adapters[0] - previous_adapter == 1:
		# print("curr and prev:", adapters[0], previous_adapter)
		if adapters[1] - previous_adapter == 3:
			return recurse_adapters(copy.deepcopy(adapters[1:]), adapters[0], count) \
				+ recurse_adapters(copy.deepcopy(adapters[2:]), adapters[1], count)

		elif adapters[1] - previous_adapter == 2:
			# print("another level:", adapters[0], previous_adapter)
			if len(adapters) > 2 and (adapters[2] - previous_adapter == 3):
				# print("final boss:", adapters[0], previous_adapter)
				return recurse_adapters(copy.deepcopy(adapters[1:]), adapters[0], count) \
				+ recurse_adapters(copy.deepcopy(adapters[2:]), adapters[1], count) \
				+ recurse_adapters(copy.deepcopy(adapters[3:]), adapters[2], count)
			else:
				return recurse_adapters(copy.deepcopy(adapters[1:]), adapters[0], count) \
				+ recurse_adapters(copy.deepcopy(adapters[2:]), adapters[1], count)
			# else:
			# 	return recurse_adapters(copy.deepcopy(adapters[1:]), adapters[0], count)

		else:
			return recurse_adapters(copy.deepcopy(adapters[1:]), adapters[0], count)
	else:
		print("impossible?")


with open("input.txt", "r") as f:
	total = 0
	adapters = []

	for line in f:
		line = line.strip()
		adapters.append(int(line))

	adapters.sort()
	last_adapter = 0

	total = recurse_adapters(adapters, 0, 0)

	print("Total:", total)