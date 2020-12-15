import os

with open("input.txt", "r") as f:
	memory = {}

	mask = f.readline().strip().split(" ")[2][::-1]

	for line in f:
		line = line.strip()

		if "mask" in line:
			mask = line.strip().split(" ")[2][::-1]
			continue

		# print(line)
		mem_addr = line.split("[")[1].split("]")[0]
		num = str(bin(int(line.split(" ")[2])))[::-1]

		new_num = ""
		for i in range(0, len(mask)):
			if mask[i] != "X":
				new_num += mask[i]
			else:
				if i > len(num) - 3:
					new_num += "0"
				else:
					new_num += num[i]

		# print(mem_addr, num[::-1], new_num[::-1], int(new_num[::-1], 2))
		# exit()

		num = int(new_num[::-1], 2)
		memory[mem_addr] = num

	total = 0
	for addr in memory:
		total += memory[addr]

	print("Total:", total)