import os

with open("input.txt", "r") as f:
	accumulator = 0
	lines = []

	for line in f:
		lines.append(line.strip())

	index = 0
	visited = set()
	while True:
		if index in visited:
			break

		l = lines[index]
		ops = l.split()
		# print(l)
		# print(accumulator)
		# print(ops[0])
		# exit()

		if ops[0] == "nop":
			visited.add(index)
			index += 1
			continue

		if ops[0] == "acc":
			accumulator += int(ops[1])
			visited.add(index)
			index += 1
			continue

		if ops[0] == "jmp":
			visited.add(index)
			index += int(ops[1])
			continue

	print(accumulator)
	print(sorted(visited))