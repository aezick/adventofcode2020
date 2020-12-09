import os

with open("input.txt", "r") as f:
	index = 0
	sums = {}
	numbers = []

	preamble_length = 25

	for line in f:
		line = line.strip()
		num = int(line)
		numbers.append(num)

		# print(index)

		if index > preamble_length:
			# print(index)
			for spot in range(index - preamble_length, index):
				# print(spot, range(index - preamble_length, index))
				summ = numbers[spot] + num

				if summ in sums:
					sums[summ].append(spot)
				else:
					sums[summ] = [spot]

			# check for num in sums dict
			found = False
			if num in sums:
				for i in sums[num]:
					if i >= (index - preamble_length - 1):
						found = True

			if not found:
				print("num:", num, " index:", index)
				# print("sums:", sums)
				# the num is 14360655
				exit()

		else:
			spot = 0

			if index == 0:
				# print("once")
				pass
			else:
				while spot < index:
					summ = numbers[spot] + num

					if summ in sums:
						sums[summ].append(spot)
					else:
						sums[summ] = [spot]

					spot += 1

		# print("increment")
		index += 1
