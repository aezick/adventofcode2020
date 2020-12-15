import os

with open("input.txt", "r") as f:
	count = 0
	numbers = []
	max_turns = 2020

	for line in f:
		line = line.strip().split(",")
		for n in line:
			numbers.insert(0, int(n))
			count += 1

	# print(numbers)
	# exit()
	while count < max_turns:
		num = numbers[0]
		next_num = None

		try:
			prev_spoken = numbers[1:].index(num)
			next_num = prev_spoken + 1
			# print("prev:", prev_spoken, next_num)
		except:
			next_num = 0

		numbers.insert(0, next_num)
		count += 1

	# print(numbers[::-1])
	print(numbers[0])
