import copy
import os

with open("input.txt", "r") as f:
	accumulator = 0
	lines = []

	for line in f:
		lines.append(line.strip())

	for i in range(0,len(lines)):
		# print(accumulator)
		accumulator = 0

		fresh_lines = copy.deepcopy(lines)
		l = fresh_lines[i]
		ops = l.split()

		if ops[0] == "acc":
			continue

		if ops[0] == "nop":
			new_line = "jmp " + ops[1]
			fresh_lines[i] = new_line
		elif ops[0] == "jmp":
			new_line = "nop " + ops[1]
			fresh_lines[i] = new_line

		index = 0
		visited = set()
		while True:
			if index in visited:
				break

			try:
				l = fresh_lines[index]
			except:
				print("Answer:", accumulator)
				exit()
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

	# print(accumulator)
	# print(sorted(visited))