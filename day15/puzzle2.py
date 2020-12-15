import os

with open("input.txt", "r") as f:
	count = 0
	prev_num = None
	numbers = []
	max_turns = 30000000
	prev_turn_used = {}

	for line in f:
		line = line.strip().split(",")
		for n in line:
			n = int(n)
			prev_num = n
			prev_turn_used[n] = count
			numbers.append(n)
			count += 1

	# print(prev_num, prev_turn_used)
	# exit()
	while count < max_turns:
		next_num = None
		# print(prev_num)

		if prev_num in prev_turn_used:
			prev_spoken = prev_turn_used[prev_num]
			next_num = count - prev_spoken - 1
			prev_turn_used[prev_num] = count - 1
			# print("prev:", count, prev_num, prev_spoken, next_num)
		else:
			next_num = 0
			prev_turn_used[prev_num] = count - 1
	
		numbers.append(next_num)
		count += 1
		prev_num = next_num

	# print("Expected:", "[0, 3, 6, 0, 3, 3, 1, 0, 4, 0]")
	# print("Actual  :", numbers)
	print(numbers[-1])
