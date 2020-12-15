import os

def down_we_go(number):
	if "X" not in number:
		# print("number:", number)
		return [number]
	else:
		lower = number.replace("X", "0", 1)
		higher = number.replace("X", "1", 1)
		nums = down_we_go(lower) + down_we_go(higher)
		return nums


with open("input.txt", "r") as f:
	memory = {}

	mask = f.readline().strip().split(" ")[2][::-1]

	for line in f:
		line = line.strip()

		if "mask" in line:
			mask = line.strip().split(" ")[2][::-1]
			continue

		# chopped and screwed
		mem_addr = str(bin(int(line.split("[")[1].split("]")[0])))[::-1]
		# normal this time
		num = int(line.split(" ")[2])

		new_addr = ""
		for i in range(0, len(mask)):
			# unchanged
			if mask[i] == "0":
				if i > len(mem_addr) - 3:
					new_addr += "0"
				else:
					new_addr += mem_addr[i]
			# make it a 1
			elif mask[i] == "1":
				new_addr += "1"
			# floating nonsense
			elif mask[i] == "X":
				new_addr += "X"

		# print(mem_addr, num, new_addr[::-1])
		# exit()

		floats = down_we_go(new_addr)
		# print(floats)
		# exit()
		for addr in floats:
			memory[addr] = num

	total = 0
	for addr in memory:
		total += memory[addr]

	print("Total:", total)