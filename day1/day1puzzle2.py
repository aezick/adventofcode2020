import os

with open("input.txt", "r") as f:
	numbers = []
	for line in f:
		numbers.append(int(line))

	i = 0
	while i < len(numbers):
		j = 0
		while j < len(numbers):
			k = 0
			while k < len(numbers):
				if (numbers[i] + numbers[j] + numbers[k]) == 2020:
					print(numbers[i], numbers[j], numbers[k])
					print(numbers[i] * numbers[j] * numbers[k])
					exit(0)
				k += 1
			j += 1
		i += 1
